import pathlib
p = pathlib.Path("index.js")
t = p.read_text()

# 1. Cria função PESQUISAR - Wikipedia PT
func_pesq = """
async function PESQUISAR_WEB(pergunta){
  try{
    let q = String(pergunta||'').toLowerCase().trim();
    q = q.replace(/^(quem e|quem é|o que e|o que é|me fala sobre|fala sobre|explica|quem|o que|onde|quando|qual)\\s+/,'').replace(/[?!.]/g,'').trim();
    if(!q || q.length < 2) return '';
    // tira palavras extra, fica só o nome: "quem e oruam" -> "oruam"
    let partes = q.split(' ');
    let termo = partes.slice(-2).join(' ');
    if(partes.length <= 3) termo = q;
    let url = 'https://pt.wikipedia.org/api/rest_v1/page/summary/' + encodeURIComponent(termo);
    let r = await fetch(url, {headers:{'User-Agent':'SUKUNA-Bot'}});
    if(!r.ok){
      // tenta só última palavra
      let url2 = 'https://pt.wikipedia.org/api/rest_v1/page/summary/' + encodeURIComponent(partes[partes.length-1]);
      r = await fetch(url2, {headers:{'User-Agent':'SUKUNA-Bot'}});
      if(!r.ok) return '';
    }
    let j = await r.json();
    if(!j.extract) return '';
    return 'INFO DA PESQUISA sobre ' + termo + ': ' + j.extract.slice(0,1200);
  }catch(e){ return ''; }
}
"""
if "PESQUISAR_WEB" not in t:
    t = t.replace("async function PERGUNTAR_IA", func_pesq + "\nasync function PERGUNTAR_IA")
    print("PESQUISAR CRIADO ✅")
else:
    print("JA TINHA PESQUISAR")

# 2. Dentro do PERGUNTAR_IA, antes de chamar Groq, pesquisa se for PV e for pergunta
ancora = "const r = await fetch('https://api.groq.com/openai/v1/chat/completions'"
if "infoPesquisa" not in t:
    codigo = """
    let infoPesquisa = '';
    if(!isGrupo){
      try{
        let lowQ = String(pergunta||'').toLowerCase();
        if(lowQ.includes('quem') || lowQ.includes('o que') || lowQ.includes('onde') || lowQ.includes('quando') || lowQ.includes('qual') || lowQ.includes('explica') || lowQ.includes('oruam') || lowQ.includes('fala sobre')){
          infoPesquisa = await PESQUISAR_WEB(pergunta);
        }
      }catch(e){}
    }
    """
    t = t.replace(ancora, codigo + "\n    " + ancora)
    print("PESQUISA LIGADA NO PV ✅")
else:
    print("JA LIGADO")

# 3. Mete a pesquisa dentro da mensagem que vai para IA
velho = "contexto + contextoPag + '\\n\\nMensagem do cliente: '"
novo = "contexto + contextoPag + (infoPesquisa ? '\\n\\n' + infoPesquisa : '') + '\\n\\nMensagem do cliente: '"
if velho in t:
    t = t.replace(velho, novo)
    print("INFO INJETADA ✅")
else:
    print("NAO ACHEI MENSAGEM - manda sed 101,185")

# 4. Tira o corte de 800 que deixava resposta a meio
t = t.replace(".slice(0,800)", ".slice(0,2500)")
print("CORTE AUMENTADO ✅")

p.write_text(t)
