import random

class Dado:

    def __init__(self, lados):
        self.__lados = lados

    @property
    def verifica_dado(self):
        if self.__lados == 6:
            return f'Dado de 6 lados'
        elif self.__lados == 20:
            return f'Dado de RPG'
        else:
            return f'O dado só pode ser de 6 ou 20 lados'

    def joga_dado(self):
        if self.__lados == 6:
            jogada = random.randint(1, 6)
            print(jogada)
        if self.__lados == 20:
            jogada = random.randint(1, 20)
            print(jogada)


request = str(input('Você gostaria de jogar dados [S/ N]: '))
if request == 'S':
    dado = int(input('Qual dado você quer jogas de 6 ou de 20 lados? '))
    if dado == 6:
        dado1 = Dado(6)
        print(dado1.verifica_dado)
        print('1º jogada:')
        dado1.joga_dado()
        print('2° jogada:')
        dado1.joga_dado()
        resp = str(input('Voce quer jogar mais[S/N]'))
        i = 3
        while resp == 'S':
            print(f'{i}° jogada:')
            dado1.joga_dado()
            i+=1
            resp = str(input('Voce quer jogar mais[S/N]'))
    elif dado == 20:
        dado2 = Dado(20)
        print(dado2.verifica_dado)
        dado2.joga_dado()
        print('2° jogada:')
        dado2.joga_dado()
        resp = str(input('Voce quer jogar mais[S/N]'))
        i = 3
        while resp == 'S':
            print(f'{i}° jogada:')
            dado2.joga_dado()
            i += 1
            resp = str(input('Voce quer jogar mais[S/N]'))
else:
    print('Obrigado. Da próxima vez jogamos')