import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
# Limpa LaTeX de TODAS as respostas da IA
old = "let respIA = await PERGUNTAR_IA"
if old in t and "LIMPA_LATEX" not in t:
    novo = """let respIA = await PERGUNTAR_IA
        // LIMPA_LATEX - WhatsApp nao entende $ \\times etc
        try{
          respIA = String(respIA).replace(/\\$+/g,'').replace(/\\\\times/g,' x ').replace(/\\\\div/g,' / ').replace(/\\\\frac\\{([^}]+)\\}\\{([^}]+)\\}/g,'($1/$2)').replace(/\\\\[a-zA-Z]+/g,'').replace(/_\\{([^}]+)\\}/g,'$1').replace(/_([0-9A-Za-z])/g,'$1').replace(/\\^\\{([^}]+)\\}/g,'^$1').replace(/\\^{([0-9A-Za-z])}/g,'^$1');
        }catch(e){}"""
    t = t.replace(old, novo, 1)
    print("LATEX LIMPO NA IA PRINCIPAL")
else:
    print("JA TEM OU NAO ACHEI - manda grep PERGUNTAR_IA")

# Tambem reforça no prompt da IA para nao usar LaTeX
if "NAO USE LaTeX" not in t:
    # procura o prompt do sistema
    t = t.replace("PROIBIDO INVENTAR PREÇO", "NAO USE LaTeX, NUNCA USE $ , \\\\times , _ , ^ em formulas. Escreve formulas em texto simples WhatsApp: V1, P1, P1 x V1 = P2 x V2, V2 = V1 / 4. PROIBIDO INVENTAR PREÇO")
    print("PROMPT REFORCADO")
p.write_text(t)
