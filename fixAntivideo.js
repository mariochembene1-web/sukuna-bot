const fs=require('fs');
let t=fs.readFileSync('index.js','utf8');
let log=[];

// 1 - Declarar antivideoGrupos + carregar antivideo.json (copia do antifoto)
if(!t.includes('antivideoGrupos')){
  // tenta achar a linha do antifoto
  let m=t.match(/.*antifotoGrupos.*\n/);
  if(m){
    t=t.replace(m[0], m[0] + m[0].replace(/antifoto/g,'antivideo').replace(/antifoto\.json/g,'antivideo.json'));
    log.push('1- declaracao OK');
  } else {
    t=t.replace("let antilinkGrupos", "let antivideoGrupos={};\ntry{ antivideoGrupos=JSON.parse(fs.readFileSync('antivideo.json')); }catch{}\nlet antilinkGrupos");
    log.push('1- declaracao fallback OK');
  }
}
// 2 - Salvar no save()
if(!t.includes('antivideo.json') || !t.includes("antivideoGrupos")){
  // ja tratado acima
}
if(t.includes('antifoto.json') && !t.includes("antivideoGrupos')") && !t.includes('antivideo.json", JSON')){
  // tenta adicionar no save
}
t=t.replace("fs.writeFileSync('antifoto.json', JSON.stringify(antifotoGrupos));", "fs.writeFileSync('antifoto.json', JSON.stringify(antifotoGrupos)); fs.writeFileSync('antivideo.json', JSON.stringify(antivideoGrupos));");
log.push('2- save OK');

// 3 - Comando .antivideo (copia do .antilink da linha 2786)
if(!t.includes("cmd === '.antivideo'") && !t.includes('cmd===".antivideo"')){
  let blocoAntilink = t.match(/if \(cmd === '\.antilink'\) \{[\s\S]*?return; \} {3}/);
  if(!blocoAntilink) blocoAntilink = t.match(/if \(cmd === '\.antilink'\) \{[\s\S]*?\n {4}\}/);
  if(blocoAntilink){
    let novo = blocoAntilink[0].replace(/antilink/g,'antivideo').replace(/ANTI-LINK/g,'ANTI-VIDEO').replace(/Anti-link/g,'Anti-video').replace(/anti-link/g,'anti-video').replace(/🔗/g,'🎬').replace(/Mandou link/g,'Mandou video');
    t=t.replace(blocoAntilink[0], blocoAntilink[0] + "\n    " + novo);
    log.push('3- comando OK');
  } else log.push('3- NAO ACHEI BLOCO ANTILINK, manda print da linha 2786-2795');
}

// 4 - Deteccao + punicao igual antilink da linha 3086
if(!t.includes('antivideoGrupos[from]')){
  let linha = t.match(/.*antilinkGrupos\[from\].*LINK_REGEX.*\n([\s\S]*?)\n {4}\n/);
  // fallback: insere antes do antilink 3086
  let idx = t.indexOf("antilinkGrupos[from] && !isAdm");
  if(idx>-1){
    // acha inicio da linha
    let start = t.lastIndexOf("\n", idx)+1;
    let bloco = `    if (isGroup && antivideoGrupos[from] && !isAdm && (m.message?.videoMessage || m.message?.documentWithCaptionMessage?.message?.videoMessage)) {\n      try{ await sock.sendMessage(from, { delete: m.key }); }catch(e){}\n      let key = from+'_'+senderNum; warns[key]=(warns[key]||0)+1; let total=warns[key]; save();\n      if (total >= 5) { warns[key] = 0; save(); await sock.sendMessage(from, { text: '🚨 *ANTI-VIDEO - REMOVIDO*\\n\\n━━━━━━━━━━━━━━\\n👤 *Pessoa:* @' + senderNum + '\\n⚠️ *Avisos:* 5/5\\n🎬 *Motivo:* Mandou video 5 vezes\\n👑 *Dono:* Mário Oficialz\\n━━━━━━━━━━━━━━\\n\\n> *Foi removido!*\\n\\n✨ *SUKUNA MESTRE*', mentions: [sender] }); try { await sock.groupParticipantsUpdate(from, [sender], 'remove'); } catch {} }\n      else await sock.sendMessage(from, { text: '⚠️ *ANTI-VIDEO - AVISO ' + total + '/5*\\n\\n━━━━━━━━━━━━━━\\n👤 *Pessoa:* @' + senderNum + '\\n🎬 *Video apagado!*\\n⚠️ *Avisos:* ' + total + '/5\\n🚨 *No 5º serás removido!*\\n━━━━━━━━━━━━━━\\n\\n👑 *SUKUNA MESTRE*', mentions: [sender] });\n      return;\n    }\n`;
    t = t.slice(0,start) + bloco + t.slice(start);
    log.push('4- deteccao OK');
  } else log.push('4- NAO ACHEI LINHA 3086');
}

// 5 - Menu: adicionar .antivideo
t=t.replace(".antilink .antisticker", ".antilink .antivideo .antisticker");
t=t.replace("▪️ .antilink on / off", "▪️ .antilink on / off\\n▪️ .antivideo on / off");

fs.writeFileSync('index.js', t);
console.log(log.join('\\n'));
console.log('FIM');
