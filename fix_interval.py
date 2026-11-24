import pathlib
p = pathlib.Path("index.js")
t = p.read_text()

# No privado - antes do return, limpa o intervalo
old_pv = "if(await GERAR_NATURAL(sock, from, m, txtPV)){ return; }"
new_pv = "if(await GERAR_NATURAL(sock, from, m, txtPV)){ try{ if(global._typingPV) clearInterval(global._typingPV); await sock.sendPresenceUpdate('paused', from); }catch(e){} return; }"
if old_pv in t:
    t = t.replace(old_pv, new_pv, 1)
    print("PV CORRIGIDO")

# No grupo - faz o mesmo se tiver intervalo de grupo
# procura o check do grupo
old_gp = "if(await GERAR_NATURAL(sock, from, m, perguntaFinal)){ return; }"
new_gp = "if(await GERAR_NATURAL(sock, from, m, perguntaFinal)){ try{ if(global._typingGrupo) clearInterval(global._typingGrupo); if(global._typing) clearInterval(global._typing); await sock.sendPresenceUpdate('paused', from); }catch(e){} return; }"
if old_gp in t:
    t = t.replace(old_gp, new_gp, 1)
    print("GRUPO CORRIGIDO")

p.write_text(t)
