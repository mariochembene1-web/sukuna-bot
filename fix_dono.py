s = open('index.js', encoding='utf-8', errors='ignore').read()
# 1. Adiciona comando .meuid e .soudono antes do confirmar
if 'SOUDONO_SUKUNA' not in s:
    codigo = r"""
// ===== SOUDONO / MEUID - SOUDONO_SUKUNA =====
if (!isGroup && (textoLow === '.meuid' || textoLow === '.soudono')) {
  const fsD = require('fs');
  if (textoLow === '.meuid') {
    await sock.sendMessage(from, { text: `🆔 Teu ID: *${from}*\nManda isso ao bot para eu te registar.` }, { quoted: m });
    return;
  }
  let donos = [];
  try{ donos = JSON.parse(fsD.readFileSync('donos.json','utf8')); }catch{}
  if (!donos.includes(from)) donos.push(from);
  fsD.writeFileSync('donos.json', JSON.stringify(donos,null,2));
  await sock.sendMessage(from, { text: `👑 *REGISTADO COMO DONO!* ✅\n\nID: ${from}\nAgora podes usar .confirmar / .rejeitar` }, { quoted: m });
  return;
}
"""
    s = s.replace('// ===== CONFIRMAR / REJEITAR DONO', codigo + '\n// ===== CONFIRMAR / REJEITAR DONO', 1)

# 2. Troca a verificação do dono no confirmar para usar donos.json
s = s.replace(
  "  const dono = '258865697467';\n  if (!from.startsWith(dono))",
  "  const dono = '258865697467';\n  let donosList = [];\n  try{ donosList = JSON.parse(fsC.readFileSync('donos.json','utf8')); }catch{}\n  const isDono = from.startsWith(dono) || from.includes('865697467') || donosList.includes(from);\n  if (!isDono)"
)
open('index.js','w',encoding='utf-8').write(s)
print('FIX DONO OK')
