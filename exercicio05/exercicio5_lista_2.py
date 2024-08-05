'''EX5 - T0MADA DE DECISAO 
Desenvolva um programa que solicite ao usuário os comprimentos dos três
lados de um triângulo e classifique-o como equilátero, isósceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isósceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas'''


# Função para classificar o triângulo com base nos comprimentos dos lados
def classificar_triangulo(lado1, lado2, lado3):
    # Verifica se todos os lados são iguais
    if lado1 == lado2 == lado3:
        return "Equilátero"
    # Verifica se dois lados são iguais
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Isósceles"
    # Se todos os lados são diferentes
    else:
        return "Escaleno"

# Função principal do programa
def main():
    print("Classificador de Triângulos")

    # Solicita ao usuário os comprimentos dos lados do triângulo
    lado1 = float(input("Digite o comprimento do primeiro lado: "))
    lado2 = float(input("Digite o comprimento do segundo lado: "))
    lado3 = float(input("Digite o comprimento do terceiro lado: "))

    # Classifica o triângulo usando a função definida anteriormente
    tipo_triangulo = classificar_triangulo(lado1, lado2, lado3)

    # Exibe o resultado da classificação
    print(f"O triângulo é {tipo_triangulo}.")

# Executa o programa principal
if __name__ == "__main__":
    main()