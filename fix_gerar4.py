import pathlib
p = pathlib.Path("index.js")
lines = p.read_text().splitlines(True)

# Mete de baixo para cima para não estragar os números
# Grupo - linha 1152 (indice 1151)
# Privado - linha 983 (indice 982)
# Verifica se já não tem
for idx, var in [(1151, "perguntaFinal"), (982, "txtPV")]:
    if idx < len(lines):
        linha = lines[idx]
        print(f"LINHA {idx+1}: {linha.strip()[:80]}")
        # verifica se a linha anterior já tem o check
        if idx>0 and "GERAR_NATURAL" in lines[idx-1]:
            print("JA TEM CHECK")
            continue
        indent = linha[:len(linha)-len(linha.lstrip())]
        check = f"{indent}if(await GERAR_NATURAL(sock, from, m, {var})){{ return; }}\n"
        lines.insert(idx, check)
        print(f"CHECK METIDO PARA {var}")

p.write_text(''.join(lines))
print("FEITO")
