import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
old = "let lista = Object.keys(pendentes).map(k =>"
new = "let _verTodos = String(texto||'').toLowerCase().includes('todos') && isDono;\n      let _chavesPend = Object.keys(pendentes).filter(k => _verTodos || !pendentes[k].grupo || pendentes[k].grupo === from);\n      let lista = _chavesPend.map(k =>"
if old in t:
    t = t.replace(old, new, 1)
    print("FILTRO POR GRUPO POSTO - .pendentes")
else:
    print("NAO ACHEI - manda a linha de novo")
p.write_text(t)
