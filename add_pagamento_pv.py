s = open('index.js', encoding='utf-8', errors='ignore').read()

if 'PAGAMENTO_SUKUNA_PV' in s:
    print('JA TEM - nao vou duplicar')
else:
    codigo = """
// ===== PAGAMENTO SUKUNA - SO NO PV - PAGAMENTO_SUKUNA_PV =====
if (!isGroup && ['.pagamento','!pagamento','pagamento','.pagar','pagar','.formas','formas','.como','como pago','como pago?'].includes(textoLow)) {
  await sock.sendMessage(from, { text: `💰 *FORMAS DE PAGAMENTO - SUKUNA MESTRE* 💰

━━━━━━━━━━━━━━
*FORMAS DE PAGAMENTO*

━━━━━━━━━━━━━━━━━━
💚 *M-PESA*
📱 Número: 849 683 738
👤 Titular: Mário António

━━━━━━━━━━━━━━━━━━
💛 *E-MOLA*
📱 Número: 865 697 467
👤 Titular: Mário António

━━━━━━━━━━━━━━━━━━
📞 *SUPORTE OFICIAL*
📱 Número: 865 697 467
⚠️ Somente chamadas pelo WhatsApp.

🕗 Horário de atendimento:
20:00 às 23:00 horas.

━━━━━━━━━━━━━━━━━━
⚠️ *IMPORTANTE*
Após efectuar o pagamento, envie o comprovativo para confirmação do aluguer.

👑 *MESTRE SUKUNA BOT*
🔥 Obrigado pela preferência!
━━━━━━━━━━━━━━

📸 *Depois manda o comprovativo!*
👑 *Dono:* Mário Oficialz` }, { quoted: m });
  return;
}
"""
    if '// ===== CONVERSA NO PV' in s:
        s = s.replace('// ===== CONVERSA NO PV', codigo + '\n// ===== CONVERSA NO PV', 1)
    else:
        s = codigo + '\n' + s
    open('index.js','w',encoding='utf-8').write(s)
    print('PAGAMENTO PV INSTALADO')
