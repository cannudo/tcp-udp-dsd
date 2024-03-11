import utils

HOST = '127.0.0.1'
PORTA = 1234
TIPO_DE_SOCKET = utils.getTipoDeSocket("UDP")
FAMILIA_DE_SOCKET = utils.getFamilia("IPV4")

socket_servidor = utils.instanciarSocket(FAMILIA_DE_SOCKET, TIPO_DE_SOCKET)
utils.configurarSocket(socket_servidor, HOST, PORTA)

while True:
    mensagem, cliente = utils.receberDados(socket_servidor, 1024, TIPO_DE_SOCKET)
    print(utils.decodificarDados(mensagem))