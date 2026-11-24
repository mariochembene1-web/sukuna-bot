import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()

# 1. Desfaz o ternário torto
t = t.replace("GERAR_NATURAL(sock, from, m, texto) ? null : PERGUNTAR_IA(texto", "PERGUNTAR_IA(texto")
print("DESFEITO TERNO")

# 2. Mete o check correto antes da resposta no privado
# Procura a primeira vez que chama PERGUNTAR_IA para texto no privado
# Vamos inserir antes dela: if(await GERAR_NATURAL(...)) return;
if "if(await GERAR_NATURAL" not in t:
    # tenta achar o padrão: const resp = await PERGUNTAR_IA
    m = re.search(r"(const \w+ = await PERGUNTAR_IA\(texto[^\n]+\n)", t)
    if m:
        linha = m.group(1)
        novo = "    if(await GERAR_NATURAL(sock, from, m, texto)){ return; }\n" + linha
        t = t.replace(linha, novo, 1)
        print("CHECK PRIVADO OK")
    else:
        # fallback: procura qualquer PERGUNTAR_IA(texto
        m2 = re.search(r"(\s*)(await PERGUNTAR_IA\(texto)", t)
        if m2:
            t = t.replace(m2.group(0), m2.group(1) + "if(await GERAR_NATURAL(sock, from, m, texto)){ return; }\n" + m2.group(1) + "await PERGUNTAR_IA(texto", 1)
            print("CHECK PRIVADO OK 2")
        else:
            print("NAO ACHEI ONDE METER - manda print do trecho PERGUNTAR_IA")
else:
    print("JA TEM CHECK")

p.write_text(t)
