import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
# o erro é aqui: falta um } antes do catch da TABELA
old = "  }catch(e){console.log('TABELA ERRO'"
new = "  }\n  }catch(e){console.log('TABELA ERRO'"
if old in t:
    t = t.replace(old, new, 1)
    p.write_text(t)
    print("FECHADO")
else:
    print("NAO ACHEI CATCH - manda sed -n '1630,1650p' index.js")
