import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
# acha a linha do .clima neste menu ADM e mete o alerta logo a seguir
alvo = "▪️ .clima"
if alvo in t:
    # só na primeira ocorrência do menu ADM
    pos = t.find(alvo)
    fim_linha = t.find("\n", pos)
    linha = t[pos:fim_linha]
    nova = linha + "\n▪️ .alertacalor on = Ligar alerta de calor neste grupo 🔥\n▪️ .alertacalor off = Desligar alerta de calor\n▪️ .alertacalor testar = Testar alerta de calor agora 🌡️"
    t = t[:pos] + nova + t[fim_linha:]
    print("POSTO NO MENU ADM CERTO")
else:
    print("NAO ACHEI .clima - manda o grep")
p.write_text(t)
