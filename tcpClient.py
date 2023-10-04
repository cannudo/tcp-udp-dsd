import utils

SERVER_HOST = utils.setAny('127.0.0.1')
SERVER_PORT = utils.setAny(5001)
SERVER_PATH = utils.getPathStr(SERVER_HOST, SERVER_PORT)
BUFFER_SIZE = utils.setAny(1024)
FAMILIA = utils.getFamilia("IPV4")
TIPO_DE_SOCKET = utils.getTipoDeSocket("TCP")

print(FAMILIA)
print(TIPO_DE_SOCKET)

def loop_cliente(socket_cliente):
    while True:
        dados = 'dados'
        utils.enviarDados(socket_cliente, utils.encodificarDados(dados), TIPO_DE_SOCKET)
        utils.log("[📨 loop_cliente(): Dados enviados para " + SERVER_PATH + " : " + dados + "]")
        dados = utils.receberDados(socket_cliente, BUFFER_SIZE, TIPO_DE_SOCKET)
        utils.log("[📨 loop_cliente(): Dados recebidos de " + SERVER_PATH + " : " + utils.decodificarDados(dados) + "]")

def iniciarCliente():
    socket_cliente = utils.instanciarSocket(FAMILIA, TIPO_DE_SOCKET)
    utils.log("[📡 iniciarCliente(): Cliente TCP configurado em " + SERVER_PATH + "]")
    utils.conectarSocket(socket_cliente, SERVER_HOST, SERVER_PORT)
    utils.receberDados(socket_cliente, BUFFER_SIZE, TIPO_DE_SOCKET)

    return socket_cliente

socket_cliente = iniciarCliente()
loop_cliente(socket_cliente)