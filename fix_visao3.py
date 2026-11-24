import pathlib
p = pathlib.Path("index.js")
t = p.read_text()
t = t.replace("meta-llama/llama-4-maverick-17b-128e-instruct", "qwen/qwen3.8-27b")
t = t.replace("meta-llama/llama-4-scout-17b-16e-instruct", "qwen/qwen3.8-27b")
p.write_text(t)
print("TROCADO PARA QWEN VISAO")
