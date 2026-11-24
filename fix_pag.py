import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()
pat = re.compile(r"// VER PAGAMENTO.*?return;\s*\}\s*\}catch", re.DOTALL)
new = """// VER PAGAMENTO - GRUPO MANDA NO PV + PV DIRETO
  if(cmd==='.pagamento'||cmd==='pagamento'){
   let pg=pags[from] || Object.values(pags)[0] || '';
   if(!pg){await sock.sendMessage(from,{text:'PAGAMENTO VAZIO - Pede ao ADM para colocar as formas de pagamento! - SUKUNA MESTRE'},{quoted:m});return;}
   let _txt='FORMAS DE PAGAMENTO - SUKUNA MESTRE - ' + pg + ' - Depois manda o comprovativo! - Dono: Mario Oficialz';
   let _eGrupo = String(from||'').endsWith('@g.us');
   if(_eGrupo){
    let _dest='';
    try{ _dest = m.key.participant || ''; }catch{}
    let _ok=false;
    try{ if(_dest){ await sock.sendMessage(_dest,{text:_txt}); _ok=true; } }catch{}
    if(_ok){ await sock.sendMessage(from,{text:'Te mandei o pagamento no teu PV! Confere la! - SUKUNA MESTRE'},{quoted:m}); }
    else{ await sock.sendMessage(from,{text:_txt},{quoted:m}); }
    return;
   }
   await sock.sendMessage(from,{text:_txt},{quoted:m});
   return;
  }catch"""
if pat.search(t):
    t = pat.sub(new, t, count=1)
    p.write_text(t)
    print("PAGAMENTO PV POSTO")
else:
    print("NAO ACHEI PAGAMENTO")
