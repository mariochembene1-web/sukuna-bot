const {
  makeWASocket,
  useMultiFileAuthState,
  fetchLatestBaileysVersion,
  Browsers
} = require('@whiskeysockets/baileys');

const pino = require('pino');

const numero = '258870140424';
const pasta = 'auth_numero_870140424_NOVA';

let codigoPedido = false;
let reconectando = false;

async function iniciar() {
  console.log('===== SUKUNA - EMPARELHAMENTO =====');

  const { version } = await fetchLatestBaileysVersion();
  const { state, saveCreds } = await useMultiFileAuthState(pasta);

  const sock = makeWASocket({
    version,
    auth: state,
    logger: pino({ level: 'warn' }),
    printQRInTerminal: false,
    browser: Browsers.ubuntu('Chrome'),
    keepAliveIntervalMs: 30000,
    connectTimeoutMs: 60000,
    defaultQueryTimeoutMs: undefined
  });

  sock.ev.on('creds.update', saveCreds);

  sock.ev.on('connection.update', ({ connection, lastDisconnect }) => {
    if (connection) console.log('ESTADO:', connection);

    if (connection === 'open') {
      console.log('✅ SUKUNA LIGADO AO WHATSAPP!');
      reconectando = false;
    }

    if (connection === 'close') {
      const erro = lastDisconnect?.error;
      const status = erro?.output?.statusCode;

      console.log('LIGAÇÃO FECHADA:', status, erro?.message);

      if (status === 515 && !reconectando) {
        reconectando = true;
        console.log('REINICIANDO LIGAÇÃO COM A MESMA SESSÃO...');
        setTimeout(() => {
          reconectando = false;
          iniciar().catch(console.error);
        }, 2500);
      }
    }
  });

  if (!state.creds.registered && !codigoPedido) {
    await new Promise(resolve => setTimeout(resolve, 5000));

    try {
      const codigo = await sock.requestPairingCode(numero);
      codigoPedido = true;
      console.log('\nCÓDIGO DE EMPARELHAMENTO:', codigo);
      console.log('Introduz no WhatsApp do número +258 870 140 424.');
      console.log('Não feches este processo.');
    } catch (erro) {
      console.error('ERRO AO PEDIR CÓDIGO:', erro.message);
    }
  } else if (state.creds.registered) {
    console.log('Sessão já registada. A tentar ligar sem novo código.');
  }
}

iniciar().catch(console.error);
