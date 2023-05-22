import socket
import time

def contagemRegressiva():

    contagem = 6

    while contagem > 1:
        print(contagem-1)
        time.sleep(1)
        contagem-=1

def marchas(username):

    inicioCorrida = round(float(time.time()%60), 2)

    marcha = 1

    while marcha < 5:

        print('Acelerando\n')
        time.sleep(marcha + 3)
        marchaComando = input('Pressione <Q> e <ENTER> para passar a marcha: ')

        if(marchaComando == 'q' or marchaComando == 'Q'):

            marcha+=1
            print(f"Marcha {marcha}!")

        if(marcha == 5):

            time.sleep(8)
            marcha = 6

            fimCorrida = round(float(time.time()%60), 2)
            resultado = round((fimCorrida - inicioCorrida), 2)

            chegada  = f'Jogador <{username}> alcançou a linha de chegada em {abs(resultado)} segundos'
            chegadaSend = str.encode(chegada)
            udpScoket.sendto(chegadaSend, portServer)

            print(chegada)

try:

    while True: 

        udpScoket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        portServer = ('10.0.30.208', 10101)

        msgStart = input('Pronto?(Pressione a tecla <Y> para confirmar) ')
        if(msgStart == 'y' or msgStart == 'Y'):

            msgStartSend = str.encode(msgStart)
            udpScoket.sendto(msgStartSend, portServer)
        else:

            exit()


        username = input('Digite seu Username: ')

        msgServer = udpScoket.recvfrom(2048)
        msg = msgServer[0].decode()

        if(msg == 'ok'):

            print('Verificação do servidor realizada, o jogo pode iniciar')
            contagemRegressiva()
            print('Marcha 1!')
            marchas(username)
            exit()

except:

    print('Game Over!')
