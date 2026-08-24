tarefas = []

while True:
    print("\n--- GERENCIADOR DE TAREFAS ---")
    print("1. Adicionar Tarefa")
    print("2. Listar Tarefas")
    print("3. Remover Tarefa")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == "1":
        nova_tarefa = input("Digite a nova tarefa: ").strip()
        if nova_tarefa != "":
            tarefas.append(nova_tarefa)
            print(f" Tarefa '{nova_tarefa}' adicionada com sucesso!")
        else:
            print(" O nome da tarefa não pode ser vazio.")

    elif opcao == "2":
        if not tarefas:
            print(" Nenhuma tarefa cadastrada.")
        else:
            print("\nSUAS TAREFAS:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

    elif opcao == "3":
        if not tarefas:
            print(" Não há tarefas para remover.")
        else:
            print("\nSUAS TAREFAS:")
            for i, tarefa in enumerate(tarefas, start=1):
                print(f"{i}. {tarefa}")

            try:
                indice = int(input("Digite o número da tarefa a remover: ")) - 1
                if 0 <= indice < len(tarefas):
                    removida = tarefas.pop(indice)
                    print(f" Tarefa '{removida}' removida!")
                else:
                    print(" Número de tarefa inválido.")
            except ValueError:
                print(" Por favor, digite um número válido.")

    elif opcao == "4":
        print("Saindo do sistema... Até logo!")
        break

    else:
        print(" Opção inválida. Tente novamente.")
