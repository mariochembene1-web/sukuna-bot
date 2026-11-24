import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()
# acha o bloco VER TABELA até ao return; }
pat = re.compile(r"// VER TABELA.*?if\(cmd==='\.tabela'\|\|cmd==='tabela'\).*?return;\s*\}", re.DOTALL)
new = """// VER TABELA - SO NO PV
  if(cmd==='.tabela'||cmd==='tabela'){
   let _eGrupo = String(from||'').endsWith('@g.us');
   if(_eGrupo){ await sock.sendMessage(from,{text:'📋 *Tabela só no PV!*\\n\\nFala comigo no privado e escreve *tabela* 👑\\n👤 Mário Oficialz'},{quoted:m}); return; }
   let tb=tabelas[from] || Object.values(tabelas)[0] || '';
   if(!tb){await sock.sendMessage(from,{text:'📋 *TABELA VAZIA* 📋\\n\\nPede ao ADM para colocar a tabela! 🙏'},{quoted:m});return;}
   await sock.sendMessage(from,{text:tb},{quoted:m});
   return;
  }"""
m = pat.search(t)
if m:
    print("ACHEI:", m.group(0)[:120])
    t = pat.sub(new, t, count=1)
    p.write_text(t)
    print("TABELA PV ONLY POSTA")
else:
    print("AINDA NAO ACHEI")
