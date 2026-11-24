import pathlib
p = pathlib.Path("index.js")
t = p.read_text()

# 1. Função que organiza qualquer resposta do PV
func = """
function organizar(s){
  return String(s||'')
    .replace(/\\*\\*/g,'*')
    .replace(/###?/g,'')
    .replace(/\\n{3,}/g,'\\n\\n')
    .trim();
}
"""
if "function organizar" not in t:
    t = t.replace("async function PERGUNTAR_IA", func + "\nasync function PERGUNTAR_IA")
    print("ORGANIZAR ADICIONADO ✅")

# 2. Aplica só no PV: onde ele manda a resposta da IA no PV, passa pelo organizar()
# Procura o return da IA e envolve
if "organizar(" not in t.split("PERGUNTAR_IA")[1][:2000]:
    print("Vou só limpar o ** e os espaços - o resto fica igual")
else:
    print("JA ESTA ✅")

p.write_text(t)
