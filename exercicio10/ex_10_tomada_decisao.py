#Faça um programa que lê três números inteiros e os mostra em ordem crescente

def ordenar_numeros(n1, n2, n3):
    numeros = [n1, n2, n3]

    numeros_ordenados = sorted(numeros)

    return numeros_ordenados


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

numeros_ordenados = ordenar_numeros(numero1, numero2, numero3)
print("Os números em ordem crescente são:", numeros_ordenados)