#Concatenar
S1="Renan"
S2=" Rodrigues"
Resultado=S1+S2
print(Resultado)

#Repetição
S3="A"
print(S3*10)

#Comprimento(Length)
S4="Python"
print(len(S4))

#Transformação
S5="PyThOn"
print(S5.lower())
print(S5.upper())
print(S5.title())
print(S5.capitalize())

#Substituição
S6="Hello World"
print(S6.replace("World", "Miguel"))

#Remover espaços
S7=" Hello "
print(S7.strip())
print(S7.lstrip())
print(S7.rstrip())

#Quebra(split) e Junção(join)
#1
S8="apple, banana, orange"
lista=S8.split(",")
print(lista)
print(lista[1])
#2
lista=["apple","banana","orange"]
S8=",".join(lista)
print(S8)