try:
    a = int(input('>>>'))
    b = int(input('>>>'))
    lista  =  [a,b]
    print(a/b)
    i  =  int(input('Digite um indice da lista: '))
    print(lista[i])
except ZeroDivisionError as erro:
    print(erro)
except ValueError as erro :
    print(erro)
except TypeError as erro:
    print(erro)
except IndexError as erro:
    print(erro)
else:
    print('Erro não identificado') 
finally:
    print('Fim de carregamento ...')               

