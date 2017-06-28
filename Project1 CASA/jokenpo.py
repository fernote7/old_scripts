__author__ = 'fernando.ormonde'



import random as rd

print rd.randint(0, 2)


pedra= 'pedra'
tesoura = 'tesoura'
papel = 'papel'


def jokenpo(jogada1, jogada2):
    if jogada1 == pedra and jogada2 == tesoura:
        return 'Jogador 1 vence com %s' %(jogada1)

    elif jogada1 == pedra and jogada2 == papel:
        return 'Jogador 2 vence com %s' %(jogada2)

    elif jogada1 == papel and jogada2 == pedra:
        return 'Jogador 1 vence com %s' %(jogada1)

    elif jogada1 == papel and jogada2 == tesoura:
        return 'Jogador 2 vence com %s' %(jogada2)

    elif jogada1 == tesoura and jogada2 == papel:
        return 'Jogador 1 vence com %s' %(jogada1)

    elif jogada1 == tesoura and jogada2 == pedra:
        return 'Jogador 2 vence com %s' %(jogada2)
    else:
        return 'Empate'

print jokenpo(pedra, tesoura)
print jokenpo(pedra, papel)

print jokenpo(pedra, pedra)
print jokenpo(pedra, tesoura)

print jokenpo(tesoura, tesoura)
print jokenpo(tesoura, papel)