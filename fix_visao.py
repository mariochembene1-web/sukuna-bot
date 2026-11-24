import pathlib
p = pathlib.Path("index.js")
t = p.read_text()

# Acha só a função VISAO
ini = t.find("async function PERGUNTAR_IA_VISAO")
fim = t.find("async function GERAR_NATURAL", ini)
bloco = t[ini:fim]

# 1. Tira o bloco da pesquisa que usa isGrupo (só na VISAO)
velho = """    let infoPesquisa = '';
    if(!isGrupo){"""
if velho in bloco:
    # tira do let infoPesquisa até ao fecho do if
    a = bloco.find("    let infoPesquisa = '';")
    b = bloco.find("const r = await fetch('https://api.groq.com/openai/v1/chat/completions'", a)
    bloco = bloco[:a] + bloco[b:]
    print("BUG isGrupo TIRADO ✅")
else:
    print("NAO ACHEI BLOCO isGrupo")

# 2. Troca modelo que não vê foto por um que vê
if "qwen/qwen3.8-27b" in bloco:
    bloco = bloco.replace("qwen/qwen3.8-27b", "meta-llama/llama-4-scout-17b-16e-instruct")
    print("MODELO VISAO TROCADO ✅")

# 3. Aumenta resposta da visão
bloco = bloco.replace("max_tokens:800", "max_tokens:1500")
bloco = bloco.replace(".slice(0,1500)", ".slice(0,2500)")

t = t[:ini] + bloco + t[fim:]
p.write_text(t)
print("VISAO ARRanjADA")
