import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
old = "prompt = prompt + ' ' + promptEN;"
novo = "if(promptEN.toLowerCase() !== prompt.toLowerCase()) prompt = prompt + ' ' + promptEN;"
if old in t:
    t = t.replace(old, novo)
    print("DUPLICADO CORRIGIDO")
else:
    print("NAO ACHEI")
p.write_text(t)
