import utils
import socket

class ServidorUDP():
    def enviarDados(self, mensagem, endereco):
        try:
            mensagem_codificada = mensagem.encode("utf-8")
            self.socket_servidor.sendto(mensagem_codificada, endereco)
        except socket.error as e:
            print("[❌ Erro ao enviar dados: %s]" % str(e))

    def receberDados(self, tamanho_maximo):
        try:
            dados_codificados, endereco_cliente = self.socket_servidor.recvfrom(tamanho_maximo)
            dados_decodificados = dados_codificados.decode("utf-8")
        except socket.error as e:
            print("[❌ Erro ao receber dados: %s]" % str(e))

    def configurarSocketParaEscutarNoEndereco(self, maquina, porta):
        endereco = (maquina, porta)
        self.socket_servidor.bind(endereco)

    def instanciarSocket(self, familia):
        familia_de_sockets = utils.getFamilia(familia)
        instancia = socket.socket(familia_de_sockets, socket.SOCK_DGRAM)
        return instancia

    def __init__(self, familia, maquina, porta):
        self.familia = familia
        self.maquina = maquina
        self.porta = porta
        self.socket_servidor = self.instanciarSocket(self.familia)
        self.configurarSocketParaEscutarNoEndereco(self.maquina, self.porta)
