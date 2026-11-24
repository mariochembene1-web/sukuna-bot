import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
old = "'TABELA: .settabela .tabela .setpreco .verpreco'"
new = "'TABELA: .settabela .tabela .setpreco .verpreco','ALERTA CALOR: .alertacalor on / off / testar'"
if old in t:
    t = t.replace(old, new, 1)
    print("MENU ATUALIZADO")
else:
    print("NAO ACHEI A LINHA DO MENU, manda grep .menu")
p.write_text(t)
