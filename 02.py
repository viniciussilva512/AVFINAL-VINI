#Recebendo a variavel do salario do cidadão 

salario_atual = float(input("Digite seu salário atual: "))

#Linha de código para calcular o novo salario e seu reajuste
if salario_atual <= 400.00:
    novo_salario1 = salario_atual + salario_atual/100 * 15
    reajuste = novo_salario1 - salario_atual
    print(f"Novo salario: {novo_salario1}")
    print(f"Reajuste ganho: {reajuste}")
    print("Em percentual: 15%")

if 800.00 > salario_atual > 400.01:
    novo_salario2 = salario_atual + salario_atual/100*12
    reajuste2 = novo_salario2 - salario_atual
    print(f"Novo salario: {novo_salario2}")
    print(f"Reajuste ganho: {reajuste2}")
    print("Em percentual: 12% ")
    
if 1200.00 > salario_atual >= 800.01:
    novo_salario3 = round(salario_atual + salario_atual/100*10,2)
    reajuste3 = novo_salario3 - salario_atual
    print(f"Novo salario: {novo_salario3}")
    print(f"Reajuste ganho: {reajuste3}")
    print("Em percentual: 10% ")
    
if 2000.00 >= salario_atual  >= 1200.01:
    novo_salario4 = round(salario_atual + salario_atual/100*7,2)
    reajuste4 = novo_salario4 - salario_atual
    print(f"Novo salario: {novo_salario4}")
    print(f"Reajuste ganho: {reajuste4}")
    print("Em percentual: 7%")
    
if salario_atual > 2000.00:
    novo_salario5 = salario_atual = salario_atual/100*4
    reajuste5 = novo_salario5 - salario_atual
    print(f"Novo salario: {novo_salario5}")
    print(f"Reajuste ganho: {reajuste5}")
    print("Em percentual: 4%")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    