const fs = require('fs');
let t = fs.readFileSync('index.js','utf8');

let alvo = "if(detectorComp[from]===true && msg.hasMedia){";
if(!t.includes(alvo)){
  console.log('NAO ACHEI CONDICAO - manda: grep -n "detectorComp\\[from\\]" index.js');
} else if(t.includes('DETECTOR_OU_COMP')){
  console.log('JA ESTA NOS DOIS');
} else {
  let novo = `// DETECTOR_OU_COMP - funciona com .detector on OU .comp on
  let detJson2={}; try{ detJson2=JSON.parse(require('fs').readFileSync('detector.json')); }catch{}
  let ligadoDetector = (detectorComp[from]===true || detJson2[from]===true || (typeof detectorGrupos!=='undefined' && detectorGrupos[from]===true));
  if(ligadoDetector && msg.hasMedia){`;
  t = t.replace(alvo, novo);
  console.log('AGORA FUNCIONA NOS DOIS');
}
fs.writeFileSync('index.js', t);
