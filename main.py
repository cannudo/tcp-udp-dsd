import utils

def testeJson():
    dados = {"alunos": []}
    new = {"matrícula": "1", "nome": "João"}
    dados["alunos"].append(new)

def servidorTcp():
    HOST = utils.setAny('127.0.0.1')
    PORT = utils.setAny(5000)
    BUFFER_SIZE = utils.setAny(1024)
    FAMILIA = utils.getFamilia("IPV4")
    TIPO_DE_SOCKET = utils.getTipoDeSocket("TCP")
    socket_servidor = utils.instanciarSocket(FAMILIA, TIPO_DE_SOCKET)
    utils.configurarSocket(socket_servidor, HOST, PORT)
    utils.configurarEscuta(socket_servidor, 1)
    utils.log("[🔊] TCP escutando em " + utils.getPathStr(HOST, PORT))

def servidorUdp():
    HOST = utils.setAny('127.0.0.1')
    PORT = utils.setAny(5000)
    BUFFER_SIZE = utils.setAny(1024)
    FAMILIA = utils.getFamilia("IPV4")
    TIPO_DE_SOCKET = utils.getTipoDeSocket("UDP")
    socket_servidor = utils.instanciarSocket(FAMILIA, TIPO_DE_SOCKET)
    utils.configurarSocket(socket_servidor, HOST, PORT)
    utils.log("[🔊] UDP escutando em " + utils.getPathStr(HOST, PORT))

servidorTcp()
servidorUdp()