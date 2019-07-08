#!/bin/env python3
# coding: utf-8
# Marco André <marcoandre@gmail.com>
# Lista de exercícios 8c - revisão

def comeco_ou_fim_6(nums) :
    '''
    Verifica se 6 é o primeiro ou último elemento da lista nums.
    comeco_ou_fim_6([1, 2, 6]) -> True
    comeco_ou_fim_6([6, 1, 2, 3]) -> True
    comeco_ou_fim_6([3, 2, 1]) -> False
    '''
    if nums[0] == 6 or nums[-1] == 6:
        return True
    else:
        return False

def inicio_fim_igual(nums) :
    '''
    Retorna True se a lista nums possui pelo menos um elemento
    e o primeiro elemento é igual ao último
    inicio_fim_igual([1, 2, 3]) -> False
    inicio_fim_igual([1, 2, 3, 1]) -> True
    inicio_fim_igual([1, 2, 1]) -> True
    '''
    if nums == []:
        return False
    elif nums[0] == nums[-1]:
        return True
    else:
        return False

def extremidades_iguais(a,b) :
    '''
    Dada duas listas a e b verifica se os dois primeiros são
    iguais ou os dois últimos são iguais.
    Suponha que as listas tenham pelo menos um elemento.
    extremidades_iguais([1, 2, 3], [7, 3]) -> True
    extremidades_iguais([1, 2, 3], [7, 3, 2]) -> False
    extremidades_iguais([1, 2, 3], [1, 3]) -> True
    '''
    if a[0] == b[0] or b[-1] == a[-1]:
        return True
    else:
        return False



def maior_ponta(nums) :
    '''
    Dada uma lista não vazia, cria uma nova lista onde todos
    os elementos são o maior das duas pontas
    obs.: não é o maior de todos os itens, mas entre as duas pontas
    maior_ponta([1, 2, 3]) -> [3, 3, 3]
    maior_ponta([1, 3, 2]) -> [2, 2, 2]
    '''
    nova_lista = []
    if nums[0] > nums[-1]:
        nova_lista.append(nums[0])
        nova_lista.append(nums[0])
        nova_lista.append(nums[0])
    elif nums[0] < nums[-1]:
        nova_lista.append(nums[-1])
        nova_lista.append(nums[-1])
        nova_lista.append(nums[-1])
    else:
        nova_lista.append(nums[0])
        nova_lista.append(nums[0])
        nova_lista.append(nums[0])

    return nova_lista



def soma_2_primeiros(nums) :
    '''
    Dada uma lista de inteiros de qualquer tamanho retorna a soma dos
    dois primeiros elementos.
    Se a lista tiver menos de dois elementos, soma o que for possível.
    '''
    if nums == []:
        return 0
    elif len(nums) < 2:
        return nums[0]
    else:
        return nums[0] + nums[1]

def meio_do_caminho(a,b) :
    '''
    sejam duas listas de inteiros a e b
    retorna uma lista de tamanho 2 contendo os elementos do
    meio de a e b, suponha que as listas tem tamanho ímpar
    meio_do_caminho([1, 2, 3], [4, 5, 6]) -> [2, 5]
    meio_do_caminho([7, 7, 7], [3, 8, 0]) -> [7, 8]
    meio_do_caminho([5, 2, 9], [1, 4, 5]) -> [2, 4]
    '''


## Área de testes: só mexa aqui se souber o que está fazendo!
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
    print('comeco_ou_fim_6')
    test(comeco_ou_fim_6([1,2,6]),True)
    test(comeco_ou_fim_6([6,1,2,3]),True)
    test(comeco_ou_fim_6([3,2,1]),False)
    test(comeco_ou_fim_6([3,6,1]),False)
    test(comeco_ou_fim_6([3,6]),True)
    test(comeco_ou_fim_6([6]),True)
    test(comeco_ou_fim_6([3]),False)

    print('inicio_fim_igual')
    test(inicio_fim_igual([1,2,3]),False)
    test(inicio_fim_igual([1,2,3,1]),True)
    test(inicio_fim_igual([1,2,1]),True)
    test(inicio_fim_igual([7]),True)
    test(inicio_fim_igual([]),False)
    test(inicio_fim_igual([7,7]),True)

    print('extremidades_iguais')
    test(extremidades_iguais([1,2,3],[7,3]),True)
    test(extremidades_iguais([1,2,3],[7,3,2]),False)
    test(extremidades_iguais([1,2,3],[1,3]),True)
    test(extremidades_iguais([1,2,3],[1]),True)
    test(extremidades_iguais([1,2,3],[2]),False)

    print('maior_ponta')
    test(maior_ponta([1,2,3]),[3,3,3])
    test(maior_ponta([11,5,9]),[11,11,11])
    test(maior_ponta([2,11,3]),[3,3,3])
    test(maior_ponta([11,3,3]),[11,11,11])
    test(maior_ponta([3,11,11]),[11,11,11])
    test(maior_ponta([2,2,2]),[2,2,2])
    test(maior_ponta([2,11,2]),[2,2,2])
    test(maior_ponta([0,0,1]),[1,1,1])

    print('soma_2_primeiros')
    test(soma_2_primeiros([1,2,3]),3)
    test(soma_2_primeiros([1,1]),2)
    test(soma_2_primeiros([1,1,1,1]),2)
    test(soma_2_primeiros([1,2]),3)
    test(soma_2_primeiros([1]),1)
    test(soma_2_primeiros([]),0)
    test(soma_2_primeiros([4,5,6]),9)
    test(soma_2_primeiros([4]),4)

    print('meio_do_caminho')
    test(meio_do_caminho([1,2,3],[4,5,6]),[2,5])
    test(meio_do_caminho([7,7,7],[3,8,0]),[7,8])
    test(meio_do_caminho([5,2,9],[1,4,5]),[2,4])
    test(meio_do_caminho([1,9,7],[4,8,8]),[9,8])
    test(meio_do_caminho([1,2,3],[3,1,4]),[2,1])
    test(meio_do_caminho([1,2,3,4,5],[2,3,5,4,1]),[3,5])


if __name__ == '__main__' :
    main()
    print("\n%d Testes, %d Ok, %d Falhas: Nota %.1f" % (total,acertos,
                                                        total - acertos,float(acertos * 10) / total))
    if total == acertos :
        print("Parabéns, seu programa rodou sem falhas!")