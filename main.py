import socket, utils

def servidorTcp():
    HOST = utils.setAny('127.0.0.1')
    PORT = utils.setAny(5000)
    BUFFER_SIZE = utils.setAny(1024)
    FAMILIA = utils.getFamilia("IPV4")
    TIPO_DE_SOCKET = utils.getTipoDeSocket("TCP")
    socket = utils.instanciarSocket(FAMILIA, TIPO_DE_SOCKET)
    utils.configurarSocket(socket, HOST, PORT)
    utils.configurarEscuta(socket, 1)
    utils.log("[🔊] TCP escutando em " + utils.getPathStr(HOST, PORT))

def servidorUdp():
    HOST = utils.setAny('127.0.0.1')
    PORT = utils.setAny(5000)
    BUFFER_SIZE = utils.setAny(1024)
    FAMILIA = utils.getFamilia("IPV4")
    TIPO_DE_SOCKET = utils.getTipoDeSocket("UDP")
    socket = utils.instanciarSocket(FAMILIA, TIPO_DE_SOCKET)
    utils.configurarSocket(socket, HOST, PORT)
    utils.log("[🔊] UDP escutando em " + utils.getPathStr(HOST, PORT))

servidorTcp()
servidorUdp()