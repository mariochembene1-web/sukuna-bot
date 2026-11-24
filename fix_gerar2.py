import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
if "GERAR_NATURAL" not in t:
    # mete antes do PERGUNTAR_IA no privado
    old = "const respA = await PERGUNTAR_IA(txtAudio"
    # vamos meter o gatilho natural no inicio do tratamento de texto privado
    # procura onde começa a responder no privado - usa o texto normal
    # fallback: mete função helper no topo
    helper = """
async function GERAR_NATURAL(sock, from, m, texto){
  const low = texto.toLowerCase();
  const gatilhos = ['gera uma foto','gerar uma foto','cria uma foto','criar uma foto','gera uma imagem','cria uma imagem','me gera','gera foto','faz uma foto','faz uma imagem'];
  let g = gatilhos.find(g=> low.includes(g));
  if(!g) return false;
  let prompt = texto;
  for(const gg of gatilhos){ prompt = prompt.replace(new RegExp(gg,'i'),''); }
  prompt = prompt.replace(/^(de|uma|um|do|da|pra mim|para mim)/i,'').trim();
  if(!prompt) prompt = 'leao majestoso';
  try{
    await sock.sendMessage(from, {text:'🎨 A gerar tua foto... espera um pouco pha 🔥'}, {quoted:m});
    const url = 'https://image.pollinations.ai/prompt/' + encodeURIComponent(prompt + ', high quality, detailed') + '?width=1024&height=1024&seed=' + Math.floor(Math.random()*999999) + '&nologo=true';
    await sock.sendMessage(from, {image:{url:url}, caption:'🎨 *' + prompt + '*\\n\\n👑 *SUKUNA MESTRE*'}, {quoted:m});
  }catch(e){ await sock.sendMessage(from, {text:'Eish, falhou a gerar a foto, tenta de novo.'}, {quoted:m}); }
  return true;
}
"""
    # insere helper antes de TRANSCREVER_AUDIO
    t = t.replace("async function TRANSCREVER_AUDIO", helper + "\nasync function TRANSCREVER_AUDIO", 1)
    # tenta chamar no privado: antes de PERGUNTAR_IA(texto
    if "PERGUNTAR_IA(texto" in t:
        t = t.replace("PERGUNTAR_IA(texto", "GERAR_NATURAL(sock, from, m, texto) ? null : PERGUNTAR_IA(texto", 1)
        # isso não é ideal, vamos fazer de forma simples: procura o bloco de resposta privada
        print("HELPER CRIADO - mas preciso de ajuste manual")
    else:
        print("HELPER CRIADO")
    p.write_text(t)
else:
    print("JA EXISTE")
