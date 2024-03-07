import utils
import socket

class ServidorTCP():
    def configurarEnderecoDoServidor(self, maquina, porta):
        endereco = (maquina, porta)
        self.socket_servidor.bind(endereco)
    
    def instanciarSocket(self, familia):
        familia_de_sockets = utils.getFamilia(familia)
        instancia = socket.socket(familia_de_sockets, socket.SOCK_STREAM)
        return instancia

    def __init__(self, familia, maquina, porta):
        self.familia = familia
        self.maquina = maquina
        self.porta = porta
        self.socket_servidor = self.instanciarSocket(self.familia)
        self.socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.configurarEnderecoDoServidor(self.maquina, self.porta)
        

        
s = ServidorTCP("IPV4", 'localhost', 8082)
print(s)