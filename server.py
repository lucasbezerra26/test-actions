import socket
import threading


class Server:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        self.clients = {}
        self.prohibited_words = ["palavra1", "palavra2"]
        print(f'Servidor iniciado em {self.host}:{self.port}')

    def handle_message(self, message):
        """Aplica censura a palavras impróprias."""
        for word in self.prohibited_words:
            if word in message:
                message = message.replace(word, "***")
        return message

    def handle_client(self, client_socket, client_name):
        self.clients[client_name] = client_socket
        print(f'{client_name} conectado.')

        while True:
            try:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break

                # Extrair destinatário e mensagem
                target_name, message = data.split(":", 1)
                message = self.handle_message(message)  # Aplica censura

                if target_name in self.clients:
                    target_socket = self.clients[target_name]
                    self.send(target_socket, f"{client_name}: {message}")
                else:
                    self.send(client_socket, "Destinatário não encontrado.")

            except Exception as e:
                print(f"Erro com {client_name}: {e}")
                break

        del self.clients[client_name]
        client_socket.close()
        print(f'{client_name} desconectado.')

    def send(self, client_socket, message):
        """Envia uma mensagem para o cliente."""
        client_socket.send(message.encode('utf-8'))

    def start(self):
        print('Aguardando conexões...')
        while True:
            client_socket, _ = self.server_socket.accept()
            client_socket.send("Digite seu nome: ".encode('utf-8'))
            client_name = client_socket.recv(1024).decode('utf-8')

            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, client_name))
            client_thread.start()


if __name__ == "__main__":
    server = Server()
    server.start()