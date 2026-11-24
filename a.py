import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
if "verificarCalor" in t:
    print("JA EXISTE")
else:
    func = """
let alertaCalorLigado = false;
let grupoAlerta = null;
async function verificarCalor(sock){
  try{
    let r = await fetch('https://api.open-meteo.com/v1/forecast?latitude=-25.965&longitude=32.583&current=temperature_2m,relative_humidity_2m&timezone=Africa%2FMaputo');
    let d = await r.json();
    let temp = d.current.temperature_2m;
    let hum = d.current.relative_humidity_2m;
    if(temp >= 35){
      let msg = 'ALERTA CALOR: Maputo ' + temp + 'C Hum ' + hum + '% Bebe agua!';
      if(alertaCalorLigado && grupoAlerta){ try{ await sock.sendMessage(grupoAlerta, {text: msg}); }catch(e){} }
      return msg;
    }
    return null;
  }catch(e){ return null; }
}
"""
    cmds = """
if(textoLow === '.alertacalor on'){
  alertaCalorLigado = true;
  try{ grupoAlerta = from; globalThis.sockAlerta = sock; }catch(e){}
  await reply('ALERTA CALOR LIGADO');
  return;
}
if(textoLow === '.alertacalor off'){
  alertaCalorLigado = false;
  await reply('Alerta desligado.');
  return;
}
if(textoLow === '.alertacalor testar'){
  let msg = await verificarCalor(sock);
  await reply(msg || 'Agora esta fresco, sem alerta.');
  return;
}
"""
    t = func + "\\n" + t
    t = t.replace("if(textoLow", cmds + "\\nif(textoLow", 1)
    t += "\\nsetInterval(async () => { if(alertaCalorLigado) await verificarCalor(globalThis.sockAlerta); }, 3600000);\\n"
    p.write_text(t)
    print("ALERTACALOR INSTALADO!")
