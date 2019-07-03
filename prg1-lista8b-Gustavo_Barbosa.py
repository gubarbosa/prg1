#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 8b - revisão

def multi_string(s,n) :
    '''
    Seja uma string s e um inteiro positivo n
    retorna uma string com n cópias da string original
    multi_string('Oi', 2) -> 'OiOi'
    '''


def explode_string(s) :
    '''
    explode_string('Code') -> 'CCoCodCode'
    explode_string('abc') -> 'aababc'
    explode_string('ab') -> 'aab'
    '''


def conta_noves(nums) :
    ''' Conta quantas vezes aparece o 9 numa lista nums.'''


def nove_na_frente(nums) :
    '''
    verifica se pelo menos um dos quatro primeiros itens é nove
    nove_na_frente([1, 2, 9, 3, 4]) -> True
    nove_na_frente([1, 2, 3, 4, 9]) -> False
    nove_na_frente([1, 2, 3, 4, 5]) -> False
    '''


def alo_nome(nome) :
    '''
    Seja uma string nome
    alo_nome('Bob') -> 'Alô Bob!'
    alo_nome('Alice') -> 'Alô Alice!'
    alo_nome('X') -> 'Alô X!'
    '''


def cria_tags(tag,palavra) :
    '''
    cria_tags('i', 'Uhul'), '<i>Uhul</i>'
    cria_tags('i', 'Alô'), '<i>Alô</i>'
    cria_tags('cite', 'Uhul'), '<cite>Uhul</cite>'
    '''


def final_extra(s) :
    '''
    Seja um string s com no mínimo duas letras,
    retorna três vezes as duas últimas letras.
    final_extra('Alô'), 'lololo'
    final_extra('ab'), 'ababab'
    final_extra('Oi'), 'OiOiOi'
    '''


def primeira_metade(s) :
    '''
    Seja uma string s, retorna a primeira metade da string
    primeira_metade('papagaio') -> 'papa'
    primeira_metade('Lula') -> 'Lu'
    primeira_metade('abcdef') -> 'abc'
    '''


def sem_pontas(s) :
    '''
    Seja uma string s de pelo menos dois caracteres,
    retorna uma string sem o primeiro e último caracter.
    sem_pontas('Beleza') -> 'elez'
    sem_pontas('Python') -> 'ytho'
    sem_pontas('codigo') -> 'odig'
    '''


def gira_esquerda_2(s) :
    '''
    Rodar à esquerda uma string s duas posições
    a string possui pelo menos 2 caracteres
    gira_esquerda_2('Beleza') -> 'lezaBe'
    gira_esquerda_2('Oi') -> 'Oi'
    '''


# Área de testes: só mexa aqui se souber o que está fazendo!
acertos = 0
total = 0


def test(obtido,esperado) :
    global acertos,total
    total += 1
    if obtido != esperado :
        prefixo = '\033[31m%s' % ('Falhou')
    else :
        prefixo = '\033[32m%s' % ('Passou')
        acertos += 1
    print('%s Esperado: %s \tObtido: %s\033[1;m' % (prefixo,repr(esperado),
                                                    repr(obtido)))


def main() :
    print('Multi String')
    test(multi_string('Oi',2),'OiOi')
    test(multi_string('Oi',3),'OiOiOi')
    test(multi_string('Oi',1),'Oi')
    test(multi_string('Oi',0),'')
    test(multi_string('Oi',5),'OiOiOiOiOi')
    test(multi_string('Oh Boy!',2),'Oh Boy!Oh Boy!')
    test(multi_string('x',4),'xxxx')
    test(multi_string('',4),'')
    test(multi_string('code',2),'codecode')
    test(multi_string('code',3),'codecodecode')

    print('Explode string')
    test(explode_string('abc'),'aababc')
    test(explode_string('ab'),'aab')
    test(explode_string('x'),'x')
    test(explode_string('aqui'),'aaqaquaqui')
    test(explode_string('decai'),'ddedecdecadecai')
    test(explode_string('Beleza'),'BBeBelBeleBelezBeleza')
    test(explode_string('gago'),'ggagaggago')

    print('Conta noves')
    test(conta_noves([1,99,9]),1)
    test(conta_noves([1,9,9]),2)
    test(conta_noves([1,9,9,3,9]),3)
    test(conta_noves([1,2,3]),0)
    test(conta_noves([]),0)
    test(conta_noves([4,2,4,3,1]),0)
    test(conta_noves([9,2,99,3,1]),1)

    print('Nove na frente')
    test(nove_na_frente([1,2,9,3,4]),True)
    test(nove_na_frente([1,2,3,4,9]),False)
    test(nove_na_frente([1,2,3,4,5]),False)
    test(nove_na_frente([9,2,3]),True)
    test(nove_na_frente([1,9,9]),True)
    test(nove_na_frente([1,2,3]),False)
    test(nove_na_frente([1,9]),True)
    test(nove_na_frente([5,5]),False)
    test(nove_na_frente([2]),False)
    test(nove_na_frente([9]),True)
    test(nove_na_frente([]),False)
    test(nove_na_frente([3,9,2,3,3]),True)

    print('Alô nome')
    test(alo_nome('Bob'),'Alô Bob!')
    test(alo_nome('Alice'),'Alô Alice!')
    test(alo_nome('X'),'Alô X!')
    test(alo_nome('Alô'),'Alô Alô!')

    print('Cria Tags')
    test(cria_tags('i','Uhul'),'<i>Uhul</i>')
    test(cria_tags('i','Alô'),'<i>Alô</i>')
    test(cria_tags('cite','Uhul'),'<cite>Uhul</cite>')
    test(cria_tags('address','aqui'),'<address>aqui</address>')
    test(cria_tags('body','Coração'),'<body>Coração</body>')
    test(cria_tags('i','i'),'<i>i</i>')
    test(cria_tags('i',''),'<i></i>')

    print('Final extra')
    test(final_extra('Alô'),'lôlôlô')
    test(final_extra('ab'),'ababab')
    test(final_extra('Oi'),'OiOiOi')
    test(final_extra('Doce'),'cecece')
    test(final_extra('Beleza'),'zazaza')

    print('Primeira metade')
    test(primeira_metade('papagaio'),'papa')
    test(primeira_metade('Lula'),'Lu')
    test(primeira_metade('abcdef'),'abc')
    test(primeira_metade('ab'),'a')
    test(primeira_metade(''),'')
    test(primeira_metade('0123456789'),'01234')
    test(primeira_metade('buraco'),'bur')
    test(primeira_metade('joinville'),'join')

    print('Sem Pontas')
    test(sem_pontas('Beleza'),'elez')
    test(sem_pontas('Python'),'ytho')
    test(sem_pontas('codigo'),'odig')
    test(sem_pontas('sala'),'al')
    test(sem_pontas('ab'),'')
    test(sem_pontas('Chocolate!'),'hocolate')
    test(sem_pontas('cozinha'),'ozinh')
    test(sem_pontas('Uhull'),'hul')

    print('Gira Esquerda 2')
    test(gira_esquerda_2('Beleza'),'lezaBe')
    test(gira_esquerda_2('python'),'thonpy')
    test(gira_esquerda_2('Oi'),'Oi')
    test(gira_esquerda_2('code'),'deco')
    test(gira_esquerda_2('tio'),'oti')
    test(gira_esquerda_2('12345'),'34512')
    test(gira_esquerda_2('Chocolate'),'ocolateCh')
    test(gira_esquerda_2('tijolo'),'joloti')


if __name__ == '__main__' :
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total,acertos,
                                                        total - acertos,float(acertos * 10) / total))
    if total == acertos :
        print("Parabéns, seu programa rodou sem falhas!")