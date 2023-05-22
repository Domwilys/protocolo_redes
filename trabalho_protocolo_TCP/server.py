import threading
import socket

clientes = []

def main():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:

        server.bind(('10.0.30.208', 10101))
        server.listen(2)
        print("Servidor conectado")

    except:

        print('\nNão foi possível iniciar o servidor.\n')
        exit()
    
    while True:

        cliente, addr = server.accept()
        clientes.append(cliente)

        thread = threading.Thread(target=confirmacao, args=[cliente])
        thread.start()

def confirmacao(cliente):

    while True:

        try:

            msgRecv = cliente.recv(2048)
            msg = msgRecv.decode()
            print(msg)
            
            if(msg == 'y' or msg == 'Y'):
                
                print('Confirmação do jogador realizada')
                
        except:

            deleteClient(cliente)

def deleteClient(cliente):

    clientes.remove(cliente)

main()