#Recebendo salário do cidadão
salario = float(input("Digite o seu salário: "))
#Calculando imposto 

imposto1 = salario/100*8
imposto2 = salario/100*18
imposto3 = salario/100*28

#Condicionais para declarar o imposto de renda
if salario < 2000.01:
    print("Isento")

elif salario < 3000.01:
    print(f"seu imposto é de:{imposto1}")

elif salario <= 4500.00:
    print(f"seu imposto é de:{imposto2}")

else:
    print(f"seu imposto é de:{imposto3}")
