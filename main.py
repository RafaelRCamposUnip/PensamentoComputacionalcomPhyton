#def saudacao():
    #print("Olá, bem-vindo!")
#print = saudacao()

prossiga = "S"
media = 0.0
soma =0.0
contador = 0
while prossiga == "S":
    num = float(input("Informe um número: "))
    contador += 1
    soma += num
    prossiga = input("DESEJA PROSSEGUIR? S/N: ").upper()
    if prossiga == "N":
        print("Saindo...")
media = soma/contador
print("Contagem de números: ",contador)
print("Soma: ",soma)
print("Média: ",media)