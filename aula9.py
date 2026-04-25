# # # for i in range(10):
# # #     print(i)
# # #             # start stop step by step


# # # estruturas compostas


# # # n =  10
# # # x  =  5.9
# # # x =  'True'


# # variavel_texto = 'isso é um texto'
# # lista = [1,0,2,3,6]
# # dicionario = {
# #     'a':10,
# #     'b':20
# #     }

# # c =  {1,2,3,6}
# # tupla = (5,6,6,5)


# # # for i in range(15):
# # #     nome  =  input('nome: ')
# # #     
# #             # start stop step by step
           
# # #for i in lista:
# #  #   print(i)


# # # for i in variavel_texto:
# # #     print(i)
            
# # # for x, y in dicionario.items():
# # #     print(x, y)
# # # 
# # # for i in  tupla:
# # #     print(i)
 
# # # for z  in x:
# # #     print(z)


# # # --------------------------------------


# # # while True:
# # # #     print('teste')
# # # import time


# # # contador = 0  
# # # while contador <= 10:
# # #     print(contador)
# # #     time.sleep(2)
# # #     contador =  contador + 1
    


# # pergunta = input('Deseja adicionar um dado a lista? ')
# # lista = []
# # while pergunta == 'sim':
# #       nome = input('nome: ')
# #       lista.append(nome)
# #       pergunta = input('deseja continuar? ')
# #       print(lista)


# # ## **2  - Exercícios**
# # ### **1. Tabuada Personalizada**

# # Peça ao usuário um número inteiro positivo. Use `for` para exibir a tabuada desse número de 1 a 10.

# # **Exemplo:**

# # `Digite um número: 7` → exibe 7 x 1 = 7, 7 x 2 = 14, ..., 7 x 10 = 70.

# # tabuada
 

# # Ex: tabuada


# import time
# numero =  int(input('numero inteiro: '))
# for x in range(11):
#     r =  numero * x
#     print(numero, 'x', x , '=', r)
#     time.sleep(2)


# # ### **2. Contagem Regressiva com Pausa**

# # Peça um número inteiro positivo. Use `while` para fazer uma contagem regressiva até 0, exibindo cada número. Após o término, exiba `"Fogo!"`.
# num = int(input("Digite um número inteiro positivo: "))

# while num >= 0:
#     print(num)
#     num -= 1

# print("Fogo!")
# # ---

# # ### **3. Média de Notas com `while`**

# # Peça notas até que o usuário digite `-1`. Calcule e exiba a média das notas válidas (0 a 10). Ignore entradas inválidas e use `continue` quando necessário.

# # soma = 0
# quantidade = 0

# while True:
#     nota = float(input("Digite uma nota (ou -1 para sair): "))

#     if nota == -1:
#         break

#     if nota < 0 or nota > 10:
#         print("Nota inválida, tente novamente.")
#         continue

#     soma += nota
#     quantidade += 1

# if quantidade > 0:
#     media = soma / quantidade
#     print(f"Média: {media:.2f}")
# else:
#     print("Nenhuma nota válida foi informada.")

# # ### **4. Validação de Senha com Limite de Tentativas**

# # Defina uma senha fixa (ex: `"python123"`). Dê ao usuário 3 tentativas usando `while`. Se acertar, exiba `"Acesso liberado"` e encerre. Se errar todas, exiba `"Conta bloqueada"`.

# # senha_correta = "python123"
# tentativas = 0

# while tentativas < 3:
#     senha = input("Digite a senha: ")

#     if senha == senha_correta:
#         print("Acesso liberado")
#         break

#     tentativas += 1

# if tentativas == 3:
#     print("Conta bloqueada")

# # ### **5. Números Primos**

# # Peça um número inteiro positivo e determine se ele é primo. Use `for` com `range` e `break` para otimizar.

# # num = int(input("Digite um número inteiro positivo: "))

# if num < 2:
#     print("Não é primo")
# else:
#     primo = True
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             primo = False
#             break

#     if primo:
#         print("É primo")
#     else:
#         print("Não é primo")

# # ### **6. Sequência de Fibonacci**

# # Gere os primeiros N termos da sequência de Fibonacci, onde N é informado pelo usuário. Use `for` ou `while` para iterar.

# #n = int(input("Quantos termos da sequência de Fibonacci? "))

# a, b = 0, 1

# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b

# # ### **7. Soma de Dígitos**

# # Peça um número inteiro positivo e calcule a soma de seus dígitos. Use `while` para extrair os dígitos um a um.

# # 
# num = int(input("Digite um número inteiro positivo: "))
# soma = 0

# while num > 0:
#     digito = num % 10
#     soma += digito
#     num //= 10

# print("Soma dos dígitos:", soma)

# # ### **8 Menu Interativo**

# # Crie um menu que permaneça ativo até que o usuário escolha a opção `"Sair"`. As opções podem ser:

# # - `1` – Exibir mensagem "Olá!"
# # - `2` – Exibir a data/hora atual (use `import datetime`)
# # - `3` – Sair

# # Use `while True` e `break` para sair.

# # import datetime

# while True:
#     print("\nMenu:")
#     print("1 - Olá")
#     print("2 - Data/Hora atual")
#     print("3 - Sair")

#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         print("Olá!")
#     elif opcao == "2":
#         agora = datetime.datetime.now()
#         print("Data/Hora atual:", agora)
#     elif opcao == "3":
#         print("Encerrando...")
#         break
#     else:
#         print("Opção inválida.")

# # ### **9 Simulador de Lançamento de Dados**

# # Simule 100 lançamentos de um dado de 6 faces. Conte quantas vezes cada face foi sorteada e exiba o resultado. Use `for` e `random.randint(1,6)`. (Importe `random`.)
# import random


# correçao 
# # i  =  input('digite o numero')
# # c = 0
# # while c <=0:
# #     z   =  [int(x) for x  in i]
# #     s = sum(z)
# #     c  =  c + 1
# # print(s) 

# x  =  input('digite um numero: ') 
# l = []
# n = 0
# while n < len(x):
#     #   print(n)
#       l.append(int(x[n]))
#       n += 1



# print(l)
# print(sum(l))