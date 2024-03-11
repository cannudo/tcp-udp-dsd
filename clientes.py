import utils

class ClienteTCP():
    def __init__(self, host, porta, familia):
        self.host = host
        self.porta = porta
        self.familia = utils.getFamilia(familia)
        self.tipo = utils.getTipoDeSocket("TCP")
        self.escuta = utils.instanciarSocket(self.familia, self.tipo)

class ClienteUDP():
    def __init__(self, host, porta, familia):
        self.host = host
        self.porta = porta
        self.familia = utils.getFamilia(familia)
        self.tipo = utils.getTipoDeSocket("UDP")
        self.escuta = utils.instanciarSocket(self.familia, self.tipo)