import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
n = 0

# FIX 1 - FIX52: limpa espaços antes de testar
old1 = "let _mNumOnly = _txtNum.match(/^(84|85|86|87)\\d{7}$/);"
new1 = "let _mNumOnly = _txtNum.replace(/[\\s\\-]/g,'').match(/^(84|85|86|87)\\d{7}$/);"
if old1 in t:
    t = t.replace(old1, new1)
    n += 1
    print("FIX52 OK")
else:
    print("FIX52 NAO ACHEI")

# FIX 2 - NUMERO SO: aceita 84 891 5534 / 84-891-5534 / +258 84 891 5534
old2 = "if (/^\\s*(?:258)?\\s?(8[4567]\\d{7})\\s*$/.test(texto)) {"
if old2 in t:
    t = t.replace(old2, "if (/^\\s*(?:\\+?258)?[\\s\\-]*((?:8[4567])[\\s\\-\\d]{7,13})\\s*$/.test(texto) && texto.replace(/\\D/g,'').replace(/^258/,'').length===9) {")
    n += 1
    print("NUMERO SO REGEX OK")
else:
    print("NUMERO SO REGEX NAO ACHEI - procura manual")
    # tenta variante sem escape
    import re
    print([l.strip()[:150] for l in t.splitlines() if "NUMERO SO DA MESMA" in l or "8[4567]" in l and "test(texto)" in l][:3])

# FIX 2b - dentro desse bloco, o num tem que vir limpo sem espaços
old3 = "let num = texto.match(/(8[4567]\\d{7})/)[1];"
new3 = "let num = texto.replace(/\\D/g,'').replace(/^258/,'').slice(-9);"
if old3 in t:
    t = t.replace(old3, new3)
    n += 1
    print("NUM LIMPO OK")

p.write_text(t)
print(f"TOTAL: {n} fixes")
