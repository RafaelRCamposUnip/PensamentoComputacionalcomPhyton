import json
dados={"nome": "Rafael", "email": "rafael.campos47@aluno.unip.br"}
with open("dados.json", "w") as arquivo:
    json.dump(dados, arquivo, indent=4)