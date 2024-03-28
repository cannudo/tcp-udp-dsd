import socket
import utils

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

    def receberResposta(self):
        try:
            resposta_codificada = self.socket_cliente.recv(self.buffer)
            return resposta_codificada.decode('utf-8')
        except socket.error as e:
            print("[❌ Erro ao receber resposta: %s]" % str(e))

    def enviarBase64(self, base64_string):
        if self.socket_cliente:
            try:
                self.socket_cliente.send(base64_string)
            except socket.error as e:
                print("[❌ Erro ao enviar dados: %s]" % str(e))
        else:
            print("[❌ Nenhuma conexão ativa para enviar dados]")


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

    def __init__(self, familia, maquina_servidor, porta_servidor, buffer):
        self.familia = familia
        self.maquina_servidor = maquina_servidor
        self.buffer = buffer
        self.porta_servidor = porta_servidor
        self.socket_cliente = self.instanciarSocket(self.familia)
        endereco_do_servidor = (self.maquina_servidor, self.porta_servidor)
        print("[🔌 tentando conectar à máquina %s ⏳]" % str(str(self.maquina_servidor) + ":" + str(self.porta_servidor)))

class ClienteUDP():
    def receberBytes(self, tamanho_maximo): # IMPORTANTE: atualmente receberDados() retorna uma str UTF-8 decodificada
        bytes_recebidos = self.socket_cliente.recvfrom(tamanho_maximo)
        return bytes_recebidos

    def enviarBytes(self, mensagem):
        if self.socket_cliente:
            try:
                endereco = (self.maquina_servidor, self.porta_servidor)
                mensagem_codificada = str.encode(mensagem)
                self.socket_cliente.sendto(mensagem_codificada, (self.maquina_servidor, self.porta_servidor))
            except socket.error as e:
                print("[❌ erro ao enviar dados: %s ❌]" % str(e))
        else:
            print("[❌ Nenhuma conexão ativa para enviar dados]")

    def instanciarSocket(self, familia):
        familia_de_sockets = utils.getFamilia(familia)
        instancia = socket.socket(familia_de_sockets, socket.SOCK_DGRAM)
        instancia.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        instancia.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        return instancia
    
    def receberMensagensEmBroadcast(self):
        while True:
            dados, endereco = self.socket_cliente.recvfrom(1024)
            print(f"Mensagem recebida de {endereco}: {dados.decode()}")

    def configurarSocketParaEscutarNoEndereco(self, porta):
        endereco = ('', porta)
        self.socket_cliente.bind(endereco)

    def __init__(self, familia, maquina_servidor, porta_servidor):
        self.familia = familia
        self.maquina_servidor = maquina_servidor
        self.porta_servidor = porta_servidor
        self.socket_cliente = self.instanciarSocket(self.familia)
        self.configurarSocketParaEscutarNoEndereco(self.porta_servidor)