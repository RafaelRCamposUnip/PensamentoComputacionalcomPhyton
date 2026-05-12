import json
import os

arquivos="contatos.js"
#funções
def carregar_contatos():
    if not os.path.exists(arquivo):
        return[]
    with open(arquivo, "r", enconding="utf-8") as arquivo:
        return json.load(arquivo)

def salvar_contato(contatos):
    with open(arquivo,"w",encoding="utf-8") as arquivo:
        json.dump(contatos, arquivo, intent=4, ensure_ascii=false)

#crud
def cadastrar_contato(contatos):
    nome=input("Nome:")
    telefone=input("telefone:")
    email=input("E-mail:")

    contato={
        "nome":Nome,
        "telefone":Telefone,
        "email":Email
    }
    contatos.append(contato)
    salvar_contato(contatos)
    print("\nContato cadastrado com sucesso!\n")

def listar_contatos(contatos):
    if not contatos:
        print("\nNenhum contato cadastrado.\n")
        return
    print("\n::Contatos::")
    for i, contato in (contatos, start=1):
        print(f"""
        contato{i}
        nome:{contato['nome']}
        telefone:{contato['telefone']}
        email:{contato['email']}
        """)

def buscar_contato(contatos):
    nome=input("Digite o nome para buscar:").lower()
    encontrados=[
        contato for contato in contatos
        if nome in contato["nome"].lower()
        ]
        if not encontrados:
            print("\nContato não encontrado.\n")
            return
        print("\n::Resultados::")
        for contato in encontrados:
            print(f"""
            nome:{contato['nome']}
            telefone:{contato['telefone']}
            email:{contato['email']}
            """)

def editar_contato(contatos):
    listar_contatos(contatos)
    try
        indice=int(input("informe o numero do contato que deseja editar:"))-1
        if indice<0 or indice >=len(contatos):
            print("contato inválido")
            return
        contatos[indice]["nome"]=input("Novo nome:")
        contatos[indice]["telefone"]=input("Novo telefone:")
        contatos[indice]["email"]=input("Novo e-mail:")
        
        salvar_contato(contatos)
        print("\n contato atualizado!\n ")
        
    except ValueError:
        print("Digite um número válido.")
        
def excluir_contato(contatos)
    listar_contatos(contatos)
    try
        indice=int(input("informe o número do contato que deseja excluir:"))-1
        if indice<0 or indice >=len(contatos):
            print("contato inválido")
            return
        removido=contato.pop(indice)
        salvar_contato(contatos)
        print(f"Contato{removido['nome']}removido")
    except ValueError:
        print("Informe um número válido")

#Menu
def menu():
    contatos=carregar_contatos()
    while True:
        print("""
        ::AGENDA::
        1-Cadastrar contato
        2-Listar contato
        3-Buscar contato
        4-Editar contato
        5-Excluir contato
        0-Sair
        ::------::
        """)
        opcao=input("Escolha:")
        match opcao:
            case'1':
                cadastrar_contato(contatos)
            
            case'2':
                listar_contatos(contatos)
            
            case'3':
                buscar_contato(contatos)
            
            case'4':
                editar_contato(contatos)
            
            case'5':
                excluir_contato(contatos)
            
            case'0':
                print("\nEncerrando sistema...")
                break
            
            case _:
                print("\nOpção inválida")

#Programa Principal
menu()