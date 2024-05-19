'''Calculadora simples com o 3ºB'''
n1 = float(input('Primeiro número: '))
print('''Opções
               [ 0 ] +
               [ 1 ] -
               [ 2 ] *
               [ 3 ] /
               ''')
operacao = int(input('Qual a sua escolha? '))
n2 = float(input('Segundo número: '))
match operacao:
    case 0:
        print(f'{n1} + {n2} = {n1+n2}')
    case 1:
        print(f'{n1} - {n2} = {n1-n2}')
    case 2:
        print(f'{n1} x {n2} = {n1*n2}')
    case 3:
        print(f'{n1} / {n2} = {n1/n2}')
    case _:
        print('Operação invalida tente novamente.')