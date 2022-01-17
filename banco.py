import csv
from operator import le
from subprocess import DETACHED_PROCESS
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
                    else:
                        aux = aux + dado + ';' #concatenando
            elif j == len(dados) - 1: # para colocar a quebra de linha
                aux = aux + dado + ';' + '\n' #concatenando    
            else:
                aux = aux + dado + ';' #concatenando
            if rep == 1: # se o cpf estiver repetido não será perguntado os proximos dados
                break
            i = i+ 1
        banco_contatos.append(aux) # armazena os dados na na lista
    print(f'banco_contatos: {banco_contatos}')
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
    return None


def mostrar_lista():
    dados = ''
    print('\tLista de contatos:')
    for i in range(len(banco_contatos)):
        dados = banco_contatos[i].split(';')
        print(f'CPF: {dados[0]}, nome: {dados[1]}, sobrenome: {dados[2]}, email: {dados[3]}, telefone: {dados[4]}, curso: {dados[5]} ,data de nascimento: {dados[6]} ,observação: {dados[7]}{dados[8]}')
    return None


def buscar_contato_por_cpf(cpf):
    return None


def buscar_contato_por_email(email):
    return None


def buscar_contato_por_nome(nome):
    return None


def buscar_contato_por_curso(curso):
    return None


def quantidade_de_contatos():
    return None


def deletar_contato_por_cpf(cpf):
    return None


def deletar_contato_por_email(email):
    return None


def salvar(dado):
    arq = open('./agenda.csv', 'a+')
    arq.write(dado) # escreve os dados 
    arq.close # fecha o arquivo
    return None

