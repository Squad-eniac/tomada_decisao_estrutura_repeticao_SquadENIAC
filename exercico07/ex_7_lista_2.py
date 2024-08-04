'''
Desenvolver um programa que solicite a idade do usuário e identifique se
ele é uma criança, um adolescente, adulto ou idoso.
'''

try:
    idade = int(input('Digite a sua idade: '))

    if 0 < idade <= 12:
        print('Você é uma criança')
    elif 12 < idade < 18:
        print('Você é um(a) adolescente')
    elif 17 < idade < 60:
        print('Você é um(a) adulto(a)')
    elif 59 < idade <= 105:
        print('Você é um(a) idoso(a)')
    else:
        print('Valor inválido')

except ValueError:
    print('Por favor, insira um número válido.')