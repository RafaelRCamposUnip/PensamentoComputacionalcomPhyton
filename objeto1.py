object={
    "nome":"Mateus",
    "sobrenome":"Goulart"
}
nome_completo=object["nome"]+" "+object["sobrenome"]
print(nome_completo)

object["nome"]=input("Informe seu nome:")
object["sobrenome"]=input("Informe seu sobrenome:")
print(object["sobrenome"]+", "+object["nome"])