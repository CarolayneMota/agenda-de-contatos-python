import csv
global banco_contatos
banco_contatos = []

arq = open('./agenda.csv', 'a+')
banco_contatos = arq.readlines()
arq.close

print(banco_contatos)


ag = open("demofile.txt", "r")
def inserir():
    # cpf, nome, sobrenome, email, telefone, curso,
    # data_nasc, observacao
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


def salvar():
    return None

