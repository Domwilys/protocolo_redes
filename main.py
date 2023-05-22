import socket

try:

    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udpSocket.bind(('10.0.23.107', 10101))

    print('Servidor conectado')

    while(True):

        bytesClient = udpSocket.recvfrom(2048)
        message = bytesClient[0]
        address = bytesClient[1]

        m = message.decode()

        if(m == 'y' or m == 'Y'):

            contagemMsg = 'ok'
            contagem = str.encode(contagemMsg)
            udpSocket.sendto(contagem, address)

            print(f'Confirmação do jogador concedida')
            
        print(m)

except:

    print('Não foi possível conectar-se ao servidor')