import utils
import socket

class ServidorTCP():
    def instanciarSocket(familia):
        familia_de_sockets = utils.getFamilia(familia)
        instancia = socket.socket(familia_de_sockets, socket.SOCK_STREAM)
        return instancia

    def __init__(self, familia, maquina, porta):
        self.familia = familia
        self.maquina = maquina
        self.porta = porta
        socket_servidor = self.instanciarSocket(self.familia)
        socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        endereco_do_servidor = (maquina, porta)
        
# Continuar