import socket
import threading

class Client:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.host, self.port))
        print(f'Conectado ao servidor em {self.host}:{self.port}')

        # Configuração do nome de usuário
        self.name = input("Digite seu nome: ")
        self.client_socket.send(self.name.encode('utf-8'))

    def send_message(self):
        while True:
            target_name = input("Digite o nome do destinatário: ")
            message = input("Digite a mensagem: ")
            self.client_socket.send(f"{target_name}:{message}".encode('utf-8'))

    def receive_message(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                print(message)
            except:
                print("Conexão com o servidor perdida.")
                break

    def start(self):
        # Inicia threads para enviar e receber mensagens
        threading.Thread(target=self.send_message).start()
        threading.Thread(target=self.receive_message).start()

if __name__ == "__main__":
    client = Client()
    client.start()