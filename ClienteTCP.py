import socket
import  utils

class ClienteTCP():
    def encerrarConexao(self):
        self.socket_cliente.close()
        print("[🔌 Conexão encerrada]")

    def interagirComServidor(self, mensagem):
        self.enviarDados(mensagem)
        resposta = self.receberResposta(self.tamanho_maximo)
        print("[📬 Resposta do servidor:]")
        print("    [%s]" % resposta)

    def conectarAoServidor(self):
        endereco_do_servidor = (self.maquina_servidor, self.porta_servidor)
        print("[🔌 tentando conectar à máquina %s ⏳]" % str(str(self.maquina_servidor) + ":" + str(self.porta_servidor)))
        try:
            self.socket_cliente.connect(endereco_do_servidor)
            print("[✅ conectado 🔗]")
        except ConnectionRefusedError:
            print("[❌ conexão recusada pelo servidor]")

    def receberResposta(self, tamanho_maximo):
        try:
            resposta_codificada = self.socket_cliente.recv(tamanho_maximo)
            return resposta_codificada.decode('utf-8')
        except socket.error as e:
            print("[❌ Erro ao receber resposta: %s]" % str(e))

    def enviarDados(self, mensagem):
        try:
            mensagem_codificada = mensagem.encode("utf-8")
            self.socket_cliente.sendall(mensagem_codificada)
        except socket.error as e:
            print("[❌ erro ao enviar dados: %s ❌]" % str(e))

    def instanciarSocket(self, familia):
         familia_de_sockets = utils.getFamilia(familia)
         instancia = socket.socket(familia_de_sockets, socket.SOCK_STREAM)
         return instancia

    def __init__(self, familia, maquina_servidor, porta_servidor, tamanho_maximo):
        self.familia = familia
        self.maquina_servidor = maquina_servidor
        self.tamanho_maximo = tamanho_maximo
        self.porta_servidor = porta_servidor
        self.socket_cliente = self.instanciarSocket(self.familia)
        endereco_do_servidor = (self.maquina_servidor, self.porta_servidor)
        print("[🔌 tentando conectar à máquina %s ⏳]" % str(str(self.maquina_servidor) + ":" + str(self.porta_servidor)))
