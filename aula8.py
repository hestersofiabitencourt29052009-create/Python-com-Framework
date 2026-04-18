# idade =  int(input('Idade: '))
# carta_m =  input('POssui carta sim ou não?')
# decisao =  idade>=18 and carta_m == 'sim' and 'Pode dirigir' or 'não pode...'
# print(decisao)

# if idade >= 18 and carta_m == 'sim':
#     print('Pode ')
# else:
#     print('Não pode')
    
# if idade >= 18:
#    if carta_m == 'sim':
#        print('Pode ')
# else:
#     print('Não pode')
    
    
# if idade >= 18 and carta_m == 'sim':
#    print('Pode ')
# elif idade >= 18 and carta_m == 'não':
#    print('pode tirar a carta')
# else:
#    print('Não pode')
# print('SISTEMA DE NOTAS')
# lista_nomes = []
# aluno_1 =  input('Digite o nome do aluno: ')
# aluno_2 =  input('Digite o nome do aluno: ')
# lista_nomes.append(aluno_1)
# lista_nomes.append(aluno_2)
# print('lista de alunos: ', lista_nomes)

# notas_aluno_1 = [float(input(f'nota1 {aluno_1}: ')), float(input(f'nota2 {aluno_1}: '))]
# notas_aluno_2 = [float(input(f'nota1 {aluno_2}: ')), float(input(f'nota2 {aluno_1}: '))]

# media_aluno_1 = sum(notas_aluno_1)/len(notas_aluno_1)
# media_aluno_2  = sum(notas_aluno_2)/len(notas_aluno_2)
# print('Aluno', aluno_1, 'Média', media_aluno_1)
# print('Aluno', aluno_2, 'Média', media_aluno_2)

# if media_aluno_1 > 6:
#     print('Aluno aprovado', aluno_1)
# elif media_aluno_1 >= 5 and media_aluno_1 <= 6:
#     print('Aluno de recuperação', aluno_1)
# else:
#     print('Aluno reprovado', aluno_1)

# print('.......................................')

# if media_aluno_2 > 6:
#     print('Aluno aprovado', aluno_2)
# elif media_aluno_2 >= 5 and media_aluno_2 <= 6:
#     print('Aluno de recuperação', aluno_2)
# else:
#     print('Aluno reprovado', aluno_2)


#    Crie um programa que leia a nota de um aluno (0 a 10) e exiba a menção correspondente:

# - `"Excelente"` se nota >= 9
# - `"Bom"` se nota >= 7 e < 9
# - `"Regular"` se nota >= 5 e < 7
# - `"Insuficiente"` se nota < 5



# aluno1 = float(input('nota1: 0 à 10 ')) 

# if aluno1 >=9:
#     print('excelente')
# elif  aluno1  >= 7 and aluno1 < 9:
#     print('bom')

# elif aluno1 >=5 and aluno1 < 7:
#     print( ' regular')
# else :
#     print ( ' insuficiente')            









# ### **2. Validação de Triângulo**

# Leia três lados de um triângulo. Verifique se eles formam um triângulo (cada lado é menor que a soma dos outros dois). Se sim, classifique como:

# - `"Equilátero"` (todos os lados iguais)
# - `"Isósceles"` (dois lados iguais)
# - `"Escaleno"` (todos diferentes)


# a = float(input("Lado 1: "))
# b = float(input("Lado 2: "))
# c = float(input("Lado 3: "))

# if (a + b > c) and (a + c > b) and (b + c > a):
#     print("É um triângulo.")
    
    
#     if a == b == c:
#         print("Classificação: Equilátero")
#     elif a == b or b == c or a == c:
#         print("Classificação: Isósceles")
#     else:
#         print("Classificação: Escaleno")
# else:
#     print("Os valores não formam um triângulo.")





### **3. Cálculo de IMC com Faixas**
# Leia peso (kg) e altura (m). Calcule o IMC e classifique conforme a tabela da OMS:

# - `"Abaixo do peso"` se IMC < 18.5
# - `"Peso normal"` se 18.5 ≤ IMC < 25
# - `"Sobrepeso"` se 25 ≤ IMC < 30
# - `"Obesidade"` se IMC ≥ 30

# peso = float(input('peso:'))
# altura = float(input('altura'))
# imc = peso / (altura ** 2)
# if imc < 18.5:
#     print('abaixo do peso')
# elif imc >=18.5 and imc < 25:
#     print ('peso normal')
# elif imc <=25  and imc <= 30:
#     print('sobrepeso')
# if imc >= 30:
#     print ('obesidade')


# # ### **4. Imposto de Renda Simplificado**

# # Leia o salário bruto mensal e calcule o desconto do INSS (11% sobre o salário, limitado a R$ 1.500,00) e o IRRF conforme tabela:

# # - Isento se salário bruto ≤ R$ 2.500,00
# # - 7,5% sobre o que exceder R$ 2.500,00 até R$ 3.500,00
# # - 15% sobre o que exceder R$ 3.500,00 até R$ 5.000,00
# # - 27,5% sobre o que exceder R$ 5.000,00
    
# #     Exiba o salário líquido após os descontos.


# # salario = float(input('R$ '))

# # if salario >= 1500.0 and salario >=2500.0
# # inss = salario * 0.11
# # print ('INSS:' , inss)
# # salario = salario - inss
# # print('desconto de 11% R$', salario_inss)

# # elif salario > 2500.0 and salario >= 3500.0
# # inss = salario * 0.15
# # print ('INSS:' , inss)
# # salario_ = salario - inss
# # print('desconto IRRF de 15% R$' , salario_inss)

# # salario > 2500.0 and salario >= 3500.0
# # inss = salario * 0.0
# # print ('INSS:' , inss)
# # salario = salario - inss
# # print('desconto IRRF de 15% R$' , salario_inss)



# # # ### **5. Jogo de Pedra, Papel e Tesoura**
# # Leia duas jogadas (`"pedra"`, `"papel"` ou `"tesoura"`) e determine o vencedor ou empate. Use condicionais aninhadas.
# def jogar_pedra_papel_tesoura():
#     # 1. Entrada de dados
#     jogador1 = input("Jogador 1 (pedra, papel, tesoura): ").lower().strip()
#     jogador2 = input("Jogador 2 (pedra, papel, tesoura): ").lower().strip()

#     print("-" * 30)

#     # 2. Verificação de Empate
#     if jogador1 == jogador2:
#         print(f"Empate! Ambos escolheram {jogador1}.")
    
#     # 3. Lógica com Condicionais Aninhadas
#     else:
#         if jogador1 == "pedra":
#             if jogador2 == "tesoura":
#                 print("Jogador 1 venceu! (Pedra quebra Tesoura)")
#             else: # jogador2 é papel
#                 print("Jogador 2 venceu! (Papel cobre Pedra)")
        
#         elif jogador1 == "papel":
#             if jogador2 == "pedra":
#                 print("Jogador 1 venceu! (Papel cobre Pedra)")
#             else: # jogador2 é tesoura
#                 print("Jogador 2 venceu! (Tesoura corta Papel)")
        
#         elif jogador1 == "tesoura":
#             if jogador2 == "papel":
#                 print("Jogador 1 venceu! (Tesoura corta Papel)")
#             else: # jogador2 é pedra
#                 print("Jogador 2 venceu! (Pedra quebra Tesoura)")
        
#         else:
#             print("Entrada inválida. Use apenas 'pedra', 'papel' ou 'tesoura'.")

# # Executar o jogo
# jogar_pedra_papel_tesoura()




# # ### **6. Aprovação com Recuperação**

# # Leia a nota da N1 e N2. Calcule a média (`(N1+N2)/2`). Se média ≥ 7, aprovado. Se média < 4, reprovado. Caso contrário, o aluno vai para recuperação. Nesse caso, leia a nota da recuperação (NR). A média final é `(média + NR)/2`. Se média final ≥ 5, aprovado; senão, reprovado.
# # 1. Leitura das notas iniciais
# n1 = float(input("Digite a nota N1: "))
# n2 = float(input("Digite a nota N2: "))

# # 2. Cálculo da média inicial
# media = (n1 + n2) / 2
# print(f"Média inicial: {media:.2f}")

# # 3. Verificação da situação do aluno
# if media >= 7:
#     print("Situação: Aprovado")
# elif media < 4:
#     print("Situação: Reprovado")
# else:
#     print("Situação: Recuperação")
#     # 4. Processo de Recuperação
#     nr = float(input("Digite a nota da recuperação (NR): "))
#     media_final = (media + nr) / 2
#     print(f"Média final após recuperação: {media_final:.2f}")
    
#     if media_final >= 5:
#         print("Situação: Aprovado na Recuperação")
#     else:
#         print("Situação: Reprovado na Recuperação")

# # ### **7. Alistamento Militar**

# # Leia o ano de nascimento, o sexo (`M` ou `F`) e se o usuário possui alguma deficiência impeditiva (`sim` ou `não`).
# import datetime

# def verificar_alistamento():
#     # 1. Obter ano atual automaticamente
#     ano_atual = datetime.date.today().year
    
#     # 2. Leitura dos dados
#     try:
#         ano_nascimento = int(input("Digite o ano de nascimento: "))
#         sexo = input("Digite o sexo (M/F): ").strip().upper()
#         deficiencia = input("Possui deficiência impeditiva? (sim/não): ").strip().lower()
        
#         idade = ano_atual - ano_nascimento
        
#         # 3. Lógica de validação
#         if deficiencia == 'sim':
#             print("Não apto: A deficiência impeditiva dispensa o alistamento.")
#         elif sexo != 'M':
#             print("Não obrigatório: O alistamento obrigatório é apenas para o sexo masculino.")
#         elif idade < 18:
#             print(f"Não apto: Você tem {idade} anos. O alistamento é obrigatório no ano em que completa 18 anos.")
#         elif idade >= 18:
#             print(f"Apto: Você tem {idade} anos. Proceda com o alistamento.")
#         else:
#             print("Dados inválidos.")
            
#     except ValueError:
#         print("Erro: Por favor, digite um ano válido.")

# # Executar a função
# verificar_alistamento()


# # - Se sexo for `F`, exiba `"Não obrigatório"`.
# # - Se sexo for `M`, calcule a idade. Se idade < 18, exiba o tempo restante. Se idade = 18, exiba `"Aliste-se imediatamente"`. Se idade > 18 e ≤ 45, exiba `"Já passou do prazo"`. Se idade > 45, exiba `"Dispensado por idade"`.
# # - Se houver deficiência, altere a mensagem para `"Dispensado por condição de saúde"` (prioridade sobre outras mensagens).

# # ### **8. Escolha de Plano de Saúde**

# # Leia a idade do cliente e o tipo de plano (`"basico"`, `"standard"`, `"premium"`). O valor mensal é calculado como:

# # - Básico: R$ 100 + (idade * 2)
# # - Standard: R$ 150 + (idade * 3)
# # - Premium: R$ 200 + (idade * 5)
    
# #     Se o cliente tiver mais de 60 anos, há um acréscimo de 10% sobre o valor total.
    
# # Entrada de dados
# idade = int(input("Digite a idade do cliente: "))
# plano = input("Escolha o plano (basico, standard, premium): ").strip().lower()

# # Cálculo do valor base por tipo de plano
# if plano == "basico":
#     valor_mensal = 100 + (idade * 2)
# elif plano == "standard":
#     valor_mensal = 150 + (idade * 3)
# elif plano == "premium":
#     valor_mensal = 200 + (idade * 5)
# else:
#     valor_mensal = 0
#     print("Plano inválido.")

# # Aplicação do acréscimo para maiores de 60 anos
# if valor_mensal > 0:
#     if idade > 60:
#         valor_mensal *= 1.10  # Acréscimo de 10%

#     print(f"O valor mensal do plano {plano} para {idade} anos é: R$ {valor_mensal:.2f}")

# # ### **9. Validação de Data**

# # Leia um dia (1-31), mês (1-12) e ano (qualquer). Verifique se a data é válida, considerando meses com 30/31 dias e fevereiro (28 ou 29 dias, considerando ano bissexto: divisível por 400 ou (divisível por 4 e não por 100)).
# dia = int(input("Dia: "))
# mes = int(input("Mês: "))
# ano = int(input("Ano: "))

# valida = False

# # Meses com 31 dias
# if mes in [1, 3, 5, 7, 8, 10, 12]:
#     if 1 <= dia <= 31:
#         valida = True
# # Meses com 30 dias
# elif mes in [4, 6, 9, 11]:
#     if 1 <= dia <= 30:
#         valida = True
# # Fevereiro e a regra do bissexto
# elif mes == 2:                           
#     if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
#         if 1 <= dia <= 29:
#             valida = True
#     elif 1 <= dia <= 28:
#         valida = True

# if valida:
#     print(f"A data {dia}/{mes}/{ano} é válida.")
# else:
#     print("Data inválida.")

# # ### **10. Simulador de Caixa Eletrônico**

# # Leia o valor a ser sacado (inteiro, múltiplo de 5, entre 10 e 1000). Calcule a menor quantidade possível de notas de 50, 20, 10 e 5. Exiba a quantidade de cada nota. Caso o valor não esteja dentro das regras, exiba uma mensagem de erro.

# Solicita o valor ao usuário
# try:
#     valor = int(input("Digite o valor para saque (múltiplo de 5, entre 10 e 1000): "))

#     # Validação das regras
#     if valor < 10 or valor > 1000 or valor % 5 != 0:
#         print("Erro: Valor inválido. O saque deve ser entre R$ 10 e R$ 1000 e múltiplo de 5.")
#     else:
#         print(f"Saque de R$ {valor} processado:")
        
#         # Cálculo das notas usando divisão inteira e resto
#         for nota in [50, 20, 10, 5]:
#             quantidade = valor // nota
#             valor %= nota
#             if quantidade > 0:
#                 print(f"{quantidade} nota(s) de R$ {nota}")

# except ValueError:
#     print("Erro: Por favor, digite apenas números inteiros.")







