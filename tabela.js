const fs = require('fs');
function handleTabela(cmd, args, reply) {
  let tabela = {};
  if (fs.existsSync('./tabela.json')) tabela = JSON.parse(fs.readFileSync('./tabela.json'));
  if (cmd !== '.tabela') return false;
  let sub = args[0];
  let resto = args.slice(1).join(' ');
  if (sub === 'add') {
    let pares = resto.split(',');
    for (let p of pares) {
      let partes = p.trim().split('=');
      if (partes[0] && partes[1]) tabela[partes[0].trim()] = partes[1].trim().toUpperCase();
    }
    fs.writeFileSync('./tabela.json', JSON.stringify(tabela));
    reply('✅ Tabela atualizada! Manda .tabela ver para ver');
    return true;
  }
  if (sub === 'ver') {
    let txt = '📋 *TABELA SUKUNA* 👹\n\n';
    for (let preco in tabela) txt += `• ${preco} MT - ${tabela[preco]}\n`;
    reply(txt);
    return true;
  }
  if (sub === 'del') {
    delete tabela[resto.trim()];
    fs.writeFileSync('./tabela.json', JSON.stringify(tabela));
    reply('🗑️ Apagado!');
    return true;
  }
  if (sub === 'limpar') {
    fs.writeFileSync('./tabela.json', JSON.stringify({}));
    reply('🧹 Tabela limpa!');
    return true;
  }
  return false;
}
module.exports = { handleTabela };
