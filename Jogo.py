#Jogo da Adivinhação
#Gabriel Alves 
#Versão 1.0
#UMC
import random
import os

Tit='''
=====================
 JOGO DA ADIVINHAÇÃO
=====================
'''
Inst= '''
O objetivo do jogo é adivinhar o número que eu escolhientre 1 e 100. 
A cada tentativa, eu vou te dizer se o número é maior ou menor.
Vamos começar!'''
#Entrada
print (Tit)
print(Inst)

#Entrada de dados
nm= input('Entre com seu nome para Inciar: ')
os.system ('cls')
ns= random.randint(1, 100)#sorteia o numero secreto de 1 à 100 
tent= 0 # inicia contador de tentativas 

#Função principal loop do jogo
while True:
    print(f"Jogador: {nm} | Tentativas: {tent}" )
    # Entrada
    try:
        chute = int(input('Digite seu Palpite: '))
    except ValueError:
        os.system ('cls')
        print("Oops! Isso não é um número. Tente novamente.")
        continue

    # Processamento
    tent += 1

    # Saida
    os.system('cls')
    if chute < ns:
        print(f"Que pena, {nm}! O número {chute} é muito baixo")
    elif chute > ns:
        print(f"Quase lá, {nm}! O número {chute} é muito alto.")
    else:
        # Saída da mensagem de vitória personalizada
        print(f"BOA, {nm.upper()}! Você acertou o número {ns} em {tent} tentativas.")
        break

