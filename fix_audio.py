import pathlib
p = pathlib.Path("index.js")
t = p.read_text()

# 1. Cria função de transcrever se ainda não existe
if "TRANSCREVER_AUDIO" not in t:
    func = """
async function TRANSCREVER_AUDIO(buf, mime){
  try{
    const key = process.env.GROQ_API_KEY;
    if(!key) return '';
    const form = new FormData();
    form.append('file', new Blob([buf], {type: mime||'audio/ogg'}), 'audio.ogg');
    form.append('model', 'whisper-large-v3-turbo');
    form.append('language', 'pt');
    const r = await fetch('https://api.groq.com/openai/v1/audio/transcriptions', {method:'POST', headers:{'Authorization':'Bearer '+key}, body: form, signal: AbortSignal.timeout(60000)});
    if(!r.ok){ console.log('ERRO WHISPER:', r.status); return ''; }
    const j = await r.json();
    return (j.text||'').trim();
  }catch(e){ console.log('ERRO TRANSCREVER:', e.message); return ''; }
}
function parseComprovativo(txt){
"""
    t = t.replace("function parseComprovativo(txt){", func, 1)
    print("FUNCAO CRIADA")
else:
    print("FUNCAO JA EXISTE")

# 2. Mete tratamento de áudio no privado, antes da imagem
old = "const imgMsg = m.message?.imageMessage"
novo = """const audioMsg = m.message?.audioMessage || m.message?.viewOnceMessageV2?.message?.audioMessage || m.message?.viewOnceMessage?.message?.audioMessage;
      if (audioMsg) {
        try{
          try{ await sock.sendPresenceUpdate('recording', from); }catch(e){}
          const streamA = await downloadContentFromMessage(audioMsg, 'audio');
          let bufA = Buffer.alloc(0);
          for await (const chunk of streamA) bufA = Buffer.concat([bufA, chunk]);
          const txtAudio = await TRANSCREVER_AUDIO(bufA, audioMsg.mimetype||'audio/ogg');
          try{ await sock.sendPresenceUpdate('paused', from); }catch(e){}
          if(!txtAudio){ await sock.sendMessage(from, {text:'Eish, não consegui ouvir esse áudio, manda de novo pha.'}, {quoted:m}); }
          else {
            try{ await sock.sendPresenceUpdate('composing', from); }catch(e){}
            const respA = await PERGUNTAR_IA(txtAudio, m.pushName || 'amigo', '', '', false);
            await sock.sendMessage(from, {text: respA}, {quoted:m});
          }
        }catch(e){ console.log('ERRO AUDIO PV:', e.message); await sock.sendMessage(from, {text:'Eish, falhou a ouvir o áudio, tenta de novo.'}, {quoted:m}); }
        return;
      }
      const imgMsg = m.message?.imageMessage"""
if old in t and "audioMsg" not in t.split("PRIVADO = SO IA")[1].split("const imgMsg")[0]:
    t = t.replace(old, novo, 1)
    print("AUDIO NO PRIVADO OK")
else:
    print("AUDIO JA ESTAVA OU NAO ACHEI")

p.write_text(t)
