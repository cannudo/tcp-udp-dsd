import utils

class ServidorTCP():
    def rodar(self):
        if self.escuta:
            cliente, endereco = utils.aceitarConexao(self.escuta)
            mensagem = utils.receberDados(cliente)
            utils.fecharSocket(cliente)
        else:
            print("Socket não conectado.")

    def configurar(self):
        server_socket = utils.instanciarSocket(self.familia, self.tipo)
        utils.configurarSocket(server_socket, self.host, self.porta)
        print("[PAREI AQUI LINHA 15]")
        utils.escutar(server_socket, 1)
        return server_socket

    def __init__(self, host, porta, familia):
        self.host = host
        self.porta = porta
        self.familia = utils.getFamilia(familia.upper())
        self.tipo = utils.getTipoDeSocket("TCP")
        self.escuta = self.configurar()


class ServidorUDP():
    def escutar(self):
        mensagem, endereco = utils.receberDados(self.escuta)
        print(f"Recebi a mensagem: {mensagem.decode('utf-8')}")
        utils.fecharSocket(self.escuta)

    def configurar(self):
        server_socket = utils.instanciarSocket(self.familia, self.tipo)
        utils.configurarSocket(server_socket, self.host, self.porta)
        return server_socket

    def __init__(self, host, porta, familia):
        self.host = host
        self.porta = porta
        self.tipo = utils.getTipoDeSocket("UDP")
        self.familia = utils.getFamilia(familia.upper())
        self.escuta = self.configurar()

s = ServidorUDP("localhost", 5000, "ipv4")
s.escutar()