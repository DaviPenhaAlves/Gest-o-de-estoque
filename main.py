from banco import criar_tabelas
from produtos import cadastrar_produto, listar_produtos
from movimentacoes import entrada_estoque, saida_estoque, historico

criar_tabelas()

while True:

    print("\n=== ESTOQUE ===")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Entrada estoque")
    print("4 - Saída estoque")
    print("5 - Histórico")
    print("6 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        espec = input("Especificações: ")

        cadastrar_produto(nome, categoria, preco, quantidade, espec)

    elif opcao == "2":
        for p in listar_produtos():
            print(p)

    elif opcao == "3":
        idp = int(input("ID produto: "))
        qtd = int(input("Quantidade: "))
        entrada_estoque(idp, qtd)

    elif opcao == "4":
        idp = int(input("ID produto: "))
        qtd = int(input("Quantidade: "))
        saida_estoque(idp, qtd)

    elif opcao == "5":
        for h in historico():
            print(h)

    elif opcao == "6":
        break