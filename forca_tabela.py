import pathlib, re
p = pathlib.Path("index.js")
t = p.read_text()
nova = """━━━━━━━━━━━━━━━━━━
🤖 PLANOS DISPONÍVEIS
━━━━━━━━━━━━━━━━━━

🆓 TESTE — 2 DIAS GRÁTIS
🥉 1 DIA — 10 MT
🥈 2 DIAS — 25 MT
🥉 3 DIAS — 35 MT
🏆 7 DIAS — 100 MT
👑 30 DIAS — 550 MT

━━━━━━━━━━━━━━━━━━
⚡ BENEFÍCIOS DO SUKUNA
✅ Gestão de grupos
✅ Proteção e segurança
✅ Administração automática
✅ Ferramentas inteligentes

━━━━━━━━━━━━━━━━━━
📩 QUER ALUGAR O SUKUNA?
Entre em contacto com o administrador!

🔥 MESTRE SUKUNA BOT
👑 Qualidade e poder ao serviço do teu grupo!"""
# força tabela nova sempre, ignora tabela velha guardada
t = re.sub(r"let tb=.*?;", "let tb=`" + nova + "`;", t, count=1)
p.write_text(t)
print("AGORA E SEMPRE ESSA")
