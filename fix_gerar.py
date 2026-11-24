import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
if ".gerar" not in t:
    old = "const cmd = textoLow.split(/\\s+/)[0];"
    novo = """if (textoLow.startsWith('.gerar ') || textoLow.startsWith('.imagem ') || textoLow.startsWith('.foto ia ')) {
      const prompt = texto.replace(/^\\.(gerar|imagem|foto ia)\\s+/i,'').trim();
      if(!prompt){ await sock.sendMessage(from, {text:'Manda assim: *.gerar um leao com coroa dourada*'}, {quoted:m}); return; }
      try{
        await sock.sendMessage(from, {text:'🎨 A gerar tua foto... espera um pouco pha 🔥'}, {quoted:m});
        const url = 'https://image.pollinations.ai/prompt/' + encodeURIComponent(prompt + ', high quality, detailed') + '?width=1024&height=1024&seed=' + Math.floor(Math.random()*999999) + '&nologo=true';
        await sock.sendMessage(from, {image:{url:url}, caption:'🎨 *' + prompt + '*\\n\\n👑 *SUKUNA MESTRE*'}, {quoted:m});
      }catch(e){ await sock.sendMessage(from, {text:'Eish, falhou a gerar a foto, tenta de novo.'}, {quoted:m}); }
      return;
    }
    const cmd = textoLow.split(/\\s+/)[0];"""
    t = t.replace(old, novo, 1)
    print("GERAR CRIADO")
else:
    print("JA EXISTE")
p.write_text(t)
