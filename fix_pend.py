import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()
# 1. descobre o id do grupo atual - usa o que já existe no teu código
# tenta achar variável do chat
grupo_var = "from"
if "remoteJid" in t:
    grupo_var = "msg?.key?.remoteJid || from"

# 2. filtra a lista de pendentes: só do grupo atual
# procura todas as listas de pendentes e mete filtro
# padrão mais comum: Object.values(...pendentes...)
orig = t
t = re.sub(
    r"Object\.values\((global\.pendentes|pendentes)\)",
    r"Object.values(\1).filter(pp => !pp.grupo || pp.grupo === ("+grupo_var+") || String(texto||'').toLowerCase().includes('todos'))",
    t
)
if t != orig:
    print("FILTRO POR GRUPO POSTO")
else:
    print("NAO ACHEI Object.values(pendentes) - manda: grep -n pendentes index.js | head -30")

# 3. atualiza a descrição no menu ADM certo
t = t.replace(
    "▪️ .pendentes = Ver pagamentos à espera de confirmação",
    "▪️ .pendentes = Ver pendentes SÓ deste grupo\n▪️ .pendentes todos = Ver pendentes de todos os grupos (só dono)"
)
p.write_text(t)
print("OK")
