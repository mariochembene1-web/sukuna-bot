const fs = require('fs');
let db = {};
try { db = JSON.parse(fs.readFileSync('./ativados.json')); } catch(e){ db = {}; }
function salvar(){ fs.writeFileSync('./ativados.json', JSON.stringify(db, null, 2)); }
function parseTempo(txt){
  if(!txt) return null;
  txt = txt.toLowerCase().trim();
  if(txt.endsWith('h')) return parseInt(txt) * 60 * 60 * 1000;
  if(txt.endsWith('d')) return parseInt(txt) * 24 * 60 * 60 * 1000;
  if(txt.endsWith('m')) return parseInt(txt) * 60 * 1000;
  return null;
}
function estaAtivo(groupId){
  if(!db[groupId]) return false;
  if(Date.now() > db[groupId]){ delete db[groupId]; salvar(); return false; }
  return true;
}
function tempoRestante(groupId){
  if(!db[groupId]) return 'Nao ativado';
  let diff = db[groupId] - Date.now();
  if(diff <= 0) return 'Expirado';
  let h = Math.floor(diff / 3600000);
  let m = Math.floor((diff % 3600000) / 60000);
  let d = Math.floor(h / 24);
  if(d > 0) return d + 'd ' + (h % 24) + 'h ' + m + 'm';
  return h + 'h ' + m + 'm';
}
module.exports = { db, salvar, parseTempo, estaAtivo, tempoRestante };
