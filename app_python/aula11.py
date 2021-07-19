
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
    
except ZeroDivisionError:
    print('Não é possivel realizar divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except Exception as ex:
    print('erro desconhecido. Erro: ()'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()

# lista = [1, 10]
# try:
#     divisao = 10 / 0
#     numero = lista[1]
#
# except ZeroDivisionError:
#     print('Não é possivel realizar divisão por 0')
# except ArithmeticError:
#     print('Houve um erro ao realizar uma operação aritmética')
# except IndexError:
#     print('Erro ao acessar um indice inválido da lista')
# except Exception as ex:
#     print('erro desconhecido. Erro: ()'.format(ex))

# lista = [1, 10]
# try:
#     divisao = 10 / 0
#     numero = lista[1]
#
# except BaseException as ex:
#     print('erro desconhecido. Erro: ()'.format(ex))
# except ZeroDivisionError:
#     print('Não é possivel realizar uma divisão por 0')
# except IndexError:
#     print('Erro ao acessar um indice inválido da lista')



# lista = [1, 10]
# try:
#     divisao = 10 / 1
#     numero = lista[1]
#     x = a
# except ZeroDivisionError:
#     print('Não é possivel realizar uma divisão por 0')
# except IndexError:
#     print('Erro ao acessar um indice inválido da lista')
# except BaseException as ex:
#     print('erro desconhecido. Erro: ()'.format(ex))

# lista = [1, 10]
# try:
#     divisao = 10 / 0
#     numero = lista[3]
# except ZeroDivisionError:
#     print('Não é possivel realizar uma divisão por 0')