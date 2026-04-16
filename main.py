nomes=["Tamires", "Simone", "Mel"]
for nome in nomes:
   print(f"Olá, {nome}!")

amigos={"Mário":19, "Bruno":19}
for nome, idade in amigos.items():
    print(f"{nome} tem {idade} anos")

num=int(input("Digite um número:"))
for i in range(1,11):#1 a 10
    print(f"{num} X {i}={num*i}")