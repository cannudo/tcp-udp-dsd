import socket

def log(mensagem):
    print(mensagem)

def aguardar_enter():
    input()
    log("[✅ OK]")

def setAny(foo):
    return foo

def getPathStr(host, porta):
    return str("{}:{}".format(host, porta))

def getFamilia(tipo_de_endereco = "IPV4"):
    if tipo_de_endereco == "IPV4":
        retorno = socket.AF_INET
    elif tipo_de_endereco == "IPV6":
        retorno = socket.AF_INET6
    elif tipo_de_endereco == "LOCAL":
        retorno = socket.AF_UNIX

    return retorno

def getTipoDeSocket(tipo_de_socket = "TCP"):
    if tipo_de_socket == "TCP":
        retorno = socket.SOCK_STREAM
    elif tipo_de_socket == "UDP":
        retorno = socket.SOCK_DGRAM
    elif tipo_de_socket == "RAW":
        retorno = socket.SOCK_RAW
    elif tipo_de_socket == "SEQPACKET":
        retorno = socket.SOCK_SEQPACKET
    elif tipo_de_socket == "RDM":
        retorno = socket.SOCK_RDM

    return retorno

def instanciarSocket(familia, tipo_de_socket):
    return socket.socket(familia, tipo_de_socket)

def configurarSocket(socket, host, porta):
    socket.bind((host, porta))

def configurarEscuta(socket, hosts):
    socket.listen(hosts)

def aceitarConexao(socket):
    return socket.accept()

def receberDados(socket, tamanho_do_buffer = 1024, tipo_de_socket = socket.SOCK_STREAM):
    if tipo_de_socket == socket.SOCK_STREAM:
        return socket.recv(tamanho_do_buffer)
    else:
        return socket.recvfrom(tamanho_do_buffer)
    
def decodificarDados(dados):
    return dados.decode("utf-8")

def encodificarDados(dados):
    return dados.encode("utf-8")

def enviarDados(socket, dados, tipo_de_socket):
    if tipo_de_socket == socket.SOCK_DGRAM:
        socket.sendto(dados)
    else:
        socket.send(dados)

def fecharSocket(socket):
    socket.close()

def conectarSocket(socket, host, porta):
    socket.connect((host, porta))

