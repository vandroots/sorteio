"""
Desenvolver um algoritmo que recebe o valor total de um prêmio e o 
nome de participantes (quantos o usuário quiser!). 

O algoritmo deve sortear o valor para todos os participantes sendo que o
prêmio mínimo deve respeitar ser 10% do total dividido pelo número de usuários.  
"""
from random import randint

participantes = []
premio = float(input("Qual é o prêmio? "))

while True:
    participante = input("Nome do participante ou [S]air: ")
    
    if(participante=="S"):
        break
    else:
        participantes.append({
                "nome":participante
        })

premio_minimo = (premio*0.1)/len(participantes)

resto_premio = premio*(1-0.1) #Desconto do prêmio minimo

for participante in participantes:
    participante["premio"] = premio_minimo

sorteado = randint(0,(len(participantes)-1)) #Sortear o vitorioso

participantes[sorteado]["premio"] = premio_minimo + resto_premio #Adicionar o resto do premio ao ganahador

for participante in participantes:
    print("Nome: "+str(participante["nome"]))
    print("Nome: "+str(participante["premio"]))
    print("-----------------------")