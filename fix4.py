import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()
pat = re.compile(r"// VER TABELA - SO NO PV.*?// VER PAGAMENTO", re.DOTALL)
new = "// VER TABELA - SO NO PV\n  if(cmd==='.tabela'||cmd==='tabela'){\n   let _eGrupo = String(from||'').endsWith('@g.us');\n   let tb=tabelas[from] || Object.values(tabelas)[0] || '';\n   if(!tb){await sock.sendMessage(from,{text:'TABELA VAZIA - Pede ao ADM para colocar a tabela!'},{quoted:m});return;}\n   if(_eGrupo){\n    let _dest = '';\n    try{ _dest = m.key.participant || m.key.remoteJid || ''; }catch{}\n    if(!_dest && typeof sender!=='undefined') _dest = sender;\n    if(_dest){ await sock.sendMessage(_dest,{text:tb}); }\n    return;\n   }\n   await sock.sendMessage(from,{text:tb},{quoted:m});\n   return;\n  }\n  // VER PAGAMENTO"
if pat.search(t):
    t = pat.sub(new, t, count=1)
    p.write_text(t)
    print("AGORA MANDA NO PV SEM FALAR NO GRUPO")
else:
    print("NAO ACHEI")
