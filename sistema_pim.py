import csv
import os
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

        exportar_producao_csv()

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

                exportar_estoque_csv()

                print("Estoque atualizado!")
                return

        estoque.append({
            "material": material,
            "quantidade": quantidade
        })

        exportar_estoque_csv()

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

                exportar_residuos_csv()

                print("Resíduo atualizado!")
                return

        residuos.append({
            "tipo": tipo,
            "quantidade": quantidade
        })

        exportar_residuos_csv()

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

def carregar_producao_csv():
    if os.path.exists("producao.csv"):

        with open("producao.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                producao.append({
                    "data": linha["Data"],
                    "produto": linha["Produto"],
                    "quantidade": int(linha["Quantidade"])
                })

def carregar_estoque_csv():
    if os.path.exists("estoque.csv"):

        with open("estoque.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                producao.append({
                    "material": linha["Material"],
                    "quantidade": int(linha["Quantidade"])
                })

def carregar_residuos_csv():
    if os.path.exists("residuos.csv"):

        with open("residuos.csv", "r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                producao.append({
                    "tipo": linha["Tipo"],
                    "quantidade": int(linha["Quantidade"])
                })

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

    with open("producao.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
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

    with open("estoque.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
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

    with open("residuos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["Tipo", "Quantidade"])
        for item in residuos:
            escritor.writerow([
                item["tipo"],
                item["quantidade"]
            ])
    print("Arquivo 'residuos.csv' gerado com sucesso!")

def buscar_producao():
    if len(producao) == 0:
        print("Nenhum registro encontrado!")
        return

    busca = input("Digite o nome do produto: ").lower()

    encontrado = False

    for item in producao:
        if item["produto"].lower() == busca:
            print(f"{item['data']} - {item['produto']} - {item['quantidade']}")
            encontrado = True

        if not encontrado:
            print("Produto não encontrado!")

def buscar_estoque():
    if len(estoque) == 0:
        print("Nenhum registro encontrado!")
        return

    busca = input("Digite o nome do material: ").lower()

    encontrado = False

    for item in estoque:
        if item["material"].lower() == busca:
            print(f"{item['material']} - {item['quantidade']}")
            encontrado = True

        if not encontrado:
            print("Material não encontrado!")

def buscar_residuos():
    if len(residuos) == 0:
        print("Nenhum registro encontrado!")
        return

    busca = input("Digite o nome do resíduo: ").lower()

    encontrado = False

    for item in residuos:
        if item["tipo"].lower() == busca:
            print(f"{item['tipo']} - {item['quantidade']}")
            encontrado = True

        if not encontrado:
            print("Resíduo não encontrado!")

def editar_producao():
    if len(producao) == 0:
        print("Nenhum registro encontrado!")
        return

    busca = input("Digite o nome do produto que deseja  editar: ").lower()

    for item in producao:
        if item["produto"].lower() == busca:
            print("\nRegistro encontrado:")
            print(f"Data: {item['data']}")
            print(f"Produto: {item['produto']}")
            print(f"Quantidade: {item['quantidade']}")

            nova_data = input("Nova data: ")
            novo_produto = input("Novo produto: ")
            while True:
                 try:
                     nova_quantidade = int(input("Nova quantidade: "))
                     break
                 except ValueError:
                     print("Digite apenas números!")

                 item['data'] = nova_data
                 item['produto'] = novo_produto
                 item['quantidade'] = nova_quantidade

                 exportar_producao_csv()

                 print("Registro atualizado com sucesso!")
                 return
    print("Produto não encontrado!")

def editar_estoque():
    if len(estoque) == 0:
        print("Nenhum registro encontrado!")
        return

    busca = input("Digite o nome do material que deseja  editar: ").lower()

    for item in estoque:
        if item["material"].lower() == busca:
            print("\nRegistro encontrado:")
            print(f"Material: {item['material']}")
            print(f"Quantidade: {item['quantidade']}")

            novo_material = input("Novo material: ")
            while True:
                 try:
                     nova_quantidade = int(input("Nova quantidade: "))
                     break
                 except ValueError:
                     print("Digite apenas números!")

                 item['material'] = novo_material
                 item['quantidade'] = nova_quantidade

                 exportar_estoque_csv()

                 print("Registro atualizado com sucesso!")
                 return
    print("Material não encontrado!")

def editar_residuos():
    if len(residuos) == 0:
        print("Nenhum registro encontrado!")
        return

    busca = input("Digite o nome do resíduo que deseja  editar: ").lower()

    for item in residuos:
        if item["tipo"].lower() == busca:
            print("\nRegistro encontrado:")
            print(f"Resíduo: {item['tipo']}")
            print(f"Quantidade: {item['quantidade']}")

            novo_residuo = input("Novo resíduo: ")
            while True:
                 try:
                     nova_quantidade = int(input("Nova quantidade: "))
                     break
                 except ValueError:
                     print("Digite apenas números!")

                 item['material'] = novo_residuo
                 item['quantidade'] = nova_quantidade

                 exportar_residuos_csv()

                 print("Registro atualizado com sucesso!")
                 return
    print("Resíduo não encontrado!")

def excluir_producao():
    if len(producao) == 0:
        print("Nenhum registro encontrado!")
        return

    busca = input("Digite o nome do produto que deseja  excluir: ").lower()

    for item in producao:
        if item["produto"].lower() == busca:
            print("\nRegistro encontrado:")
            print(f"Data: {item['data']}")
            print(f"Produto: {item['produto']}")
            print(f"Quantidade: {item['quantidade']}")

            confirmar = input("Deseja excluir esse registro? (s/n): ").lower()

            if confirmar == 's':
                producao.remove(item)

                exportar_producao_csv()

                print("Registro excluido com sucesso!")
                return

            else:
                print("Exclusão cancelada.")
                return
            
    print("Produto não encontrado!")

carregar_producao_csv()
carregar_estoque_csv()
carregar_residuos_csv()

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
    print("9- Buscar produção")
    print("10- Buscar estoque")
    print("11- Buscar resíduos")
    print("12- Editar produção")
    print("13- Editar estoque")
    print("14- Editar resíduos")
    print("15- Excluir produção")
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
        buscar_producao()

    elif opcao == "10":
        buscar_estoque()

    elif opcao == "11":
        buscar_residuos()

    elif opcao == "12":
        editar_producao()

    elif opcao == "13":
        editar_estoque()

    elif opcao == "14":
        editar_residuos()
        
    elif opcao == '15':
        excluir_producao()

    elif opcao == "0":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
