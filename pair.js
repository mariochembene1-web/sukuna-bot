const { makeWASocket, useMultiFileAuthState, fetchLatestBaileysVersion } = require('@whiskeysockets/baileys');
const readline = require('readline');
async function start(){
  const { version } = await fetchLatestBaileysVersion();
  const { state, saveCreds } = await useMultiFileAuthState('auth');
  const sock = makeWASocket({ version, auth: state, printQRInTerminal: false, browser: ['SUKUNA','Chrome','Windows'] });
  sock.ev.on('creds.update', saveCreds);
  sock.ev.on('connection.update', (u)=>{
    if(u.connection==='open') console.log('✅ CONECTADO COM NÚMERO NOVO!');
  });
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  rl.question('Mete o número novo com código do país (ex: 258870140424): ', async (num)=>{
    rl.close();
    const code = await sock.requestPairingCode(num.trim());
    console.log('\n🔑 TEU CÓDIGO É: ' + code);
    console.log('Vai no WhatsApp desse número: Configurações > Aparelhos conectados > Conectar um aparelho > Conectar com número de telefone e cola o código');
  });
}
start();
