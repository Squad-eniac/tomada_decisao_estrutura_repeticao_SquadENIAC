'''O programa deve calcular e apresentar a quantidade de números pares e
ímpares inseridos. O processo de leitura deve ser encerrado quando o usuário
informar o valor zero. Certifique-se de incluir validações para garantir que
apenas números positivos sejam considerados na contagem e cálculos.'''

pares = 0 
impares = 0 
numeros_pares = []
numeros_impares = []

while True:
    
    numero = int(input('Digite um número positivo (ou 0 para encerrar o programa): '))
    if numero == 0:
        break
        
    if numero > 0:
        if numero % 2 == 0:
            pares += 1
            numeros_pares.append(numero)
        else:
            impares += 1
            numeros_impares.append(numero)
    else:
        print('Por favor, digite um número positivo')
        

print(f'Quantidade de números pares: {pares}')
print(f'Números pares digitados: {numeros_pares}')
print(f'Quantidade de números ímpares: {impares}')
print(f'Números ímpares digitados: {numeros_impares}')