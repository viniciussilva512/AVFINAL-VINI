# Iniciar a contagem de números 
quantidade_positivos = 0

# Lista para armazenar os números 
numeros_positivos = []

# Loop para coletar os números e identificar se são positivos ou negativos 
for _ in range(6):
    numero = float(input("Digite um número: "))

    # Verificar se o número é positivo ou negativo
    if numero > 0:
        print("O número é positivo.")
        quantidade_positivos += 1
        numeros_positivos.append(numero)

    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")

# Mostrar a quantidade 
print(f"\nQuantidade de números positivos: {quantidade_positivos}")

if quantidade_positivos > 0:
    print("Números positivos:")
    for num_positivo in numeros_positivos:
        print(num_positivo)
