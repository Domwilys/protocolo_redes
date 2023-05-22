import threading
import socket
import time

def main():
    
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        cliente.connect(('10.0.30.208', 10101))
        print("Cliente conectado")

    except:

        print('\nNão foi possível conectar-se ao servidor.\n')
        exit()
    
    username = input("Digite seu nickname: ")
    print("\nConectado.")

    thread = threading.Thread(target=dragRace, args=[cliente, username])

    thread.start()

def marchas(cliente, username):

    inicioCorrida = round(float(time.time()%60), 2)

    marcha = 1

    while marcha < 5:

        print('Acelerando\n')
        time.sleep(marcha + 3)
        marchaComando = input('Pressione <Q> e <ENTER> para passar a marcha: ')

        if(marchaComando == 'q' or marchaComando == 'Q'):

            marcha+=1
            print(f"Marcha {marcha}!")

        else:

            print('Game Over!')
            exit()

        if(marcha == 5):

            time.sleep(8)
            marcha = 6

            fimCorrida = round(float(time.time()%60), 2)
            resultado = round((fimCorrida - inicioCorrida), 2)

            chegada  = f'Jogador <{username}> alcançou a linha de chegada em {abs(resultado)} segundos'
            cliente.send(f'{chegada}'.encode('utf-8'))

            print(chegada)

def contagemRegressiva():

    contagem = 6

    while contagem > 1:
        
        print(contagem-1)
        time.sleep(1)
        contagem-=1
    
def dragRace(cliente, username):
    
    while True:

        try:

            msg = input('Pronto? ')

            if (msg == 'y') or (msg == 'Y'):

                cliente.send(f'{msg}'.encode('utf-8'))
                contagemRegressiva()
                marchas(cliente, username)

            else:

                exit()

        except:

            print('Game Over!')
            exit()

main()

