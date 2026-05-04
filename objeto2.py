import json
curso={
    "codigo":"",
    "nome":"",
    "alunos":[]
}
aluno={
    "cpf":"",
    "nome":"",
    "dataNasc":"",
    "telefone":"",
    "email":""
}
aluno2={
    "cpf":"",
    "nome":"",
    "dataNasc":"",
    "telefone":"",
    "email":""
}
curso["codigo"]=input("Informe o código do curso:")
curso["nome"]=input("Informe o nome do curso:")

aluno["cpf"]=input("Informe o CPF do aluno:")
aluno["nome"]=input("Informe o nome do aluno:")
aluno["dataNasc"]=input("Informe a data de nascimento do aluno:")
aluno["telefone"]=input("Informe o telefone do aluno:")
aluno["email"]=input("Informe o email do aluno:")

aluno2["cpf"]=input("Informe o CPF do aluno:")
aluno2["nome"]=input("Informe o nome do aluno:")
aluno2["dataNasc"]=input("Informe a data de nascimento do aluno:")
aluno2["telefone"]=input("Informe o telefone do aluno:")
aluno2["email"]=input("Informe o email do aluno:")
curso["alunos"].append(aluno)
curso["alunos"].append(aluno2)
print("------------")
print(f"Curso:{curso["codigo"]}-{curso["nome"]}")
for obj in curso["alunos"]:
    print(f"{obj["cpf"]}-{obj["nome"]}")
with open("curso.json","w") as arquivo:
    json.dump(curso, arquivo, indent=4)
