import csv
producao = []
estoque = []
residuos = []

def registrar_producao():
    while True:
        data = input("Informe a data (dd/mm/aaaa): ")
        produto = input("Informe o nome do produto: ")

        if data=="" or produto=="":
            print("Preencha todos os campos!")
            continue

        while True:
            try:
                quantidade = int(input("Informe a quantidade produzida: "))
                break
            except ValueError:
                print("Digite apenas números!")

        registro = {
            "data": data,
            "produto": produto,
            "quantidade": quantidade
        }

        producao.append(registro)

        print("Produção registrada com sucesso!")

        while True:
            continuar = input("Deseja registrar outra produção? (s/n): ").lower()
            if continuar == "s":
                break

            elif continuar == "n":
                print("Voltando ao menu...")
                return

            else:
                print("Digite apenas 's' ou 'n'.")

def registrar_estoque():
    while True:
        material = input("Informe o material: ")

        if material=="":
            print("Nome inválido!")
            continue

        while True:
            try:
                quantidade = int(input("Informe a quantidade: "))
                break
            except ValueError:
                print("Digite apenas números!")

        for item in estoque:
            if item["material"].lower() == material.lower():
                item["quantidade"] += quantidade
                print("Estoque atualizado!")
                return

        estoque.append({
            "material": material,
            "quantidade": quantidade
        })

        print("Material adicionado ao estoque!")

        continuar = input("Deseja registrar outro material ao estoque? (s/n): ").lower()
        if continuar == "s":
            break

        elif continuar == "n":
            print("Voltando ao menu...")
            return

        else:
            print("Digite apenas 's' ou 'n'.")

def registrar_residuo():
    while True:
        tipo = input("Informe o tipo de resíduo: ")
        if tipo == "":
            print("Nome inválido!")
            continue

        while True:
            try:
                quantidade = int(input("Informe a quantidade descartada: "))
                break
            except ValueError:
                print("Digite apenas números!")

        for item in residuos:
            if item["tipo"].lower() == tipo.lower():
                item["quantidade"] += quantidade
                print("Resíduo atualizado!")
                return

        residuos.append({
            "tipo": tipo,
            "quantidade": quantidade
        })

        print("Resíduo registrado com sucesso!")

        while True:
            continuar = input("Deseja registrar outro resíduo? (s/n): ").lower()

            if continuar == "s":
                break

            elif continuar == "n":
                print("Voltando ao menu...")
                return

            else:
                print("Digite apenas 's' ou 'n'.")

def listar_producao():
    if len(producao) == 0:
        print("Sem registro!")
        return

    for item in producao:
        print(f"{item['data']} - {item['produto']} - {item['quantidade']}")

def listar_estoque():
    if len(estoque) == 0:
        print("Sem registro!")
        return

    for item in estoque:
        print(f"{item['material']} - {item['quantidade']}")

def listar_residuos():
    if len(residuos) == 0:
        print("Sem registro!")
        return 

    for item in residuos:
        print(f"{item['tipo']} - {item['quantidade']}")

def relatorio_producao():
    if len(producao) == 0:
        print("Não há dados registrados!")
        return

    total = 0

    for item in producao:
        total += item["quantidade"]

    media = total/len(producao)

    produtos = {}

    for item in producao:
        nome = item["produto"]

        if nome in produtos:
            produtos[nome] += item["quantidade"]
        else:
            produtos[nome] = item["quantidade"]

    mais_produzido = max(produtos, key=produtos.get)

    print("\n --- RELATÓRIO DE PRODUÇÃO ---")
    print("Total produzido:", total)
    print("Média por registro:", round(media,2))
    print("Produto mais produzido:", mais_produzido)
    print("Quantidade de registros:", len(producao))

def relatorio_ambiental():
     if len(residuos) == 0:
         print("Não há dados registrados!")
         return

     total = 0

     for item in residuos:
         total += item["quantidade"]

     media = total/len(residuos)

     tipos={}

     for item in residuos:
         nome = item["tipo"]

         if nome in tipos:
             tipos[nome] += item["quantidade"]
         else:
             tipos[nome] = item["quantidade"]

     mais_gerado = max(tipos, key=tipos.get)

     print("\n--- RELATÓRIO AMBIENTAL ---")
     print("Total de resíduos:", total)
     print("Média de descarte:", round(media,2))
     print("Resíduo mais gerado:", mais_gerado)
     print("Quantidade de registros:", len(residuos))

def exportar_producao_csv():
    if len(producao) == 0:
        print("Não há dados de produção para exportar!")
        return

    with open("producao.csv", "w", newline="", encoding="utf-8") as arquivos:
        escritor = csv.writer(arquivos)
        escritor.writerow(["Data", "Produto", "Quantidade"])
        for item in producao:
            escritor.writerow([
                item["data"],
                item["produto"],
                item["quantidade"]
            ])
    print("Arquivo 'producao.csv' gerado com sucesso!")

def exportar_estoque_csv():
    if len(estoque) == 0:
        print("Não há dados do estoque para exportar!")
        return

    with open("estoque.csv", "w", newline="", encoding="utf-8") as arquivos:
        escritor = csv.writer(arquivos)
        escritor.writerow(["Material", "Quantidade"])
        for item in estoque:
            escritor.writerow([
                item["material"],
                item["quantidade"]
            ])
    print("Arquivo 'estoque.csv' gerado com sucesso!")

def exportar_residuos_csv():
    if len(residuos) == 0:
        print("Não há dados de resíduos para exportar!")
        return

    with open("residuos.csv", "w", newline="", encoding="utf-8") as arquivos:
        escritor = csv.writer(arquivos)
        escritor.writerow(["Tipo", "Quantidade"])
        for item in residuos:
            escritor.writerow([
                item["tipo"],
                item["quantidade"]
            ])
    print("Arquivo 'residuos.csv' gerado com sucesso!")

while True:
    print("\n--- SISTEMA ---")
    print("1- Registrar produção")
    print("2- Registrar estoque")
    print("3- Registrar resíduos")
    print("4- Ver produção")
    print("5- Ver estoque")
    print("6- Ver resíduos")
    print("7- Relatório de produção")
    print("8- Relatório ambiental")
    print("9- Exportar produção (CSV)")
    print("10- Exportar estoque (CSV)")
    print("11- Exportar resíduos (CSV)")
    print("0- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        registrar_producao()

    elif opcao == "2":
        registrar_estoque()

    elif opcao == "3":
        registrar_residuo()

    elif opcao == "4":
        listar_producao()

    elif opcao == "5":
        listar_estoque()

    elif opcao == "6":
        listar_residuos()

    elif opcao == "7":
        relatorio_producao()

    elif opcao == "8":
        relatorio_ambiental()

    elif opcao == "9":
        exportar_producao_csv()

    elif opcao == "10":
        exportar_estoque_csv()

    elif opcao == "11":
        exportar_residuos_csv()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
