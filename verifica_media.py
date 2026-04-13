#Verifica_media.py
nome=input("Informe o nome do aluno:")
np1=float(input("Informe a nota da np1:"))
np2=float(input("Informe a nota da np2:"))
pim=float(input("Informe a nota do PIM:"))
media=(((np1+np1)/2)*0.8)+(pim*0.2)
if media>=7.0:
    print(f"{nome} foi aprovado")
elif media>=5.0:
    print(f"{nome} está de recuperação")
else:
    print(f"{nome} foi reprovado")
print(f"A média final de {nome} é de {media}")