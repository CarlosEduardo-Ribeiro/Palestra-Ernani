'''Jokenpo com o 2ºA'''
from random import randint
from time import sleep

def contagem():
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')

def main():
    print('''         JOKENPO      
        Suas opções:
        [ 1 ] Pedra
        [ 2 ] Papel
        [ 3 ] Tesoura''') 
    
    while True:
        try:
            escolha = int(input('Qual a sua escolha? '))
            if escolha in [1, 2, 3]:
                break
            else:
                print('Escolha inválida. Por favor, escolha entre 1, 2 ou 3.')
                main()
        except ValueError:
            print('Entrada inválida. Por favor, insira um número.')

    computador = randint(0, 2)
    jogadas = ["Pedra", "Papel", "Tesoura"]
    
    contagem()
    print(f'Computador jogou {jogadas[computador]}')
    print(f'Jogador jogou {jogadas[escolha-1]}')

    if computador == escolha - 1:
        print('Empate')
    elif (computador + 1) % 3 == escolha - 1:
        print('Vitória')
    else:
        print('Derrota')

while True:
    main()
    continuar = input('Deseja jogar novamente? (s/n): ').lower()
    if continuar.lower() != 's':
        break