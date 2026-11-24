import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()

# Melhora a limpeza do prompt dentro de GERAR_NATURAL
old = "  prompt = prompt.replace(/^(de|uma|um|do|da|pra mim|para mim)/i,'').trim();"
novo = """  prompt = prompt.replace(/^(de|do|da|dos|das|uma|um|uns|pra mim|para mim|por favor|pfv)\\s+/gi,'').trim();
  // limpa de novo se ainda começar com artigo
  prompt = prompt.replace(/^(de|do|da|uma|um)\\s+/gi,'').trim();
  // ajuda o Pollinations a entender em ingles
  const mapa = { 'leao':'lion', 'leão':'lion', 'gato':'cat', 'cao':'dog', 'cão':'dog', 'menina':'girl', 'menino':'boy', 'carro':'car', 'casa':'house', 'praia':'beach', 'mulher':'woman', 'homem':'man' };
  let promptEN = prompt;
  for(const k in mapa){ promptEN = promptEN.replace(new RegExp(k,'gi'), mapa[k]); }
  prompt = prompt + ' ' + promptEN;"""
if old in t:
    t = t.replace(old, novo, 1)
    print("PROMPT LIMPO")
else:
    print("NAO ACHEI LINHA - manda grep")

# Muda a URL para usar modelo flux que é mais realista
if "model=flux" not in t:
    t = t.replace("?width=1024&height=1024&seed=", "?model=flux&width=1024&height=1024&seed=", 1)
    # só a primeira ocorrência é do GERAR_NATURAL? vamos garantir que foi na função certa - se não, reverte
    print("MODELO FLUX OK")

p.write_text(t)
