import utils

HOST = utils.setAny('127.0.0.1')
PORT = utils.setAny(5001)
SERVER_PATH = utils.getPathStr(HOST, PORT)
BUFFER_SIZE = utils.setAny(1024)
FAMILIA = utils.getFamilia("IPV4")
TIPO_DE_SOCKET = utils.getTipoDeSocket("TCP")

def loop_servidor(socket_servidor):
    while True:
        socket_cliente, endereco_cliente = utils.aceitarConexao(socket_servidor)
        utils.log("[🤝 loop_servidor(): Conexão aceita de " + utils.getPathStr(endereco_cliente[0], endereco_cliente[1]) + "]")
        dados = utils.receberDados(socket_cliente, BUFFER_SIZE)
        utils.log("[📨 loop_servidor(): Dados recebidos de " + utils.getPathStr(endereco_cliente[0], endereco_cliente[1]) + " : " + utils.decodificarDados(dados) + "]")
        socket_cliente.close()

def colocarServidorNaEscuta(socket_servidor):
    utils.escutar(socket_servidor, 5)
    utils.log("[👂 colocarServidorNaEscuta(): Servidor TCP escutando em " + SERVER_PATH + "]")

def iniciarServidor():
    socket_servidor = utils.instanciarSocket(FAMILIA, TIPO_DE_SOCKET)
    utils.configurarSocket(socket_servidor, HOST, PORT)
    utils.log("[📡 iniciarServidor(): Servidor TCP configurado em " + SERVER_PATH + "]")

    return socket_servidor

socket_servidor = iniciarServidor()
colocarServidorNaEscuta(socket_servidor)
loop_servidor(socket_servidor)