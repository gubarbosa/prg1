# Lista de exercícios de estruturas
# Resolva esses exercícios sem usar if, for ou while.
# Utilize apenas fatiamento, funções embutidas e métodos dos
# objetos string, lista, dicionário, etc.

def soma_dois_inteiros(a, b):
    """ Recebe dois números inteiros, e retorna a sua soma"""

def metro_para_milimetros(metros):
    """ Recebe um valor em metros, e retorna o valor em milímetros"""


def tempo_para_percorrer_uma_distancia(distancia, velocidade):
    """ Recebe uma distância e a velocidade de movimentação, e retorna
    as horas que seriam gastas para percorrer em linha reta"""



def aumento_salarial(salario, porcentagem):
    """ Recebe um salário e sua porcentagem de aumento, e retorna
    o novo salário"""


def preco_com_desconto(preco_original, percentual_desconto):
    """ Recebe um preço e sua porcentagem de desconto, e retorna
    novo preço"""


def dias_para_segundos(dias, horas, minutos, segundos):
    """ Recebe uma data em dias com horas, minutos e segundos, e retorna
    a data em segundos"""


def celsius_para_fahrenheit(c):
    """ Recebe uma temperatura em celsius, e retorna a temperatura
    em fahrenheit"""


def fahrenheit_para_celsius(f):
    """ Recebe uma temperatura em fahrenheit, e retorna a temperatura
     em celsius"""


def preco_aluguel_carro(dias, km):
    """ Recebe uma quantidade de dias que o carro foi alugado e a
    quantidade de quilômetros rodados, e retorna o valor a ser pago.
    1 dia: 60 reais mais R$ 0,15 por km rodado."""


def dias_perdidos_por_fumar(cigarros_fumados_por_dia, anos_fumando):
    """ Recebe uma quantidade de cigarros fumados por dia e a quantidade
     de anos que fuma, e retorna o total de dias perdidos, sabendo que
     cada cigarro reduz a vida em 10 minutos."""


def dois_elevado_a_um_milhao():
    """ Calcula dois elevado a um milhão, e retorna a quantidade de
    algarismos"""


def media_final_aprovado_reprovado(p1, p2, ep1, ep2):
    """ Recebe as notas das 2 provas e 2 exercícios de programação e retorna
    se o aluno foi ou não aprovado. As provas têm peso 7 e os exercícios
    têm peso 3. Cada parcial tem peso igual."""


def salario(valor_hora, horas_mensais):
    """ Recebe quanto ganha por hora e quantas horas trabalho ao mês,
    e retorna o salário líquido.

    Descontos:
    - INSS é 8% do salário bruto
    - IR é 11% do salário bruto
    - Sindicato é 5% do salário bruto"""


def tinta(metros_pintar):
    """ Recebe quantos metros quadrados precisa pintar,
    e retorna a quantidade de latas de tinta a comprar.
    A cobertura da tinta é de 3 metros por litro de tinta
    Cada lata possui 18 litros de tinta"""


def duzias(ovos):
    ''' Receba o número de ovos e devolva a quantidade de dúzias
    correspondente. Considere sempre dúzias cheias, arredondando pra
    cima se necessário.
    '''


def decompor_numero(numero):
    '''
    Leia um número inteiro menor que 1000 e devolva a quantidade de
    centenas, dezenas e unidades do mesmo.
    Obs.: não utilize operações com strings
    '''


def palindrome(texto):
    """Faça uma função que verifique se uma textro passado é palíndrome,
    isto é, se é igual quando lido de trás pra frente."""


def troca_caixa(texto):
    """Vogais ficam em caixa alta (maiúsculas)
    Consoantes ficam em caixa baixa (minúsculas)"""


def imprime_mes_por_extenso(data):
    """Faça um programa que solicite a data de nascimento (dd/mm/aaaa)
    e imprima com o nome do mês por extenso
    """


def encontra_caracter(texto, caracter_procurado):
    """Receba um texto e retorne a localização da primeira vez que
    aparece o caracter especificado"""




def é_azarado(numero):
    """O último dígito não pode ser igual ao primeiro, porque isso dá azar."""


def ondernamento_contrario(lista):
    """ Devolve a lista invertida"""


def maximo(lista):
    """ Calcule o maior número da 'lista' """


def minimo(lista):
    """ Calcule o menor número da 'lista' """


def maior_menor(lista):
    """ Calcule o maior e o menor numero da 'lista' """


def media_saltos_lista(saltos):
    """Receba uma lista com os saltos de um atleta e calcule a média
    dos seus saltos, sabendo que o melhor e o pior saltos são desconsiderados.
    """


def contem(lista, item_procurado):
    """Verifica se uma lista contém um item e devolve um valor booleano."""


def conta(lista, item_procurado):
    """Informa quantas ocorrências de um item existem numa lista."""


def mes_extenso(mes):
    """Receba um número correspondente ao mês e devolva o nome do mês,
    com 3 letras. Ex.: 1-jan, 2-fev, ..., 12-dez.
    Use uma lista com os nomes dos meses."""


def media_temperaturas(temperaturas):
    """Devolva a média das temperaturas.
    """


def leet(texto):
    '''
    Converte texto em leet
    troca = {'a':'4','e':'3','g':'9','i':'1','s':'5','t':'7','o':'0'}
    '''


def apaga(s, n):
    """
    Seja uma string s e um inteiro n
    retorna uma nova string sem a posição n
    apaga('kitten', 1) -> 'ktten'
    apaga('kitten', 4) -> 'kittn'
    """


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido, esperado):
    global acertos, total
    total += 1
    if obtido != esperado:
        prefixo = '\033[31m%s' % 'Falhou'
    else:
        prefixo = '\033[32m%s' % 'Passou'
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo, repr(esperado),
                                                    repr(obtido)))


def main():
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista2 = [-1, 0]
    lista3 = [-10, 0, 10, 2, 100, -100, -100.1]
    lista4 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

    print('Soma dois inteiros:')
    test(soma_dois_inteiros(0, 0), 0)
    test(soma_dois_inteiros(-1, 0), -1)
    test(soma_dois_inteiros(1, 1), 2)
    test(soma_dois_inteiros(0, -1), -1)
    test(soma_dois_inteiros(10, 10), 20)
    test(soma_dois_inteiros(-10, -10), -20)
    test(soma_dois_inteiros(-10, 20), 10)

    print('Metros para milimetros:')
    test(metro_para_milimetros(0), 0)
    test(metro_para_milimetros(1), 1000)
    test(metro_para_milimetros(1.8), 1800)
    test(metro_para_milimetros(1.81), 1810)

    print('Tempo gasto para percorrer um distancia a uma velocidade'
          'constante(linha reta):')
    test(tempo_para_percorrer_uma_distancia(1330, 20), 66.50)
    test(tempo_para_percorrer_uma_distancia(1000, 100), 10.00)
    test(tempo_para_percorrer_uma_distancia(1000, 123), 8.13)
    test(tempo_para_percorrer_uma_distancia(100000, 201), 497.51)

    print('Aumento salarial baseado na porcentagem de aumento:')
    test(aumento_salarial(1330, 20), 1596.00)
    test(aumento_salarial(1000, 0), 1000.00)
    test(aumento_salarial(1000.10, 123), 2230.22)
    test(aumento_salarial(0.0, 200), 0.00)

    print('Desconto do preco atual baseado na porcentagem do desconto:')
    test(preco_com_desconto(1330, 20), 1064.00)
    test(preco_com_desconto(1000, 0), 1000.00)
    test(preco_com_desconto(1000.10, 5.5), 945.09)
    test(preco_com_desconto(0.0, 200), 0.00)

    print('Dias,horas,minutos e segundos para segundos:')
    test(dias_para_segundos(0, 0, 0, 0), 0)
    test(dias_para_segundos(0, 0, 0, 1), 1)
    test(dias_para_segundos(0, 0, 0, 30), 30)
    test(dias_para_segundos(0, 0, 1, 0), 60)
    test(dias_para_segundos(0, 0, 1, 1), 61)
    test(dias_para_segundos(0, 1, 0, 0), 3600)
    test(dias_para_segundos(0, 0, 60, 0), 3600)
    test(dias_para_segundos(1, 0, 0, 0), 86400)
    test(dias_para_segundos(1, 1, 1, 1), 90061)
    test(dias_para_segundos(0, 23, 59, 59), 86399)
    test(dias_para_segundos(10, 20, 59, 1), 939541)

    print('Celsius para Fahrenheit:')
    test(celsius_para_fahrenheit(0), 32.00)
    test(celsius_para_fahrenheit(100), 212.00)
    test(celsius_para_fahrenheit(30), 86.00)
    test(celsius_para_fahrenheit(300), 572.00)
    test(celsius_para_fahrenheit(-100), -148.00)
    test(celsius_para_fahrenheit(1), 33.80)

    print('Fahrenheit para Celsius:')
    test(fahrenheit_para_celsius(32), 0)
    test(fahrenheit_para_celsius(212), 100)
    test(fahrenheit_para_celsius(30), -1.11)
    test(fahrenheit_para_celsius(300), 148.89)
    test(fahrenheit_para_celsius(-100), -73.33)
    test(fahrenheit_para_celsius(1), -17.22)

    print('Preco a pagar pelo aluguel do carro:')
    test(preco_aluguel_carro(10, 100), 615.00)
    test(preco_aluguel_carro(13, 133), 799.95)
    test(preco_aluguel_carro(1, 0), 60.00)
    test(preco_aluguel_carro(3, 79), 191.85)

    print('Total de dias que perdeu de viver por ter fumados:')
    test(dias_perdidos_por_fumar(10, 10), 253.47)
    test(dias_perdidos_por_fumar(13, 13), 428.37)
    test(dias_perdidos_por_fumar(0, 110), 0.00)
    test(dias_perdidos_por_fumar(3, 79), 600.73)

    print('Calcula a quantidade de numeros que ha em dois elevado a um'
          'milhao:')
    test(dois_elevado_a_um_milhao(), 301030)

    print('Média final:')
    test(media_final_aprovado_reprovado(10, 10, 0, 0), True)
    test(media_final_aprovado_reprovado(0, 0, 10, 10), False)
    test(media_final_aprovado_reprovado(10, 10, 10, 10), True)
    test(media_final_aprovado_reprovado(0, 0, 5, 0), False)
    test(media_final_aprovado_reprovado(8.0, 7.0, 9.0, 8.0), True)

    print('Salário líquido:')
    test(salario(10, 80), 608)
    test(salario(100, 30), 2280)
    test(salario(2.5, 300), 570)
    test(salario(5, 120), 456)

    print('Latas de tinta:')
    test(tinta(10), 1)
    test(tinta(100), 2)
    test(tinta(560), 11)
    test(tinta(50001), 926)

    print('Dúzias:')
    test(duzias(12), 1)
    test(duzias(24), 2)
    test(duzias(11), 1)
    test(duzias(23), 2)

    print('Decompor número:')
    test(decompor_numero(326), (3, 2, 6))
    test(decompor_numero(320), (3, 2, 0))
    test(decompor_numero(310), (3, 1, 0))
    test(decompor_numero(305), (3, 0, 5))
    test(decompor_numero(300), (3, 0, 0))
    test(decompor_numero(100), (1, 0, 0))
    test(decompor_numero(101), (1, 0, 1))
    test(decompor_numero(311), (3, 1, 1))
    test(decompor_numero(111), (1, 1, 1))
    test(decompor_numero(12), (0, 1, 2))
    test(decompor_numero(25), (0, 2, 5))
    test(decompor_numero(20), (0, 2, 0))
    test(decompor_numero(10), (0, 1, 0))
    test(decompor_numero(21), (0, 2, 1))
    test(decompor_numero(11), (0, 1, 1))
    test(decompor_numero(16), (0, 1, 6))
    test(decompor_numero(1), (0, 0, 1))
    test(decompor_numero(7), (0, 0, 7))

    print(' Palindrome:')
    test(palindrome("ovo"), True)  # normal
    test(palindrome("Ovo"), True)  # mudança de caixa
    test(palindrome("Ovo "), True)  # espaço no final
    test(palindrome(" Ovo "), True)  # espaço no início
    test(palindrome('Assam a massa'), True)  # frases (espaços em branco)
    test(palindrome('Ame o poema!'), True)  # frases com pontuação

    print(' Troca caixa:')
    test(troca_caixa("Araquari"), "ArAqUArI")  # normal
    test(troca_caixa("Caxias do Sul"), "cAxIAs dO sUl")  # com espaços

    print(' Mês por extenso:')
    test(imprime_mes_por_extenso("19/05/2014"), "19 de maio de 2014")
    test(imprime_mes_por_extenso("25/12/2016"), "25 de dezembro de 2016")

    print(' Encontra caracter:')
    test(encontra_caracter("--*--", "*"), 2)
    test(encontra_caracter("19/05/2014", "/"), 2)

    print(' É azarado:')
    test(é_azarado('213452'), True)
    test(é_azarado('213451'), False)

    print(' Listas invertidas:')
    test(ondernamento_contrario(lista1), ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    test(ondernamento_contrario(lista2), ([0, -1]))
    test(ondernamento_contrario(lista3), ([-100.1, -100, 100, 2, 10, 0, -10]))

    print(' Maior e o menor da lista:')
    test(maior_menor(lista1), (10, 1))
    test(maior_menor(lista2), (0, -1))
    test(maior_menor(lista3), (100, -100.1))
    test(maior_menor(lista4), (-1, -10))

    print(' Média dos saltos em lista:')
    test(media_saltos_lista([10, 10, 10, 10, 10]), 10)
    test(media_saltos_lista([9, 9.1, 8, 7, 6.9]), 8)
    test(media_saltos_lista([1, 1, 3, 5, 5]), 3)
    test(media_saltos_lista([10, 10, 9.9, 10, 10]), 10)
    test(media_saltos_lista([1, 4.5, 0, 7, 5]), 3.5)

    print('Possui item:')
    test(contem([1, 2, 3, 4, 5], 6), False)
    test(contem([1, 2, 3, 4, 5], 3), True)
    test(contem(['b', 's', 'i'], 'i'), True)
    test(contem(['b', 's', 'i'], 'S'), False)

    print('Conta itens:')
    test(conta([1, 2, 3, 4, 5], 6), 0)
    test(conta([1, 2, 3, 4, 5], 1), 1)
    test(conta([1, 2, 1, 4, 1], 1), 3)
    test(conta(['b', 's', 'i'], 'i'), 1)
    test(conta(['b', 's', 'i'], 'S'), 0)
    test(conta(['b', 's', 'i', 'i', 'f', 'c'], 'i'), 2)

    print('Mês por extenso:')
    test(mes_extenso(1), 'jan')
    test(mes_extenso(2), 'fev')
    test(mes_extenso(12), 'dez')

    print('Média das temperaturas:')
    test(media_temperaturas(
        [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    ), 10.0)
    test(media_temperaturas(
        [10, 12, 9, 13, 12, 10, 9, 13, 10, 12, 9, 13]
    ), 11.0)

    print('leet')
    test(leet('ifc'), '1fc')
    test(leet('fisl2013'), 'f15l2013')
    test(leet('deco'), 'd3c0')
    test(leet('EMO'), '3M0')
    test(leet('restart'), 'r3574r7')
    test(leet('infeliz'), '1nf3l1z')
    test(leet('The Cure'), '7h3 Cur3')
    test(leet('Eu te amo'), '3u 73 4m0')

    print('Apaga')
    test(apaga('kitten', 1), 'ktten')
    test(apaga('kitten', 0), 'itten')
    test(apaga('kitten', 2), 'kiten')
    test(apaga('kitten', 4), 'kittn')
    test(apaga('Hi', 0), 'i')
    test(apaga('Hi', 1), 'H')
    test(apaga('code', 0), 'ode')
    test(apaga('code', 1), 'cde')
    test(apaga('code', 2), 'coe')
    test(apaga('code', 3), 'cod')
    test(apaga('chocolate', 8), 'chocolat')


if __name__ == '__main__':
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (
        total, acertos, total - acertos, float(acertos * 10) / total)
    )
    if total == acertos:
        print("Parabéns, seu programa rodou sem falhas!")