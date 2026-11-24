import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
antes = t

t = t.replace("{ text: respPV }", "{ text: organizar(respPV) }")
t = t.replace("{text: respA}", "{text: organizar(respA)}")
t = t.replace("{text:respA}", "{text: organizar(respA)}")

# Garante que a função organizar existe e é forte - organiza de verdade
if "function organizar" in t:
    # substitui a função fraca por uma que organiza como eu faço
    import re
    nova = """function organizar(s){
  let x = String(s||'').replace(/\\*\\*/g,'*').replace(/###?/g,'').trim();
  // tira linhas vazias a mais e garante espaço entre blocos
  x = x.replace(/\\n{3,}/g,'\\n\\n');
  // se vier tudo colado numa linha gigante, parte nos pontos
  if(!x.includes('\\n') && x.length > 220){
    x = x.replace(/\\.\\s+/g, '.\\n\\n');
  }
  return x;
}"""
    t = re.sub(r"function organizar\(s\)\{.*?\n\}", nova, t, count=1, flags=re.DOTALL)
    print("ORGANIZAR MELHORADO ✅")

print("PV trocado:", "organizar(respPV)" in t)
print("AUDIO PV trocado:", "organizar(respA)" in t)
p.write_text(t)
