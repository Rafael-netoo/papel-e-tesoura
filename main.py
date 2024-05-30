from classes.jogada import*
import random

desisao = 0
jogadorPonto = 0
computadorPonto = 0
escolha = 0
while(desisao != 2):
    pontosJogador = 0
    pontosComputador = 0
    jogadas = [1,2,3]
    print("**Pedra, Papel e Tesoura**")
    print("Menu:")
    print("1 - Começar Jogo")
    print("2 - Sair do jogo")
    decisao = int(input("Escolha (1 ou 2) : "))
    print(" ")
    nome = input("Digite o seu nome :")

    while(escolha != 4):
            escolha = int(input("Digite a sua jogada(1 - Pedra,2 - Papel, 3 - Tesoura, 4 - Sair):"))
            jogadaComputador = random.choice(jogadas)
            jogador = Jogada(nome,escolha)
            computador = Jogada("computador",jogadaComputador)

            if(jogador.jogada == computador.jogada):
                 print(" ")
                 print(f"{jogador.nome}: {jogador.jogada}")
                 print(f"{computador.nome}: {computador.jogada}")
                 print("Empate")

            elif(jogador.jogada == 1 and computador.jogada == 2):
                 print(" ")
                 print(f"{jogador.nome}: Pedra")
                 print(f"{computador.nome}: Papel")
                 computadorPonto+=1
                 print(f"{computador.nome}: Ganhou")
                 print(f'Pontos {jogador.nome}:{jogadorPonto} ||{computador.nome}:{computadorPonto}')

            elif(jogador.jogada == 1 and computador.jogada == 3):
                 print(" ")
                 print(f"{jogador.nome}: Pedra")
                 print(f"{computador.nome}: Tesoura")
                 jogadorPonto+=1
                 print(f"{jogador.nome}: Ganhou")
                 print(f'Pontos {jogador.nome}:{jogadorPonto} ||{computador.nome}:{computadorPonto}')    

            elif(jogador.jogada == 2 and computador.jogada == 1):
                 print(" ")
                 print(f"{jogador.nome}: {jogador.jogada}")
                 print(f"{computador.nome}: {computador.jogada}")
                 jogadorPonto+=1
                 print(f"{jogador.nome}: Ganhou")
                 print(f'Pontos {jogador.nome}:{jogadorPonto} ||{computador.nome}:{computadorPonto}')
            
            elif(jogador.jogada == 2 and computador.jogada == 3):
                 print(" ")
                 print(f"{jogador.nome}: Papel")
                 print(f"{computador.nome}: Tesoura")
                 computadorPonto+=1
                 print(f"{computador.nome}: Ganhou")
                 print(f'Pontos {jogador.nome}:{jogadorPonto} ||{computador.nome}:{computadorPonto}')

            elif(jogador.jogada == 3 and computador.jogada == 1):
                 print(" ")
                 print(f"{jogador.nome}: Tesoura")
                 print(f"{computador.nome}: Pedra")
                 computadorPonto+=1
                 print(f"{computador.nome}: Ganhou")
                 print(f'Pontos {jogador.nome}:{jogadorPonto} ||{computador.nome}:{computadorPonto}')

            elif(jogador.jogada == 3 and computador.jogada == 2):
                 print(" ")
                 print(f"{jogador.nome}: Tesoura")
                 print(f"{computador.nome}: Papel")
                 jogadorPonto+=1
                 print(f"{jogador.nome}: Ganhou")
                 print(f'Pontos {jogador.nome}:{jogadorPonto} ||{computador.nome}:{computadorPonto}')
            else:
                 print(" ")
                 print("Jogada inválida")
            
            


     
     

