import csv
alunos=[]
for i in range(3):
    aluno={
        "RA":"",
        "nome":""
    }
    RA=input("RA:")
    nome=input("nome:")
    aluno["RA"]=RA
    aluno["nome"]=nome
    alunos.append(aluno)
with open("dados.csv", "w", newline="") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(alunos[0].keys())
    for aluno in alunos:
        dados = []
        dados.append(aluno["RA"])
        dados.append(aluno["nome"])
        escritor.writerow(dados)