produtos = []

def adicionar_produto(nome):
    produtos.append(nome)

def contar_produtos(produtos):
    return len(produtos)


def listar_produtos():
    for p in produtos:
        print(p)


def buscar_produto(nome):
    return nome in produtos


def remover_produto(nome):
    if nome in produtos:
        produtos.remove(nome)

def listar_produtos_ordenados():
    for p in sorted(produtos):
        print (p)



def menu():
    while True:

        print("1 - Adicionar")
        print("2 - Listar")
        print("3 - Buscar")
        print("4 - Remover")
        print("5 - Contar Produtos")
        print("6 - Listar Produtos Ordenados")
        print("7 - Sair")

        opcao = input()

        if opcao == "1":
            nome = input("Produto: ")
            adicionar_produto(nome)

        elif opcao == "2":
            listar_produtos()

        elif opcao == "3":
            nome = input("Buscar: ")
            if buscar_produto(nome):
                print("Produto encontrado")
            else:
                print("Produto não encontrado")

        elif opcao == "4":
            nome = input("Remover: ")
            remover_produto(nome)

        elif opcao == "5":
            total = contar_produtos(produtos)
            print(f"Total de produtos: {total}")

        elif opcao == "6":
            listar_produtos_ordenados()

        elif opcao == "7":
            break

menu()

