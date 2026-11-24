import pathlib
p = pathlib.Path("index.js")
t = p.read_text()

tabela = """    if (cmd === '.tabela' || cmd === 'tabela' || (texto||'').trim().toLowerCase() === 'tabela') {
      let _isGrupo = String(from||'').endsWith('@g.us');
      if (_isGrupo) { await reply('📋 *Tabela só no PV, Mestre!*\\n\\nFala comigo no privado e escreve *tabela* 👑'); return; }
      let _tab = `INTERNET DA VODACOM 📶🔥
🎁 BÔNUS DE MB – MAIS INTERNET PELO MESMO PREÇO!

📅 PACOTES DIÁRIOS (24H)

🚀 512MB ➜ 10 MT
✈️ 530MB ➜ 11 MT
✈️ 550MB ➜ 12 MT
✈️ 600MB ➜ 13 MT
✈️ 660MB ➜ 14 MT
✈️ 700MB ➜ 15 MT
🚀 730MB ➜ 16 MT
✈️ 830MB ➜ 17 MT
✈️ 870MB ➜ 18 MT
✈️ 900MB ➜ 19 MT
✈️ 1024MB ➜ 20 MT
✈️ 1030MB ➜ 21 MT
✈️ 1050MB ➜ 22 MT
✈️ 1080MB ➜ 23 MT
✈️ 1130MB ➜ 24 MT
🚀 1200MB ➜ 25 MT
✈️ 1300MB ➜ 27 MT
🚀 1500MB ➜ 30 MT
🚀 1530MB ➜ 31 MT
🚀 1550MB ➜ 32 MT
🚀 1600MB ➜ 33 MT
🚀 1650MB ➜ 34 MT
🚀 1700MB ➜ 35 MT
🚀 2048MB ➜ 40 MT
🚀 2060MB ➜ 41 MT
🚀 2080MB ➜ 42 MT
🚀 2100MB ➜ 43 MT
✈️ 2150MB ➜ 44 MT
🚀 2180MB ➜ 45 MT
🚀 2500MB ➜ 50 MT
🚀 4000MB ➜ 75 MT
🚀 5120MB ➜ 100 MT
🚀 5500MB ➜ 125 MT
✈️ 10240MB ➜ 230 MT
🚀 10500MB ➜ 250 MT
🚀 21000MB ➜ 480 MT

👑 *SUKUNA MESTRE*
👤 *Dono:* Mário Oficialz
📲 *Pede no PV: escolhe MB + envia comprovativo*`;
      await reply(_tab);
      return;
    }
"""

if "cmd === '.tabela'" in t:
    print("JA TEM TABELA")
else:
    # mete antes do .pendentes
    alvo = "if (cmd === '.pendentes')"
    if alvo in t:
        t = t.replace(alvo, tabela + alvo, 1)
        p.write_text(t)
        print("TABELA POSTA - PV ONLY")
    else:
        print("NAO ACHEI .pendentes - manda grep")
