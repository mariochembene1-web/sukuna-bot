s = open('index.js', encoding='utf-8', errors='ignore').read()
if 'LIBERAR_PV_SUKUNA' in s:
    print('JA TEM')
else:
    codigo = r"""
// ===== LIBERAR ALUGUER PV - LIBERAR_PV_SUKUNA =====
if (!isGroup && (textoLow.startsWith('.liberar') || textoLow.startsWith('.negar'))) {
  const fsL = require('fs');
  let pendL = {};
  try{ pendL = JSON.parse(fsL.readFileSync('pendente_pv.json','utf8')); }catch{}
  const partesL = texto.trim().split(/\s+/);
  const acaoL = partesL[0].toLowerCase();
  const alvoL = (partesL[1]||'').replace(/[^0-9]/g,'');
  const diasManualL = partesL[2] ? parseInt(partesL[2]) : 0;
  const chaveL = Object.keys(pendL).find(k => k.includes(alvoL));
  if (!chaveL) { await sock.sendMessage(from, { text: '❌ Não achei pendente para '+alvoL }, { quoted: m }); return; }
  const dL = pendL[chaveL];
  if (acaoL === '.negar') {
    delete pendL[chaveL];
    fsL.writeFileSync('pendente_pv.json', JSON.stringify(pendL,null,2));
    await sock.sendMessage(chaveL, { text: '❌ *PAGAMENTO REJEITADO*\nFala com o dono.\n👑 *SUKUNA MESTRE*' });
    await sock.sendMessage(from, { text: '❌ Negado: '+alvoL }, { quoted: m });
    return;
  }
  const valorL = parseInt((dL.valor||'0').replace(/[^0-9]/g,'')) || 0;
  let diasL = diasManualL || ({10:1,15:1,25:2,35:3,100:7,550:30}[valorL] || 0);
  if (!diasL) { await sock.sendMessage(from, { text: '⚠️ Valor '+valorL+' MT não está na tabela!\nUsa: *.liberar '+alvoL+' <dias>*\nEx: *.liberar '+alvoL+' 2*' }, { quoted: m }); return; }
  const expiraL = new Date(Date.now() + diasL*24*60*60*1000);
  let alugL = {};
  try{ alugL = JSON.parse(fsL.readFileSync('alugados.json','utf8')); }catch{}
  alugL[dL.grupoId] = { cliente: chaveL, valor: valorL, dias: diasL, expira: expiraL.toISOString(), chave: dL.chave, ativo: true };
  fsL.writeFileSync('alugados.json', JSON.stringify(alugL,null,2));
  delete pendL[chaveL];
  fsL.writeFileSync('pendente_pv.json', JSON.stringify(pendL,null,2));
  await sock.sendMessage(chaveL, { text: `✅ *PAGAMENTO CONFIRMADO!* ✅\n\n💰 Valor: *${valorL} MT*\n📅 Dias: *${diasL} dias*\n🆔 Grupo: *${dL.grupoId}*\n📆 Expira: *${expiraL.toLocaleDateString('pt-PT')}*\n\n🔥 *SUKUNA ATIVADO!*\n👑 *SUKUNA MESTRE*` });
  await sock.sendMessage(from, { text: `✅ *LIBERADO!*\n\nCliente: ${alvoL}\nGrupo: ${dL.grupoId}\nValor: ${valorL} MT = ${diasL} dias\nExpira: ${expiraL.toLocaleDateString('pt-PT')}` }, { quoted: m });
  return;
}
"""
    # mete junto ao detector PV que já funciona, não nos comandos de grupo
    if 'DETECTOR_PV_SUKUNA' in s:
        s = s.replace('// ===== DETECTOR COMPROVATIVO PV', codigo + '\n// ===== DETECTOR COMPROVATIVO PV', 1)
    else:
        s = codigo + '\n' + s
    open('index.js','w',encoding='utf-8').write(s)
    print('LIBERAR INSTALADO')
