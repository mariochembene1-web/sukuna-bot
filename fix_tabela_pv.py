import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
old = """  // VER TABELA - só deste grupo
  if(cmd==='.tabela'||cmd==='tabela'){                           let tb=tabelas[from];
   if(!tb){await sock.sendMessage(from,{text:'📋 *TABELA VAZIA* 📋\\n\\n> *Pede ao ADM para colocar a tabela!* 🙏'},{quoted:m});return;}                                                       await sock.sendMessage(from,{text:tb},{quoted:m});
   return;                                                      }"""
new = """  // VER TABELA - SO NO PV
  if(cmd==='.tabela'||cmd==='tabela'){
   let _eGrupo = String(from||'').endsWith('@g.us');
   if(_eGrupo){ await sock.sendMessage(from,{text:'📋 *Tabela só no PV!*\\n\\nFala comigo no privado e escreve *tabela* 👑\\n👤 Mário Oficialz'},{quoted:m}); return; }
   let tb=tabelas[from] || Object.values(tabelas)[0] || '';
   if(!tb){await sock.sendMessage(from,{text:'📋 *TABELA VAZIA* 📋\\n\\n> *Pede ao ADM para colocar a tabela!* 🙏'},{quoted:m});return;}
   await sock.sendMessage(from,{text:tb},{quoted:m});
   return;
  }"""
if old in t:
    t=t.replace(old,new,1)
    p.write_text(t)
    print("TABELA PV ONLY POSTA")
else:
    print("NAO ACHEI BLOCO EXATO - manda grep VER TABELA")
