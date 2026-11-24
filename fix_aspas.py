import pathlib
p = pathlib.Path("index.js")
lines = p.read_text().splitlines(True)
for i, l in enumerate(lines):
    if "falhou a gerar a foto" in l and "Se continuar" in l:
        indent = l[:len(l)-len(l.lstrip())]
        lines[i] = indent + "}catch(e){ await sock.sendMessage(from, {text:'Eish, falhou a gerar a foto, tenta de novo.'}, {quoted:m}); }\n"
        print(f"CORRIGIDO LINHA {i+1}")
p.write_text(''.join(lines))
