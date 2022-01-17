from ast import Import
import menu
import banco

while True:
    escolha = menu.menu()
    if escolha == 1:
        banco.inserir()
    elif escolha == 2:
        cpf = input('Informe o cpf que quer atualizar: ')
        banco.atualizar_contato(cpf)
    elif escolha == 3:
        banco.mostrar_lista()
    elif escolha == 4:
        cpf = input('Informe o cpf que quer buscar: ')
        banco.buscar_contato_por_cpf(cpf)
    elif escolha == 5:
        email = input('Informe o email que quer buscar: ')
        banco.buscar_contato_por_email(email)
    elif escolha == 6:
        nome = input('Informe o nome que quer buscar: ')
        banco.buscar_contato_por_nome(nome)
    elif escolha == 7:
        curso = input('Informe o curso que quer buscar: ')
        banco.buscar_contato_por_curso(curso)
    elif escolha == 8:
        print(banco.quantidade_de_contatos())
    elif escolha == 9:
        cpf = int(input('Informe o cpf que quer deletar: '))
        banco.deletar_contato_por_cpf(cpf)
    elif escolha == 10:
        email = input('Informe o email que quer deletar: ')
        banco.deletar_contato_por_email(email)
    elif escolha == 11:
        break
