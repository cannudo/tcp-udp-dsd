import socket
import  utils

class ClienteTCP():
    def instanciarSocket(self, familia):
         familia_de_sockets = utils.getFamilia(familia)
         instancia = socket.socket(familia_de_sockets, socket.SOCK_STREAM)
         return instancia

    def __init__(self, familia, maquina_servidor, porta_servidor):
        self.familia = familia
        self.maquina_servidor = maquina_servidor
        self.porta_servidor = porta_servidor
        self.socket_cliente = self.instanciarSocket(self.familia)
        endereco_do_servidor = (self.maquina_servidor, self.porta_servidor)
        print("[🔌 tentando conectar à máquina %s ⏳]" % str(str(self.maquina_servidor) + ":" + str(self.porta_servidor)))
        try:
            self.socket_cliente.connect(endereco_do_servidor)
            print("[✅ conectado 🔗]")
        except ConnectionRefusedError:
            print("[❌ conexão recusada pelo servidor]")

        # TODO NÃO ACABOU BONITA

c = ClienteTCP("IPV4", 'localhost', 8082)
print(c)