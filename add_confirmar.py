s = open('index.js', encoding='utf-8', errors='ignore').read()
if 'CONFIRMAR_PV_SUKUNA' in s:
    print('JA TEM')
else:
    codigo = r"""
// ===== CONFIRMAR / REJEITAR DONO - CONFIRMAR_PV_SUKUNA =====
if (!isGroup && (textoLow.startsWith('.confirmar') || textoLow.startsWith('.rejeitar'))) {
  const fsC = require('fs');
  const dono = '258865697467';
  if (!from.startsWith(dono)) { await sock.sendMessage(from, { text: '❌ Só o dono pode usar isso.' }, { quoted: m }); return; }
  let pendC = {};
  try{ pendC = JSON.parse(fsC.readFileSync('pendente_pv.json','utf8')); }catch{}
  const partes = texto.trim().split(/\s+/);
  const acao = partes[0].toLowerCase();
  const alvoNum = (partes[1]||'').replace(/[^0-9]/g,'');
  const diasManual = partes[2] ? parseInt(partes[2]) : 0;
  const chaveCliente = Object.keys(pendC).find(k => k.includes(alvoNum));
  if (!chaveCliente) { await sock.sendMessage(from, { text: '❌ Não achei pendente para '+alvoNum }, { quoted: m }); return; }
  const d = pendC[chaveCliente];
  if (acao === '.rejeitar') {
    delete pendC[chaveCliente];
    fsC.writeFileSync('pendente_pv.json', JSON.stringify(pendC,null,2));
    await sock.sendMessage(chaveCliente, { text: `❌ *PAGAMENTO REJEITADO*\n\nFala com o dono para resolver.\n👑 *SUKUNA MESTRE*` });
    await sock.sendMessage(from, { text: `❌ Rejeitado: ${alvoNum}` }, { quoted: m });
    return;
  }
  const valorNum = parseInt((d.valor||'0').replace(/[^0-9]/g,'')) || 0;
  let dias = diasManual || ({10:1,15:1,25:2,35:3,100:7,550:30}[valorNum] || 0);
  if (!dias) { await sock.sendMessage(from, { text: `⚠️ Valor ${valorNum} MT não está na tabela!\nUsa: *.confirmar ${alvoNum} <dias>*\nEx: *.confirmar ${alvoNum} 2*` }, { quoted: m }); return; }
  const expira = new Date(Date.now() + dias*24*60*60*1000);
  let alug = {};
  try{ alug = JSON.parse(fsC.readFileSync('alugados.json','utf8')); }catch{}
  let grupoJid = d.grupoId || '';
  alug[grupoJid] = { cliente: chaveCliente, valor: valorNum, dias, expira: expira.toISOString(), chave: d.chave, ativo: true };
  fsC.writeFileSync('alugados.json', JSON.stringify(alug,null,2));
  delete pendC[chaveCliente];
  fsC.writeFileSync('pendente_pv.json', JSON.stringify(pendC,null,2));
  await sock.sendMessage(chaveCliente, { text: `✅ *PAGAMENTO CONFIRMADO!* ✅\n\n━━━━━━━━━━━━━━\n💰 Valor: *${valorNum} MT*\n📅 Dias: *${dias} dias*\n🆔 Grupo: *${d.grupoId}*\n📆 Expira: *${expira.toLocaleDateString('pt-PT')}*\n━━━━━━━━━━━━━━\n\n🔥 *SUKUNA ATIVADO NO TEU GRUPO!*\n👑 *SUKUNA MESTRE*` });
  await sock.sendMessage(from, { text: `✅ *LIBERADO!*\n\nCliente: ${alvoNum}\nGrupo: ${d.grupoId}\nValor: ${valorNum} MT = ${dias} dias\nExpira: ${expira.toLocaleDateString('pt-PT')}\n\nSe o bot já está no grupo, ele já está ativo.` }, { quoted: m });
  if (grupoJid.endsWith('@g.us')) {
    await sock.sendMessage(grupoJid, { text: `🔥 *SUKUNA ATIVADO!* 🔥\n\n✅ Pagamento confirmado\n📅 *${dias} dias* de uso\n📆 Expira: *${expira.toLocaleDateString('pt-PT')}*\n\n👑 *SUKUNA MESTRE*` }).catch(()=>{});
  }
  return;
}
"""
    if '// ===== CONVERSA NO PV' in s:
        s = s.replace('// ===== CONVERSA NO PV', codigo + '\n// ===== CONVERSA NO PV', 1)
    else:
        s = codigo + '\n' + s
    open('index.js','w',encoding='utf-8').write(s)
    print('CONFIRMAR INSTALADO')
