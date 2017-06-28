__author__ = 'fernando.ormonde'




import random as rd

a = rd.randint(0, 2)
b = rd.randint(0, 2)
lista=['pedra', 'papel', 'tesoura']

print lista[a]
print lista[b]

jogada1 = lista[a]
jogada2 = lista[b]

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



print jokenpo(jogada1, jogada2)
