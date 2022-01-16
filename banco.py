import csv
global banco_contatos
banco_contatos = []

arq = open('./agenda.csv', 'a+')
banco_contatos = arq.readlines()
arq.close


def inserir():
    # cpf, nome, sobrenome, email, telefone, curso, data_nasc, observacao
    dados = ['cpf', 'nome', 'sobrenome', 'email', 'telefone', 'curso', 'data denascimento', 'observação'] #para pedir as informações de forma pratica
    print('Informe todos os dados pedidos para inserir o contato\n')
    if len(banco_contatos) == 0: # se for o primeiro contato add na agenda
        aux = '' # aux para concatenar as informações
        for i in range(len(dados)): #para ir pedindo cada dado e concatenando 
            dado = input(f'Informe o/a {dados[i]}: ') #dedindo o dado
            aux = aux + ';' + dado #concatenando
        banco_contatos.append(aux) #colocando na lista
    else: # caso não seja o primeiro contato add na agenda
        aux = '' # aux para concatenar as informações
        for i in range(len(dados)):
            dado = input(f'Informe o/a {dados[i]}: ')
            if i == 0: # se for o primeiro dado(cpf) conferir se é repetido
                for j in range(len(banco_contatos)): # conferir de todos os contados exitentes
                    conf_cpf = banco_contatos[j].split(';') #transforma os dados em lista
                    if dado == conf_cpf[0]: # confere se o cpf do novo contato é igual a algum exixtente no banco de contatos
                        print('CPF repetido!')
                        break
                    else:
                        aux = aux + ';' + dado
            else:
                aux = aux + ';' + dado
        banco_contatos.append(aux)
    salvar(aux)
    return None


def atualizar_contato():
    return None


def mostrar_lista():
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
    arq.write(dado)
    arq.close
    return None

