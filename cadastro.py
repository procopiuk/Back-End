clientes = []

while True:
    print("/n ==MENU==")
    print("1. Cadastrar novo cliente")
    print("2. Listar clientes cadastrados")
    print("3. sair")

    opcao = input("/n Escolha uma opção")

    if opcao == '1':
        print("\n --- NOVO CADASTRO---")
        nome = input("Nome completo: ")
        telefone = input("Telefone: ")

        cliente = {
            'nome': nome,
            'telefone': telefone
        }

        clientes.append(cliente)
        print("\n Cliente cadastro com sucesso")

        elif opcao == '2':
            print("\n ---CLIENTES CADASTRADOS---")
            if len(clientes) == 0:
                print("nenhum cliente cadastrado")
                else:
                    for i, cliente in enumerate(clientes, 1):
                        print(f"\n Cliente{i}:")
                        print(f"Nome: {cliente['nome']}")
                        print(f"Telefone:{cliente['telefone']}") 