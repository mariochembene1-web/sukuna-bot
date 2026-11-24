import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
t = t.replace("\\nlet", "\nlet")
t = t.replace("\\nif(textoLow", "\nif(textoLow")
t = t.replace("\\nsetInterval", "\nsetInterval")
# tira o \n do fim
if t.endswith("\\n"):
    t = t[:-2] + "\n"
p.write_text(t)
print("CORRIGIDO!")
