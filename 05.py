def contar_pares():
    # Começar a contar números pares
    numeros_pares = 0

    # Loop obtendo os cinco número do usuario
    for _ in range(5):
        # Obter um número do usuário
        numero_str = input("Digite um número inteiro: ")

        # Converter para um número inteiro
        numero = int(numero_str)

        # Verificar se o número é par
        if numero % 2 == 0:
            numeros_pares += 1

    # Retornar a quantidade total de números pares
    return numeros_pares

# Chamar a função e exibir o resultado
total_pares = contar_pares()
print(f'Total de números pares: {total_pares}')
