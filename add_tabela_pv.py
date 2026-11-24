s = open('index.js', encoding='utf-8', errors='ignore').read()

if 'TABELA_SUKUNA_PV' in s:
    print('JA TEM - nao vou duplicar')
else:
    codigo = """
// ===== TABELA SUKUNA - SO NO PV - TABELA_SUKUNA_PV =====
if (!isGroup && ['.tabela','!tabela','tabela','.planos','!planos','planos','.precos','!precos','precos','.preco','preço','.preço'].includes(textoLow)) {
  await sock.sendMessage(from, { text: `━━━━━━━━━━━━━━━━━━
🤖 *PLANOS DISPONÍVEIS*
━━━━━━━━━━━━━━━━━━

🆓 *TESTE* — 2 DIAS GRÁTIS
🥉 *1 DIA* — 10 MT
🥈 *2 DIAS* — 25 MT
🥉 *3 DIAS* — 35 MT
🏆 *7 DIAS* — 100 MT
👑 *30 DIAS* — 550 MT

━━━━━━━━━━━━━━━━━━
⚡ *BENEFÍCIOS DO SUKUNA*
✅ Gestão de grupos
✅ Proteção e segurança
✅ Administração automática
✅ Ferramentas inteligentes

━━━━━━━━━━━━━━━━━━
📩 *QUER ALUGAR O SUKUNA?*
Entre em contacto com o administrador!

🔥 *MESTRE SUKUNA BOT*
👑 Qualidade e poder ao serviço do teu grupo!` }, { quoted: m });
  return;
}
"""
    if '// ===== CONVERSA NO PV' in s:
        s = s.replace('// ===== CONVERSA NO PV', codigo + '\n// ===== CONVERSA NO PV', 1)
    else:
        s = codigo + '\n' + s
    open('index.js','w',encoding='utf-8').write(s)
    print('TABELA PV INSTALADA')
