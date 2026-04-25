# # def nome():
# #     return 'teste'


# # print(nome())    


# # # variável fora da função
# # n = 10
# # def soma():
# #     n  =  20
# #     return n


# # print(n)
# # print(soma())


# # # variaveis locais são criadas dentro da função 
# # # variaveis globais são criadas fora da função






# # # parametros
# # # padrão
# # def soma (a, b):
# #     return a +  b
# # soma (10,20)


# # # nomeados
# # def sub(a = 10 , b = 10):
# #     return a  +  b 
# # sub(200)


# # # pocisionais
# # def mult(a , b  =  200, c=0):
# #     return a * b * c 



# # def v_salario_hora(carga, salario=250):
# #     return salario / carga


# # salario_hora =  v_salario_hora(100,1010)
# # adicional =  salario_hora * 0.7
# # print(salario_hora +  adicional)

# # def saque(saldo, saque):
# #     return saldo - saque 

# # def deposito(saldo,saque):
# #     return saldo + sauqe 
# # def extrato (ex):
# #     def emprestimp(valor,saldo):
# #         return valor + saldo 
# #     def main_banco():
# #         dados
# #         menu = unput(''Escolha uma opção:
# #                      1 - saque 
# #                      2 - deposito
# #                      3 - extrato 
# #                      4 - emprestimo

# #                      ''')
# #      if menu == '1' : 
# #      valor = float (input('R$ '))
# #      saqu = saque (dados[' saldo'], valor) 
# #      depo ['extratos'] . append(-valor)
# #      print(deposito
# # elif munu == '3' :







# # ## **Exercícios de Nível Médio**

# # ### **1. Calculadora com Funções**

# # Crie funções separadas para as quatro operações básicas (`somar`, `subtrair`, `multiplicar`, `dividir`). Em seguida, escreva um programa que leia dois números e a operação desejada (como string) e chame a função correspondente. A divisão deve tratar divisão por zero.
# def somar(a, b):
#     return a + b

# def subtrair(a, b):
#     return a - b

# def multiplicar(a, b):
#     return a * b

# def dividir(a, b):
#     if b == 0:
#         return "Erro: divisão por zero"
#     return a / b

# # Programa principal
# a = float(input("Digite o primeiro número: "))
# b = float(input("Digite o segundo número: "))
# op = input("Operação (+, -, *, /): ")

# if op == "+":
#     print(somar(a, b))
# elif op == "-":
#     print(subtrair(a, b))
# elif op == "*":
#     print(multiplicar(a, b))
# elif op == "/":
#     print(dividir(a, b))
# else:
#     print("Operação inválida")

# # ### **2. Validador de CPF (simplificado)**

# # Crie uma função `validar_cpf(cpf)` que recebe uma string com 11 dígitos e retorna `True` se for válido (use o algoritmo básico de validação de CPF). Em seguida, teste a função com alguns CPFs.

# # https://dicasdeprogramacao.com.br/algoritmo-para-validar-cpf/
# def validar_cpf(cpf):
#     if len(cpf) != 11 or not cpf.isdigit():
#         return False

#     # Primeiro dígito
#     soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
#     d1 = (soma * 10 % 11) % 10

#     # Segundo dígito
#     soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
#     d2 = (soma * 10 % 11) % 10

#     return cpf[-2:] == f"{d1}{d2}"

# # Teste
# print(validar_cpf("11144477735"))

# # ### **3. Gerador de Tabuada**

# # Escreva uma função `tabuada(numero, inicio=1, fim=10)` que exibe a tabuada do `numero` no intervalo `[inicio, fim]`. Se os argumentos `inicio` e `fim` não forem fornecidos, use 1 e 10.
# def tabuada(numero, inicio=1, fim=10):
#     for i in range(inicio, fim + 1):
#         print(f"{numero} x {i} = {numero * i}")

# tabuada(5)

# # ### **4. Contador de Palavras**

# # Crie uma função `contar_palavras(texto)` que retorna um dicionário com a contagem de cada palavra no texto (considere palavras separadas por espaços). O programa principal deve ler uma frase e exibir o resultado.
# def contar_palavras(texto):
#     palavras = texto.split()
#     contagem = {}

#     for p in palavras:
#         contagem[p] = contagem.get(p, 0) + 1

#     return contagem

# frase = input("Digite uma frase: ")
# print(contar_palavras(frase))

# # ### **5. Ordenação Personalizada**

# # Implemente uma função `ordenar_lista(lista, crescente=True)` que retorna uma nova lista ordenada. Se `crescente=True`, ordena em ordem crescente; caso contrário, decrescente. Não use `sorted()` ou `list.sort()` (implemente o algoritmo de ordenação de sua escolha, como bolha).
# def ordenar_lista(lista, crescente=True):
#     nova = lista[:]
#     n = len(nova)

#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if (crescente and nova[j] > nova[j+1]) or (not crescente and nova[j] < nova[j+1]):
#                 nova[j], nova[j+1] = nova[j+1], nova[j]

#     return nova

# print(ordenar_lista([5, 2, 9, 1], True))
# # ### **6. Jogo de Adivinhação**

# # Crie uma função `jogar()` que sorteia um número entre 1 e 100 e dá dicas ("maior", "menor") até o usuário acertar. Use `random.randint()`. A função deve retornar o número de tentativas. No programa principal, chame a função e exiba quantas tentativas foram necessárias.

# import random

# def jogar():
#     numero = random.randint(1, 100)
#     tentativas = 0

#     while True:
#         palpite = int(input("Adivinhe o número: "))
#         tentativas += 1

#         if palpite < numero:
#             print("Maior")
#         elif palpite > numero:
#             print("Menor")
#         else:
#             print("Acertou!")
#             return tentativas

# print("Tentativas:", jogar())
# # ### **7. Conversor de Bases**

# # Escreva uma função `converter_base(numero, base_origem, base_destino)` que converte um número entre bases 2, 8, 10 e 16. A entrada `numero` é uma string. A função retorna a string convertida. (Exemplo: `converter_base("1010", 2, 16)` → `"A"`). Use `int()` com base e depois formate.

# # Conteúdo para auxiliar

# # https://dev.to/udanielnogueira/valores-em-binario-octal-e-hexadecimal-em-python-pn7

# def converter_base(numero, base_origem, base_destino):
#     decimal = int(numero, base_origem)

#     if base_destino == 2:
#         return bin(decimal)[2:]
#     elif base_destino == 8:
#         return oct(decimal)[2:]
#     elif base_destino == 16:
#         return hex(decimal)[2:].upper()
#     else:
#         return str(decimal)

# print(converter_base("1010", 2, 16))
# # ### **8. Sistema de Caixa Eletrônico**
# def sacar(valor):
#     if valor % 2 != 0 or valor <= 0:
#         return None

#     notas = [100, 50, 20, 10, 5, 2]
#     resultado = {}

#     for n in notas:
#         qtd = valor // n
#         if qtd > 0:
#             resultado[n] = qtd
#             valor %= n

#     return resultado

# print(sacar(186))
# # Crie uma função `sacar(valor)` que retorna um dicionário com a quantidade de notas de 100, 50, 20, 10, 5 e 2 necessárias para o valor. O valor deve ser inteiro e positivo. Caso não seja possível (valor não múltiplo de 2), a função retorna `None`. No programa principal, chame a função e exiba o resultado.

# # ### **9. Análise de Lista com Múltiplos Retornos**

# # Escreva uma função `analisar_lista(lista)` que retorna quatro valores: o menor valor, o maior valor, a soma e a média. No programa principal, receba uma lista de números do usuário (terminada por -1) e exiba os resultados usando desempacotamento.
# def analisar_lista(lista):
#     menor = min(lista)
#     maior = max(lista)
#     soma = sum(lista)
#     media = soma / len(lista)
#     return menor, maior, soma, media

# lista = []
# while True:
#     num = int(input("Digite um número (-1 para parar): "))
#     if num == -1:
#         break
#     lista.append(num)

# menor, maior, soma, media = analisar_lista(lista)
# print(menor, maior, soma, media)
# # ### **10. Função que Modifica Lista Global**

# # Crie uma lista global `estoque = []`. Escreva funções:

# # - `adicionar_produto(nome, quantidade)`: adiciona um dicionário `{"nome": nome, "quantidade": quantidade}` à lista global.
# # - `remover_produto(nome)`: remove o produto com esse nome (se existir).
# # - `listar_estoque()`: exibe todos os produtos.
    
# #     Use a palavra-chave `global` para modificar a lista dentro das funções. O programa principal deve apresentar um menu interativo para o usuário.


# estoque = []

# def adicionar_produto(nome, quantidade):
#     global estoque
#     estoque.append({"nome": nome, "quantidade": quantidade})

# def remover_produto(nome):
#     global estoque
#     estoque = [p for p in estoque if p["nome"] != nome]

# def listar_estoque():
#     for p in estoque:
#         print(p)

# # Menu
# while True:
#     print("\n1-Adicionar 2-Remover 3-Listar 0-Sair")
#     op = input("Escolha: ")

#     if op == "1":
#         nome = input("Nome: ")
#         qtd = int(input("Quantidade: "))
#         adicionar_produto(nome, qtd)

#     elif op == "2":
#         nome = input("Nome: ")
#         remover_produto(nome)

#     elif op == "3":
#         listar_estoque()

#     elif op == "0":
        # break