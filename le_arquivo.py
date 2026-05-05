import json
with open("dados.json", "r") as arquivo:
    dados_carregados = json.load(arquivo)
print(dados_carregados)
