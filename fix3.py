import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()
# remove o bloco quebrado - vai de VER TABELA até ao proximo // VER PAGAMENTO
pat = re.compile(r"// VER TABELA.*?// VER PAGAMENTO", re.DOTALL)
new = "// VER TABELA - SO NO PV\n  if(cmd==='.tabela'||cmd==='tabela'){\n   let _eGrupo = String(from||'').endsWith('@g.us');\n   if(_eGrupo){ await sock.sendMessage(from,{text:'Tabela so no PV! Fala comigo no privado e escreve tabela - Mario Oficialz'},{quoted:m}); return; }\n   let tb=tabelas[from] || Object.values(tabelas)[0] || '';\n   if(!tb){await sock.sendMessage(from,{text:'TABELA VAZIA - Pede ao ADM para colocar a tabela!'},{quoted:m});return;}\n   await sock.sendMessage(from,{text:tb},{quoted:m});\n   return;\n  }\n  // VER PAGAMENTO"
if pat.search(t):
    t = pat.sub(new, t, count=1)
    p.write_text(t)
    print("ARRUMADO")
else:
    print("NAO ACHEI")
