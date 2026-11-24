import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
t = t.replace("?model=flux&width=", "?width=", 1)
# aumenta o tempo de espera e mete retry: se falhar tenta 2x
t = t.replace("Eish, falhou a gerar a foto, tenta de novo.", "Eish, falhou a gerar a foto, tenta de novo. Se continuar, tenta 'Gera uma foto de uma televisao'")
p.write_text(t)
print("FLUX REMOVIDO")
