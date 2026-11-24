import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
ini = t.find("async function PERGUNTAR_IA_VISAO")
fim = t.find("async function GERAR_NATURAL", ini)
bloco = t[ini:fim]
# Troca Groq por OpenRouter na VISAO só
bloco = bloco.replace("process.env.GROQ_API_KEY", "process.env.OPENROUTER_API_KEY")
bloco = bloco.replace("https://api.groq.com/openai/v1/chat/completions", "https://openrouter.ai/api/v1/chat/completions")
bloco = bloco.replace("meta-llama/llama-4-scout-17b-16e-instruct", "qwen/qwen2.5-vl-32b-instruct:free")
# OpenRouter precisa de mais headers
bloco = bloco.replace("'Content-Type':'application/json'", "'Content-Type':'application/json','HTTP-Referer':'https://sukuna.bot','X-Title':'SUKUNA'")
t = t[:ini] + bloco + t[fim:]
p.write_text(t)
print("VISAO NO OPENROUTER ✅")
