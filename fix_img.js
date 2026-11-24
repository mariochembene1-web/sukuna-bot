const fs = require('fs');
let t = fs.readFileSync('index.js','utf8');

// 1. importa tesseract no topo se não existir
if(!t.includes("tesseract.js")){
  t = t.replace(/const.*require\(.*baileys.*\)/i, (m)=> m + "\nconst Tesseract = require('tesseract.js');");
  // fallback se não achar baileys
  if(!t.includes("tesseract.js")) t = "const Tesseract = require('tesseract.js');\n" + t;
  console.log('tesseract importado');
}

// 2. função OCR - cola depois do primeiro "function" ou no topo
if(!t.includes('lerTextoDaImagem')){
  let func = `
async function lerTextoDaImagem(sock, m){
  try{
    let buf = await sock.downloadMediaMessage(m);
    if(!buf) return '';
    let r = await Tesseract.recognize(buf, 'por+eng');
    return r.data.text || '';
  }catch(e){ console.log('OCR erro:', e.message); return ''; }
}
`;
  // cola logo antes de onde começa o detector de texto, ou depois dos requires
  if(t.includes('COMPROVATIVO DETECTADO')) t = t.replace('COMPROVATIVO DETECTADO', func + '\n// COMPROVATIVO DETECTADO');
  else t = func + t;
  console.log('funcao OCR adicionada');
}

// 3. gancho: se for imagem, faz OCR e mete o texto na mesma variável que o detector de texto usa
// Procura a linha onde ele pega o texto: body / texto / msgText
if(!t.includes('OCR_COMPROVATIVO')){
  // Tenta apanhar depois de definir o texto da mensagem
  let re = /(let\s+(body|texto|text|msgText)\s*=.*?;)/;
  if(re.test(t)){
    t = t.replace(re, "$1\n    // OCR_COMPROVATIVO - se for imagem, lê o texto da foto\n    if(m.message?.imageMessage && !body){\n      try{ body = await lerTextoDaImagem(sock, m); console.log('OCR:', body.slice(0,200)); }catch(e){}\n    }\n    if(m.message?.imageMessage && body && !m.message?.conversation){\n      // se já tinha body de legenda, junta com OCR\n      try{ let ocr = await lerTextoDaImagem(sock, m); if(ocr) body = body + '\\n' + ocr; }catch(e){}\n    }");
    console.log('gancho OCR colado no body');
  } else {
    console.log('NAO ACHEI body/texto - manda: grep -n "let body\\|let texto\\|let text" index.js');
  }
}

fs.writeFileSync('index.js', t);
console.log('FEITO');
