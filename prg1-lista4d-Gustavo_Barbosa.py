#!/bin/env python3
# coding: utf-8
# Marco André Mendes <marco.mendes@ifc.edu.br>
# Lista de exercícios de listas - temperaturas


def mes_extenso(mes):
    """Receba um número correspondente ao mês e devolva o nome do mês,
    com 3 letras. Ex.: 1-jan, 2-fev, ..., 12-dez.
    Use uma lista com os nomes dos meses."""



def media_temperaturas(temperaturas):
    """Devolva a média das temperaturas.
    Não use funções embutidas, como sum, min e max.
    """


def meses_acima(temperaturas, temperatura_base):
    """Devolva uma lista com os nomes dos meses em que a
    temperatura é maior que um valor informado pelo usuário.
    Use a função que faz o mês por extenso, desenvolvida anteriormente.
    """


def mes_mais_frio(temperaturas):
    """Devolva a menor temperatura da lista.
    Não use funções embutidas, como sum, min e max."""



# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31mFalhou'
    else:
        prefixo = '\033[32mPassou'
        acertos += 1
    print('{} Esperado: {} \tObtido: {}\033[1;m'.format(prefixo, esperado, obtido))


def main():
    print('Mês por extenso:')
    test(mes_extenso(1), 'jan')
    test(mes_extenso(2), 'fev')
    test(mes_extenso(12), 'dez')

    print('Média das temperaturas:')
    test(media_temperaturas([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 10.0)
    test(media_temperaturas([10, 12, 9, 13, 12, 10, 9, 13, 10, 12, 9, 13]), 11.0)

    print('Meses com temperaturas acima de um valor informado:')
    test(meses_acima([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 10), [])
    test(meses_acima([10, 12, 9, 13, 12, 10, 9, 13, 10, 12, 9, 13], 12), ['abr', 'ago', 'dez'])

    print('Menor temperatura:')
    test(mes_mais_frio([10, 10, 10, 10, 10, 9, 10, 7, 10, 9, 10, 10]), 7.0)
    test(mes_mais_frio([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]), 10.0)


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total, acertos,
                                                        total - acertos, float(acertos * 10) / total))
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")