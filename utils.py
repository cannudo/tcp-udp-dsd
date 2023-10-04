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
    if tipo_de_endereco.upper() == "IPV4":
        retorno = socket.AF_INET
    elif tipo_de_endereco.upper() == "IPV6":
        retorno = socket.AF_INET6
    elif tipo_de_endereco.upper() == "LOCAL":
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

def configurarSocket(socket_, host, porta):
    socket_.bind((host, porta))

def escutar(socket_, hosts):
    socket_.listen(hosts)

def aceitarConexao(socket_):
    return socket_.accept()

def receberDados(socket_, tamanho_do_buffer = 1024, tipo_de_socket = socket.SOCK_STREAM):
    if tipo_de_socket == socket.SOCK_STREAM:
        return socket_.recv(tamanho_do_buffer)
    else:
        return socket_.recvfrom(tamanho_do_buffer)
    
def decodificarDados(dados):
    return dados.decode("utf-8")

def encodificarDados(dados):
    return dados.encode("utf-8")

def enviarDados(socket_, dados, tipo_de_socket):
    if tipo_de_socket == socket.SOCK_DGRAM:
        socket_.sendto(dados)
    else:
        socket_.send(dados)

def enviarDadosEmBroadcast(socket_, dados, broadcast_host, porta):
    log("[📨] Enviados para " + getPathStr(broadcast_host, porta) + " : " + decodificarDados(dados))
    socket_.sendto(dados, (broadcast_host, porta))

def ativarBroadcast(socket_):
    socket_.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

def fecharSocket(socket_):
    socket_.close()

def conectarSocket(socket_, host, porta):
    socket_.connect((host, porta))
