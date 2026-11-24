const { default: makeWASocket, useMultiFileAuthState, DisconnectReason, fetchLatestBaileysVersion } = require('@whiskeysockets/baileys');
const pino = require('pino');
const NUMERO = process.argv[2];
let jaPediu = false;
async function start(){
  const { version } = await fetchLatestBaileysVersion();
  const { state, saveCreds } = await useMultiFileAuthState('auth');
  const sock = makeWASocket({
    version,
    auth: state,
    logger: pino({ level: 'silent' }),
    printQRInTerminal: false,
    browser: ['Windows','Chrome','121.0.0.0'],
    mobile: false
  });
  sock.ev.on('creds.update', saveCreds);
  sock.ev.on('connection.update', async (u)=>{
    const { connection, lastDisconnect } = u;
    if(connection==='close'){
      const code = lastDisconnect?.error?.output?.statusCode;
      if(code !== DisconnectReason.loggedOut) start();
      else console.log('Deslogado, apaga auth');
    }
    if(connection==='open') console.log('✅ SUKUNA CONECTADO!');
    if(!state.creds.registered && NUMERO && !jaPediu){
      jaPediu = true;
      setTimeout(async ()=>{
        try{
          const code = await sock.requestPairingCode(NUMERO);
          console.log('\n👉 TEU CODIGO:', code);
        }catch(e){ console.log('Erro:', e.message); jaPediu = false; }
      }, 4000);
    }
  });
  sock.ev.on('messages.upsert', async ({messages})=>{
    const m = messages[0];
    if(!m.message || m.key.fromMe) return;
    const from = m.key.remoteJid;
    const text = m.message.conversation || m.message.extendedTextMessage?.text || '';
    if(!text.startsWith('.')) return;
    const cmd = text.slice(1).trim().split(' ')[0].toLowerCase();
    if(cmd==='ping') await sock.sendMessage(from, {text:'🏓 Pong! SUKUNA online'});
    if(cmd==='menu') await sock.sendMessage(from, {text:'👑 *SUKUNA MENU*\n\n.menu - ver menu\n.ping - testar bot'});
  });
}
start();
