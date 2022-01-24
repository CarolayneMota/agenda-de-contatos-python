import csv
import os
global banco_contatos
banco_contatos = []

arq = open('./agenda.csv', 'a+')
banco_contatos = arq.readlines()
arq.close


def inserir():
    # cpf, nome, sobrenome, email, telefone, curso, data_nasc, observacao
    dados = ['cpf', 'nome', 'sobrenome', 'email', 'telefone', 'curso', 'data de nascimento', 'observação'] #para pedir as informações de forma pratica
    print('Informe todos os dados pedidos para inserir o contato\n')
    if len(banco_contatos) == 0: # se for o primeiro contato add na agenda
        aux = '' # aux para concatenar as informações
        for i in range(len(dados)): #para ir pedindo cada dado e concatenando 
            dado = input(f'Informe o/a {dados[i]}: ') #dedindo o dado
            if i == len(dados) - 1: # para colocar a quebra de linha 
                aux = aux + dado + ';' + '\n' #concatenando
            else:
                aux = aux + dado + ';' #concatenando
        banco_contatos.append(aux) #colocando na lista
    else: # caso não seja o primeiro contato add na agenda
        aux = '' # aux para concatenar as informações
        i = 0
        while i != len(dados):
            dado = input(f'Informe o/a {dados[i]}: ')
            if i == 0: # se for o primeiro dado(cpf) conferir se é repetido
                rep = 0 # variavel que vai informar se tem cpf repetido
                for j in range(len(banco_contatos)): # conferir de todos os contados exitentes
                    conf_cpf = banco_contatos[j].split(';') #transforma os dados em lista
                    print(f'conf_cpf: {conf_cpf}')
                    if dado == conf_cpf[0]: # confere se o cpf do novo contato é igual a algum existente no banco de contatos
                        print('CPF repetido!')
                        rep = 1 # informa q o cpf ta repetido
                        break
                aux = aux + dado + ';' #concatenando
            elif i == len(dados) - 1: # para colocar a quebra de linha
                aux = aux + dado + ';' + '\n' #concatenando    
            else:
                aux = aux + dado + ';' #concatenando
            if rep == 1: # se o cpf estiver repetido não será perguntado os proximos dados
                break
            i = i+ 1
        banco_contatos.append(aux) # armazena os dados na na lista
    salvar(aux) # salva os dados na csv
    return None


def atualizar_contato(cpf):
    """
        Crie uma função atualizar contato para atualizar as informações de
    um contato.
    i. Peça pro usuário digitar um CPF, verifique se existe. Se existir
    colete do usuário as novas informações e atualize o dado na
    lista. Para isso basta remover o usuário atual (Use a função
    remover(cpf)) e inserir logo após.
    ii. Após atualizar o dado deve-se salvar(Use a função salvar()) o
    arquivo agenda.csv
    """
    dados = ['cpf', 'nome', 'sobrenome', 'email', 'telefone', 'curso', 'data de nascimento', 'observação'] #para pedir as informações de forma pratica
    dado = ''
    rep = 0 # variavel que vai informar se o contato não está cadastrado
    for i in range(len(banco_contatos)):
        dado = banco_contatos[i].split(';')
        if str(cpf) == str(dado[0]): # verifica se o cpf informado é igual a algum que já está contido no banco_contatos
            banco_contatos.pop(i)
            # reescrever
            salvar(banco_contatos, 2)
            # Para atualizar o cadastro
            aux = '' # aux para concatenar as informações
            for j in range(len(dados)):
                dado = input(f'Informe o/a {dados[j]}: ')
                if j == len(dados) - 1: # para colocar a quebra de linha
                    aux = aux + dado + ';' + '\n' #concatenando    
                else:
                    aux = aux + dado + ';' #concatenando
            banco_contatos.append(aux) # armazena os dados na na lista
            salvar(aux) # salva os dados na csv
            break
        else:
            rep += 1 # informa se o contato não está cadastrado
    if rep == len(banco_contatos): # informa se o contato não está cadastrado
        print('Contato não cadastrado')
    return None


def mostrar_lista():
    dados = ''
    print('\tLista de contatos:')
    for i in range(len(banco_contatos)):
        dados = banco_contatos[i].split(';')
        print(dados)
        dados.pop(8)
        print(dados)
        print(f'CPF: {dados[0]}, nome: {dados[1]}, sobrenome: {dados[2]}, email: {dados[3]}, telefone: {dados[4]}, curso: {dados[5]}, data de nascimento: {dados[6]}, observação: {dados[7]}')
    return None


def buscar_contato_por_cpf(cpf):
    dados = ''
    for i in range(len(banco_contatos)):
        dados = banco_contatos[i].split(';')
        if cpf == dados[0]: # verifica se o cpf informado é igual a algum que já está contido no banco_contatos
            print(f'CPF: {dados[0]}, nome: {dados[1]}, sobrenome: {dados[2]}, email: {dados[3]}, telefone: {dados[4]}, curso: {dados[5]}, data de nascimento: {dados[6]}, observação: {dados[7]}{dados[8]}')
            break # Encerra pq não existe cpf iguais logo só há uma pessoa 
        else:
            print('Contato não cadastrado')
    return None


def buscar_contato_por_email(email):
    rep = 0 # variavel que vai informar se o contato não está cadastrado
    dados = ''
    for i in range(len(banco_contatos)):
        dados = banco_contatos[i].split(';')
        if email == dados[3]: # verifica se o email informado é igual a algum que já está contido no banco_contatos
            print(f'CPF: {dados[0]}, nome: {dados[1]}, sobrenome: {dados[2]}, email: {dados[3]}, telefone: {dados[4]}, curso: {dados[5]}, data de nascimento: {dados[6]}, observação: {dados[7]}{dados[8]}')
            break # Encerra pq não existe email iguais logo só há uma pessoa 
        rep = 1 # informa se o contato não está cadastrado
    if rep == 1: # informa se o contato não está cadastrado
        print('Contato não cadastrado')
    return None


def buscar_contato_por_nome(nome):
    dados = ''
    N_cad = 0 # N_cad(não cadastrada): variavel que é responsavel em informa se não tem o contato cadastrado
    for i in range(len(banco_contatos)):
        dados = banco_contatos[i].split(';')
        if nome.lower() == dados[1].lower():
            print(f'CPF: {dados[0]}, nome: {dados[1]}, sobrenome: {dados[2]}, email: {dados[3]}, telefone: {dados[4]}, curso: {dados[5]}, data de nascimento: {dados[6]}, observação: {dados[7]}{dados[8]}')
        else:
            N_cad += 1 
    if N_cad == len(banco_contatos): # se N_cad for igual ao números de pessoas no banco_contatos quer dizer q não existe uma pessoa com o nome informado para busca
        print('Contato não cadastrado')
    return None


def buscar_contato_por_curso(curso):
    dados = ''
    N_cad = 0 # N_cad(não cadastrada): variavel que é responsavel em informa se não tem o contato cadastrado
    for i in range(len(banco_contatos)):
        dados = banco_contatos[i].split(';')
        if curso.lower() == dados[5].lower():
            print(f'CPF: {dados[0]}, nome: {dados[1]}, sobrenome: {dados[2]}, email: {dados[3]}, telefone: {dados[4]}, curso: {dados[5]}, data de nascimento: {dados[6]}, observação: {dados[7]}{dados[8]}')
        else:
            N_cad += 1 
    if N_cad == len(banco_contatos): # se N_cad for igual ao números de pessoas no banco_contatos quer dizer q não existe uma pessoa com o nome informado para busca
        print('Contato não cadastrado')
    return None


def quantidade_de_contatos():
    qtd_pessoas = len(banco_contatos)
    return f'A quantidade de contatos cadastrados são {qtd_pessoas}'


def deletar_contato_por_cpf(cpf):
    """
        Crie uma função deletar contato por cpf que recebe como parâmetro
    o cpf de um contato e o elimina da lista.
    i. Antes de deletar o contato da lista verifique se o mesmo existe
    na lista.
    ii. Após deletar o contato salve o arquivo de agenda.csv com a
    função salvar()
    """
    i = 0
    rep = 0 # variavel que vai informar se o contato não está cadastrado
    dado = ''
    while i != len(banco_contatos):
        dado = banco_contatos[i].split(';')
        if str(cpf) == str(dado[0]): # verifica se o cpf informado é igual a algum que já está contido no banco_contatos
            banco_contatos.pop(i)
            print(banco_contatos)
            #  reescrever
            salvar(banco_contatos,2)
            print('Excluido')
        else:
            rep += 1 # informa se o contato não está cadastrado
        i +=1
    if rep == len(banco_contatos): # informa se o contato não está cadastrado
        print('Contato não cadastrado')
    return None


def deletar_contato_por_email(email):
    """
        Crie uma função deletar contato por email que recebe como
    parâmetro o email de um contato e o elimina da lista.
    i. Antes de deletar o contato da lista verifique se o mesmo existe
    na lista.
    ii. Após deletar o contato salve o arquivo de agenda.csv com a
    função salvar()
    """
    i = 0
    rep = 0 # variavel que vai informar se o contato não está cadastrado
    dado = ''
    while i != len(banco_contatos):
        dado = banco_contatos[i].split(';')
        if email.lower() == dado[3].lower(): # verifica se o email informado é igual a algum que já está contido no banco_contatos
            banco_contatos.pop(i)
            print(banco_contatos)
            #  reescrever
            salvar(banco_contatos, 2)
            print('Excluido')
        else:
            rep += 1 # informa se o contato não está cadastrado
        i +=1
    if rep == len(banco_contatos): # informa se o contato não está cadastrado
        print('Contato não cadastrado')
    return None


def salvar(dado, tipo=1):
    if tipo == 1:
        arq = open('./agenda.csv', 'a+')
        arq.write(dado) # escreve os dados 
        arq.close # fecha o arquivo
    elif tipo == 2:
        with open('./agenda.csv', 'w') as f: 
                for j in range(len(banco_contatos)):
                    f.write(banco_contatos[j])
    return None
