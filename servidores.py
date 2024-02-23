class ServidorTCP():
    def __init__(self, host, porta, familia):
        self.host = host
        self.porta = porta
        self.familia = familia

    def __str__(self):
        return "[servidor TCP ({}) configurado para a máquina {} e porta {}]".format(self.familia, self.host, self.porta)

s = ServidorTCP('127.0.0.1', 1235, "IPV4")
print(s)