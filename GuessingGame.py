import random
import math

def JogoDeAdivinacao():
    print("Selecione o intervalo: ")
    
    minimo = int(input("Mínimo: "))
    maximo = int(input("Máximo: "))
    
    numeroSorteado = random.randrange(minimo, maximo)
    
    tentativas = math.log(maximo - minimo + 1, 2)//1
    
    while tentativas != 0 :
        chute = int(input("\nChute um número: "))
        
        if chute == numeroSorteado:
            print("\n Parabéns Você Ganhou\n")
            break
        else:
            if chute > numeroSorteado:
                print("\nTente novamente! Você adivinhou muito alto\n")
            else:
                print("\nTente novamente! Você adivinhou muito pequeno\n")
                
        tentativas -= 1
        print("Você tem {} tentativas".format(tentativas//1))
    
    if tentativas == 0 :
                print("\n Infelizmente, Você Perdeu\nExcedeu o Número de Tentativas")
                
JogoDeAdivinacao()