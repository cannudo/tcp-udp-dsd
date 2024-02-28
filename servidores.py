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

servidor = ServidorTCP('127.0.0.1', 1235, "IPV4")
servidor.rodar()