# 1. Verificação de maioridade e permissão
# Enunciado:
# Crie um programa que leia a idade do usuário e se ele possui autorização dos pais 
# (responda True ou False).
# O usuário pode participar da atividade se tiver 18 anos ou mais ou 
# tiver autorização dos pais.
# Use and / or para verificar e exiba "Pode participar" ou "Não pode participar".

# :idade  = int(input('Idade: '))
# autorizacao = bool(input('Possui autorização?>>>  '))
# pode  =  idade >= 18 and autorizacao == True
# msg =  pode and "Pode participar" or "Não pode participar"
# print(msg)


# print(participar)

# 2. Classificação de peso ideal
# Enunciado:
# Leia o peso (kg) e a altura (m) de uma pessoa. Calcule o IMC (peso / altura**2).
# Uma pessoa está com peso normal se o IMC estiver entre 18.5 e 24.9 (inclusive).
# Use operadores lógicos para verificar se o IMC está nessa faixa e exiba 
# "Peso normal" ou "Fora da faixa".

# Leitura dos dados
# peso = float(input("Digite o peso (kg): "))
# altura = float(input("Digite a altura (m): "))

# # Cálculo do IMC
# imc = peso / (altura ** 2)

# verificacao_imc  = imc >= 18.5 and imc <= 24.9 and 'PESO NORMAL' or 'FORA DA FAIXA'

# print ( verificacao_imc)

 # 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário 
# for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" 
# ou "Acesso negado".

# usuario = input('usuario: ')
# senha = input('senha: ')

# acessos= ((usuario == "admin" and senha == "1234") and "Acesso liberado" or "Acesso negado")

# print (acessos)

# 4. Compra com desconto
# Enunciado:
# Leia o valor da compra e se o cliente é VIP (True ou False).
# O cliente ganha 10% de desconto se o valor for maior que R$ 100 ou ele for VIP.
# Exiba o valor final com desconto (se aplicável) ou o valor original.

# valor = float(input(R$ ))
# vip =  input('Pessoa é Vip ? True ou'False: ') 

# v = (valor > 100 or vip == 'True') and f' Desconto aplicado R$ ( valor)

# valor_final = valor - desconto

# print(valor_final)





# 5. Elegibilidade para doação de sangue
# Enunciado:
# Leia a idade e o peso.
# Para doar sangue, a pessoa deve ter entre 16 e 69 anos (inclusive) e 
# pesar pelo menos 50 kg.
# Use and para verificar ambos os critérios e informe se a pessoa pode doar.

# idade  = int(input('Idade: '))
# peso = float(input("Digite o peso (kg): "))

# verificacao_doar  = (idade >= 16 and idade <= 69 and peso >= 50) and 'Pode doar' or 'Não pode doar'

# print( verificacao_doar )


# 6. Validação de horário de funcionamento
# Enunciado:
# Uma loja funciona de segunda a sexta, das 9h às 18h.
# Leia o dia da semana (1=segunda, 7=domingo) e a hora (0 a 23).
# Determine se a loja está aberta.
# Dica: use and para combinar dia útil com horário, e or se quiser tratar 
# sábado/domingo como fechado.

# h = int(input('Hora: '))
# dia_semana =  int(input('Dia da Semana: '))


# v =  h > 8 and h < 19 and dia_semana >0 and  dia_semana <6 and 'Aberto' or 'fechado'


# print(v)

# 7. Aprovação em duas disciplinas
# Enunciado:
# Leia as notas de Matemática e Português.
# O aluno é aprovado se ambas as notas forem maiores ou iguais a 6.
# Use and para verificar e exiba "Aprovado" ou "Reprovado".

# # Leitura das notas
# matematica = float(input("Digite a nota de Matemática: "))
# portugues = float(input("Digite a nota de Português: "))

# # Resultado usando operador lógico
# resultado = (matematica >= 6) and (portugues >= 6)

# # Saída
# print(resultado * "Aprovado" + (not resultado) * "Reprovado")


# 8. Identificação de ano bissexto
# Enunciado:
# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que 
# também seja divisível por 400.
# Leia um ano e use and e or para determinar se ele é bissexto.
# Exiba "Ano bissexto" ou "Ano não bissexto".

# ano = int(input("Digite um ano: "))

# print((ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)and "Ano bissexto" or "Ano não bissexto")

# 
# 9. Faixa etária
# Enunciado:
# Leia a idade e classifique:

# "Criança" se idade < 12

# "Adolescente" se 12 ≤ idade ≤ 17

# "Adulto" se idade ≥ 18
# Use and e or para definir os intervalos e exiba a classificação.

# idade = int(input())

# print((idade < 12 and "Criança") or (12 <= idade <= 17 and "Adolescente") or (idade >= 18 and "Adulto"))
    
    

# 10. Sistema de alerta de temperatura e umidade
# Enunciado:
# Leia a temperatura (°C) e a umidade (%).
# Dispare um alerta se temperatura > 35 ou umidade > 70.
# Caso contrário, exiba "Condições normais".
# Use or para combinar as condições.
# ```

# Desafio:

# Contexto:

# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).

# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80) e G == 1

# Alto: (T > 40 ou U > 80) e G == 0

# Médio: (T entre 25 e 40) e (U entre 50 e 80)

# Baixo: qualquer outra situação

# temperatura = float(input())
# umidade = float(input())

# print((temperatura > 35 or umidade > 70) and "Alerta" or "Condições normais")

# Desafio:

# Contexto:

# Uma indústria monitora temperatura (T), umidade (U) e presença de gás inflamável (G, 0 ou 1).

# O nível de risco é dado por:

# Crítico: (T > 40 ou U > 80) e G == 1

# Alto: (T > 40 ou U > 80) e G == 0

# Médio: (T entre 25 e 40) e (U entre 50 e 80)

# Baixo: qualquer outra situação

# T = float(input( 'Temperatura >>>'))
# U = float(input('Umidade >>>'))
# G = int(input('Gás >>>'))

# print((T > 40 or U > 80) and G == 1 and "Crítico") or ((T > 40 or U > 80) and G == 0 and "Alto") or ((25 <= T <= 40) and (50 <= U <= 80) and "Médio") or "Baixo" 

    