#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 8d - revisão

def numero_invertido(numero) :
    '''Receba um inteiro positivo e o mostre invertido. Ex.: 1234 gera 4321'''
    string = str(numero)
    numero_invertido = int(string[::-1])
    return numero_invertido

def gago(texto) :
    '''Receba um texto e devolva-o repetindo a primeira letra de cada palavra, junto com um traço
    gago("preciso tirar dez") -> "p-preciso t-tirar d-dez"
    gago("eu deveria ter estudado mais") -> "e-eu d-deveria t-ter e-estudado m-mais"
    '''
    # if ' ' in texto:
    #     texto1 = texto.replace(' ', '-')
    #
    #
    #
    # texto_novo = texto[0] + texto1 + texto[1] + texto1
    #
    # return texto_novo



def saudacao(nome,hora) :
    '''Escreva uma saudação para a pessoa, dependendo do horário do dia:
    Entre 5 e 12: dia
    Entre 12 e 18: tarde
    Entre 18 e 5: noite'''


def rosquinhas(n) :
    '''
    Para um inteiro n retorna uma string na forma '<n> rosquinhas'
    onde n é o valor passado como argumento.
    Caso n >= 10 devo retornar 'muitas' em lugar do número.
    rosquinhas(5) -> '5 rosquinhas'
    rosquinhas(23) -> 'muitas rosquinhas'
    '''


def pontas(s) :
    '''
    Dada uma string s, retorna uma string com as duas primeiras e as duas
    últimas letras da string original s
    Assim 'palmeiras' retorna 'paas'
    No entanto, se a string tiver menos que 2 letras, retorna uma string vazia
    '''


def fixa_primeiro(s) :
    '''
    Dada uma string s, retorna uma string onde todas as ocorrências
    do primeiro caracter são trocados por '*', exceto para o primeiro
    Assim 'abacate' retorna 'ab*c*te'
    Dica: use s.replace(stra, strb)
    '''


def nomes_pontas(n) :
    '''Dada uma string n contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome, em
    maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO MENDES"
    '''


def nomes_pontas_e_iniciais_do_meio(n) :
    '''Dada uma string n contendo o nome completo de uma pessoa,
    retorne uma nova string contendo o primeiro e o último nome,
    e as inciais dos nomes do meio, em maiúsculas.
    "Marco André Lopes Mendes" -> "MARCO A L MENDES"
    '''


def mistura2(a,b) :
    '''
    Sejam duas strings a e b
    Retorno uma string '<a> <b>' separada por um espaço
    com as duas letras trocadas de cada string
      'mix', pod' -> 'pox mid'
      'dog', 'dinner' -> 'dig donner'
    '''


def busca(frase,palavra) :
    '''
    Verifique quantas ocorrências de uma palavra há numa frase
    frase = 'ana e mariana gostam de banana'
    palavra = 'ana'
    busca ('ana e mariana gostam de banana', 'ana') == 4
    '''


def tres_maiusculas(texto) :
    '''Encontre a primeira ocorrência de 3 letras maiúsculas consecutivas
    no texto.
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
    print('número invertido')
    test(numero_invertido(1),1)
    test(numero_invertido(0),0)
    test(numero_invertido(10),1)
    test(numero_invertido(1111),1111)
    test(numero_invertido(00000),0)
    test(numero_invertido(1234),4321)
    test(numero_invertido(2013),3102)
    test(numero_invertido(20130711),11703102)

    print('Gago')
    test(gago('O'),'O-O')
    test(gago('O O'),'O-O O-O')
    test(gago('Oi'),'O-Oi')
    test(gago('beleza?'),'b-beleza?')
    test(gago('tudo bem?'),'t-tudo b-bem?')
    test(gago('nota dez!'),'n-nota d-dez!')
    test(gago('preciso tirar dez'),'p-preciso t-tirar d-dez')
    test(gago('eu deveria ter estudado mais'),'e-eu d-deveria t-ter e-estudado m-mais')

    print('Saudação')
    test(saudacao('Jorge',4),'Boa noite Jorge')
    test(saudacao('Jorge',5),'Bom dia Jorge')
    test(saudacao('Jorge',11),'Bom dia Jorge')
    test(saudacao('Maria',12),'Boa tarde Maria')
    test(saudacao('Maria',18),'Boa tarde Maria')
    test(saudacao('Suzana',19),'Boa noite Suzana')
    test(saudacao('Suzana',24),'Boa noite Suzana')
    test(saudacao('Bruna',2),'Boa noite Bruna')

    print('rosquinhas')
    test(rosquinhas(4),'4 rosquinhas')
    test(rosquinhas(9),'9 rosquinhas')
    test(rosquinhas(10),'muitas rosquinhas')
    test(rosquinhas(99),'muitas rosquinhas')

    print('pontas')
    test(pontas('palmeiras'),'paas')
    test(pontas('algoritmos'),'alos')
    test(pontas('a'),'')
    test(pontas('xyz'),'xyyz')

    print('fixa_primeiro')
    test(fixa_primeiro('abacate'),'ab*c*te')
    test(fixa_primeiro('babble'),'ba**le')
    test(fixa_primeiro('aardvark'),'a*rdv*rk')
    test(fixa_primeiro('google'),'goo*le')
    test(fixa_primeiro('donut'),'donut')

    print('mistura2')
    test(mistura2('mix','pod'),'pox mid')
    test(mistura2('dog','dinner'),'dig donner')
    test(mistura2('gnash','sport'),'spash gnort')
    test(mistura2('pezzy','firm'),'fizzy perm')

    print('nomes_pontas')
    test(nomes_pontas('Marco André Lopes Mendes'),'MARCO MENDES')
    test(nomes_pontas('Paulo César de Oliveira'),'PAULO OLIVEIRA')
    test(nomes_pontas('Fernando José Braz'),'FERNANDO BRAZ')
    test(nomes_pontas('Eduardo da Silva'),'EDUARDO SILVA')

    print('nomes_pontas')
    test(nomes_pontas_e_iniciais_do_meio('Marco André Lopes Mendes'),'MARCO A L MENDES')
    test(nomes_pontas_e_iniciais_do_meio('Paulo César de Oliveira'),'PAULO C OLIVEIRA')
    test(nomes_pontas_e_iniciais_do_meio('Fernando José Braz'),'FERNANDO J BRAZ')
    test(nomes_pontas_e_iniciais_do_meio('Eduardo da Silva'),'EDUARDO SILVA')

    print('busca')
    test(busca('ana e mariana gostam de banana','ana'),4)
    test(busca('uma arara ou duas araras','ara'),4)

    print('3 maiúsculas')
    test(tres_maiusculas('MMM'),0)
    test(tres_maiusculas('sMGH'),1)
    test(tres_maiusculas('sKKKsdddfffGGGkkklmn'),1)
    test(tres_maiusculas('ssdddfffGGGkkklmn'),8)
    test(tres_maiusculas('ssdddfffgggkkklmn'),None)


if __name__ == '__main__' :
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total,acertos,
                                                        total - acertos,float(acertos * 10) / total))
    if total == acertos :
        print("Parabéns, seu programa rodou sem falhas!")