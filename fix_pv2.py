import pathlib
p = pathlib.Path("index.js")
t = p.read_text()

# 1. Troca só as 2 linhas do PV
t = t.replace("{ text: respPV }", "{ text: organizar(respPV) }")
t = t.replace("{text: respA}", "{text: organizar(respA)}")

# 2. Troca a função organizar sem usar regex
inicio = t.find("function organizar")
if inicio != -1:
    fim = t.find("\n}\n", inicio) + 3
    nova = "function organizar(s){\n  let x = String(s||'').split('**').join('*').split('###').join('').split('##').join('').trim();\n  x = x.split('\\n\\n\\n').join('\\n\\n');\n  return x;\n}\n"
    t = t[:inicio] + nova + t[fim:]
    print("ORGANIZAR TROCADO ✅")
else:
    print("NAO ACHEI organizar")

print("PV:", "organizar(respPV)" in t)
print("AUDIO:", "organizar(respA)" in t)
p.write_text(t)
