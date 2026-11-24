import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()
pat = re.compile(r"// VER TABELA - SO NO PV.*?// VER PAGAMENTO", re.DOTALL)
new = "// VER TABELA - GRUPO E PV\n  if(cmd==='.tabela'||cmd==='tabela'){\n   let tb=tabelas[from] || Object.values(tabelas)[0] || '';\n   if(!tb){await sock.sendMessage(from,{text:'TABELA VAZIA - Pede ao ADM para colocar a tabela!'},{quoted:m});return;}\n   await sock.sendMessage(from,{text:tb},{quoted:m});\n   return;\n  }\n  // VER PAGAMENTO"
if pat.search(t):
    t = pat.sub(new, t, count=1)
    p.write_text(t)
    print("VOLTOU AO NORMAL")
else:
    print("NAO ACHEI")
