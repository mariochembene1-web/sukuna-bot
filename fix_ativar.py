import re
txt = open('index.js', encoding='utf-8', errors='ignore').read()

# 1. Helper - cola depois da linha dos gruposAtivos, se ainda nao existir
if 'parseTempoAtivar' not in txt:
    txt = txt.replace(
        "let gruposAtivos",
        "function parseTempoAtivar(a){\n  if(!a) return null;\n  a=String(a).toLowerCase().trim();\n  if(a.endswith('h')){ let n=parseInt(a); return n>0? n*3600000 : null; }\n  if(a.endswith('d')){ let n=parseInt(a); return n>0? n*86400000 : null; }\n  if(a.endswith('m')){ let n=parseInt(a); return n>0? n*60000 : null; }\n  let n=parseInt(a); return n>0? n*86400000 : null;\n}\nfunction textoTempoAtivar(ms){\n  if(ms>=86400000) return (ms/86400000).toFixed(ms%86400000==0?0:1)+' dias';\n  if(ms>=3600000) return (ms/3600000).toFixed(1)+' horas';\n  return Math.round(ms/60000)+' minutos';\n}\nlet gruposAtivos",
        1
    )

# 2. Fix ATIVAR_TOPO - linha 921
txt = txt.replace(
    "let diasTop = parseInt((texto||'').split(' ')[1]);            if(!diasTop){ await sock.sendMessage(from,{text:'❌ Usa assim: .ativar 5'},{quoted:m}); return; }",
    "let argTop=(texto||'').split(' ')[1]||''; let msTop=parseTempoAtivar(argTop); let diasTop=msTop? Math.ceil(msTop/86400000):0; if(!msTop){ await sock.sendMessage(from,{text:'❌ Usa assim: .ativar 12h | .ativar 1d | .ativar 7d | .ativar 5'},{quoted:m}); return; }"
)
# fallback se espacos diferentes
if "let diasTop = parseInt" in txt:
    txt = re.sub(r"let diasTop = parseInt.*?return; \}", "let argTop=(texto||'').split(' ')[1]||''; let msTop=parseTempoAtivar(argTop); let diasTop=msTop? Math.ceil(msTop/86400000):0; if(!msTop){ await sock.sendMessage(from,{text:'❌ Usa assim: .ativar 12h | .ativar 1d | .ativar 7d | .ativar 5'},{quoted:m}); return; }", txt, count=1, flags=re.DOTALL)

# 3. Troca calculo diasTop*24h por msTop
txt = txt.replace("gruposAtivos[from]={ate: Date.now()+diasTop*24*60*60*1000, dias: diasTop}", "gruposAtivos[from]={ate: Date.now()+msTop, dias: diasTop, tempoTxt: textoTempoAtivar(msTop)}")

# 4. Fix segundo .ativar (linha 2633)
txt = txt.replace(
    "let dias = parseInt(arg);                                     if(!dias || dias < 1){ await reply('❌ Usa assim: *.ativar 5*\\nEx: *.ativar 1* / *.ativar 2* / *.ativar 5*'); return; }",
    "let msAt=parseTempoAtivar(arg); let dias=msAt? Math.ceil(msAt/86400000):0; if(!msAt){ await reply('❌ Usa assim: *.ativar 12h*\\nEx: *.ativar 12h* / *.ativar 1d* / *.ativar 7d* / *.ativar 5*'); return; }"
)
# fallback generico
if "let dias = parseInt(arg);" in txt:
    txt = txt.replace("let dias = parseInt(arg);", "let msAt=parseTempoAtivar(arg); let dias=msAt? Math.ceil(msAt/86400000):0;")
    txt = txt.replace("if(!dias || dias < 1)", "if(!msAt)")

txt = txt.replace("gruposAtivos[from] = { ate: Date.now() + dias*24*60*60*1000, dias: dias }", "gruposAtivos[from] = { ate: Date.now() + msAt, dias: dias, tempoTxt: textoTempoAtivar(msAt) }")
txt = txt.replace("gruposAtivos[from]={ate: Date.now()+diasTop*24*60*60*1000", "gruposAtivos[from]={ate: Date.now()+msTop")

open('index.js','w',encoding='utf-8').write(txt)
print('FIX OK - parseTempoAtivar:', 'parseTempoAtivar' in txt)
