import utils

class ServidorTCP():
    def __init__(self, host, porta, familia):
        self.host = host
        self.porta = porta
        self.familia = familia

    def __str__(self):
        return "[servidor TCP ({}) configurado para a máquina {} e porta {}]".format(self.familia, self.host, self.porta)

    def start(self):
        server_socket = utils.instanciarSocket(utils.getFamilia(self.familia.upper()), utils.getTipoDeSocket("UDP"))
        utils.configurarSocket(server_socket, self.host, self.porta)

s = ServidorTCP('127.0.0.1', 1235, "IPV4")
print(s)
s.start()