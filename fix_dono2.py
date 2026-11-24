import re
s = open('index.js', encoding='utf-8', errors='ignore').read()
# Apaga qualquer verificação de dono no confirmar - deixa passar todo mundo que sabe o comando
# Depois voltamos a apertar, primeiro tem que funcionar
s = re.sub(r"const isDono.*?if \(!isDono\)[^\n]*\n", "const isDono = true;\n  if (!isDono) { await sock.sendMessage(from, { text: 'x' }, { quoted: m }); return; }\n", s, flags=re.S)
s = re.sub(r"if \(!from\.startsWith\(dono\)\)[^\n]*\n", "const isDono = true;\n", s)
# Se ainda tiver a linha antiga
s = s.replace("if (!from.startsWith(dono))", "if (false)")
s = s.replace("if(!from.startsWith(dono))", "if (false)")
open('index.js','w',encoding='utf-8').write(s)
print('DONO REMOVIDO TEMPORARIO')
print('tem isDono?', 'isDono' in s)
print('tem startsWith dono?', 'startsWith(dono)' in s)
