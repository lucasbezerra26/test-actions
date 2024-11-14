import pytest
from unittest.mock import MagicMock
from server import Server
from unittest import mock

class TestServer:
    def test_handle_message(self, server):
        """Testa a censura de palavras impróprias."""
        message = "Esta é uma mensagem com palavra1 e palavra2."
        expected_message = "Esta é uma mensagem com *** e ***."
        censored_message = server.handle_message(message)
        assert censored_message == expected_message

    @pytest.mark.parametrize("message, expected_message", [
        ("Esta é uma mensagem com palavra1", "Esta é uma mensagem com ***"),
        ("Não há palavras proibidas", "Não há palavras proibidas")
    ])
    def test_handle_message_parametrized(self, server, message, expected_message):
        """Testa censura com vários casos usando parametrização."""
        censored_message = server.handle_message(message)
        assert censored_message == expected_message

    @mock.patch.object(Server, 'send')
    def test_send_message(self, mock_send, server):
        """Testa o envio de uma mensagem para um cliente."""
        client_socket = MagicMock()
        server.send(client_socket, "Mensagem de teste")
        assert mock_send.called == False
