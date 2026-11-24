s = open('index.js', encoding='utf-8', errors='ignore').read()
if 'DETECTOR_PV_SUKUNA' in s:
    print('JA TEM')
else:
    codigo = r"""
// ===== DETECTOR COMPROVATIVO PV - DETECTOR_PV_SUKUNA =====
if (!isGroup) {
  const fsPV = require('fs');
  let pendPV = {};
  try{ pendPV = JSON.parse(fsPV.readFileSync('pendente_pv.json','utf8')); }catch{}
  const txtPV = (texto || '') + ' ' + (m.message?.imageMessage?.caption || '') + ' ' + (m.message?.extendedTextMessage?.text || '');
  const ehComprovPV = /comprovativo|comprovante|PP\d{6}\.|M-PESA|MPESA|E-MOLA|EMOLA|transa|refer.ncia|recebeste|transfer/i.test(txtPV) || !!m.message?.imageMessage;
  const ehIdGrupo = /g\.us|whatsapp\.com\/|^\d{15,20}@g\.us$|^\d{15,20}$/.test((texto||'').trim()) || (texto||'').includes('chat.whatsapp.com/');

  if (pendPV[from] && pendPV[from].aguardandoId && ehIdGrupo) {
    const dados = pendPV[from];
    dados.grupoId = texto.trim();
    dados.status = 'aguardando_dono';
    pendPV[from] = dados;
    fsPV.writeFileSync('pendente_pv.json', JSON.stringify(pendPV,null,2));
    await sock.sendMessage(from, { text: `✅ *ID DO GRUPO ASSOCIADO!* ✅\n\n━━━━━━━━━━━━━━\n🏦 Tipo: *${dados.tipo}*\n🔑 Chave: *${dados.chave}*\n💰 Valor: *${dados.valor}*\n🆔 Grupo: *${dados.grupoId}*\n━━━━━━━━━━━━━━\n\n⏳ *Aguarde!* Já mandei para o dono confirmar se o valor entrou.\n\n👑 *SUKUNA MESTRE*` }, { quoted: m });
    const donoNum = '258865697467@s.whatsapp.net';
    await sock.sendMessage(donoNum, { text: `🔔 *NOVO PAGAMENTO NO PV - LIBERAR?* 🔔\n\n━━━━━━━━━━━━━━\n🏦 Tipo: *${dados.tipo}*\n🔑 Chave: *${dados.chave}*\n💰 Valor: *${dados.valor}*\n👤 Destinatário: *${dados.dest}*\n👤 Cliente: @${from.split('@')[0]}\n🆔 Grupo: *${dados.grupoId}*\n━━━━━━━━━━━━━━\n\n✅ Para liberar: *.confirmar ${from.split('@')[0]}*\n❌ Para rejeitar: *.rejeitar ${from.split('@')[0]}*\n\n👑 *SUKUNA MESTRE*` }, { quoted: m }).catch(()=>{});
    return;
  }

  if (ehComprovPV && !pendPV[from]?.aguardandoId) {
    let tipo = /e-mola|emola/i.test(txtPV) ? 'E-MOLA' : /m-pesa|mpesa/i.test(txtPV) ? 'M-PESA' : 'PAGAMENTO';
    let chave = (txtPV.match(/PP\d{6}\.\d{4}\.[a-zA-Z0-9]+/) || txtPV.match(/[A-Z0-9]{6,}\.[0-9]+/) || ['A VERIFICAR'])[0];
    let valorM = txtPV.match(/(\d+[.,]\d{2})\s*MT/i) || txtPV.match(/(\d+)\s*MT/i);
    let valor = valorM ? valorM[1] + ' MT' : 'A VERIFICAR';
    let destM = txtPV.match(/MARIO[^\n]{0,30}|CHEMBENE[^\n]{0,20}/i);
    let dest = destM ? destM[0].trim() : 'MARIO ANTONIO CHEMBENE';
    pendPV[from] = { tipo, chave, valor, dest, aguardandoId: true, hora: new Date().toISOString() };
    fsPV.writeFileSync('pendente_pv.json', JSON.stringify(pendPV,null,2));
    await sock.sendMessage(from, { text: `🧾 *COMPROVATIVO DETECTADO!* ✅\n\n━━━━━━━━━━━━━━\n🏦 *Tipo:* ${tipo}\n🔑 *Chave:* ${chave}\n💰 *Valor:* ${valor}\n👤 *Destinatário:* ${dest}\n━━━━━━━━━━━━━━\n\n🆔 *Agora manda o ID ou LINK do teu grupo:*\nEx: https://chat.whatsapp.com/xxxx\nOu o ID do grupo\n\n👑 *SUKUNA MESTRE*` }, { quoted: m });
    return;
  }
}
"""
    if '// ===== CONVERSA NO PV' in s:
        s = s.replace('// ===== CONVERSA NO PV', codigo + '\n// ===== CONVERSA NO PV', 1)
    else:
        s = codigo + '\n' + s
    open('index.js','w',encoding='utf-8').write(s)
    print('DETECTOR PV INSTALADO')
