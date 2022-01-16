def menu():
    print(f"""\tMENU\n
            [1] Inserir contato\n
            [2] Atualizar contato\n
            [3] Mostrar agenda\n
            [4] Buscar contato(cpf)\n
            [5] Buscar contato(email)\n
            [6] Buscar contato(nome)\n
            [7] Buscar contato(curso)\n
            [8] Quantidade de contatos\n
            [9] Deletar contato(cpf)\n
            [10] Deletar contato(email)\n
            [11] Salvar e sair\n
        Informe o número com a opção do que deseja fazer\n 
    """)
    escolha = int(input('R: '))
    return escolha


