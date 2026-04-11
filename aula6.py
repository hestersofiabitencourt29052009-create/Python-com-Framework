# DESAFIO AULA 6 -  GOOGLE CLASS

# Use dicionário, variáveis ou listas … 

# Contexto:
# Uma loja oferece um cupom especial. O cliente ganha o cupom se atender a pelo menos  das seguintes condições:

# Se for VIP (responde "sim" ou "não")
# Valor da compra acima de R$ 200
# Primeira compra no mês (responder "sim" ou "nao")

# Além disso, o cupom  pode ser aplicado se o cliente tiver  no histórico. 

# Tarefa Receba:

# vip (string "sim" ou "nao")
# valor (float)
# primeira_compra (string "sim" ou "nao")
# Reclamação 

# Determine se o cliente  ("Cupom liberado") ou  ("Sem cupom"),  (SEM IF , SEM LOOP, SEM FUNÇÃO)# D

vip = input("É VIP? (sim/não): ") == "sim"
valor = float(input("Valor da compra: "))
primeira_compra = input("Primeira compra? (sim/não): ") == "sim"
reclamacao = input("Tem reclamação? (sim/não): ") == "sim"

cupom = (vip or valor < 200 or primeira_compra) and not reclamacao

resultado = ["Sem cupom", "Cupom liberado"][cupom]

print(resultado)