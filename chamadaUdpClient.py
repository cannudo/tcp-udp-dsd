import utils

HOST = '127.0.0.1'
PORTA = 1234
TIPO_DE_SOCKET = utils.getTipoDeSocket("UDP")
FAMILIA_DE_SOCKET = utils.getFamilia("IPV4")

socket_cliente = utils.instanciarSocket(FAMILIA_DE_SOCKET, TIPO_DE_SOCKET)

while True:
    mensagem = utils.encodificarDados("Testando conexão")
    utils.enviarDados(socket_cliente, mensagem, TIPO_DE_SOCKET, (HOST, PORTA))
    utils.aguardar_enter()