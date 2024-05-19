'''Cara ou coroa com o 3ºA'''
from random import randint
from time import sleep

def jogar_cara_coroa():
    escolha = input('Cara ou coroa? ').strip().lower()
    while escolha not in ['cara', 'coroa']:
        print("Por favor, escolha 'cara' ou 'coroa'.")
        escolha = input('Cara ou coroa? ').strip().lower()

    resultado = randint(0, 1)
    sleep(1)

    if resultado == 0:
        print('Cara')
    else:
        print('Coroa')

    if resultado == 0 and escolha == 'cara' or resultado == 1 and escolha == 'coroa':
        print('Venceu!')
    else:
        print('Perdeu!')

def jogar_novamente():
    return input('Deseja jogar de novo? (s/n) ').strip().lower() == 's'

def main():
    while True:
        jogar_cara_coroa()
        if not jogar_novamente():
            break

if __name__ == "__main__":
    main()
