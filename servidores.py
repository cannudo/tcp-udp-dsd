import utils
import socket

class ServidorTCP():
    def encerrarConexao(self):
        if self.socket_cliente:
            self.socket_cliente.close()
            print("[🔌 Conexão encerrada com %s]" % str(self.endereco_cliente))
            self.socket_cliente, self.endereco_cliente = None, None
        else:
            print("[❌ Nenhuma conexão ativa para encerrar]")

    def receberBase64(self):
        if self.socket_cliente:
            try:
                dados = self.socket_cliente.recv(self.buffer)
                return dados
            except socket.error as e:
                print("[❌ Erro ao receber dados: %s]" % str(e))
        else:
            print("[❌ Nenhuma conexão ativa para receber dados]")
        return None

    def receberDados(self):
        if self.socket_cliente:
            try:
                dados_codificados = self.socket_cliente.recv(self.buffer)
                if dados_codificados:
                    dados_decodificados = dados_codificados.decode("utf-8")
                    print("[📦 dados recebidos de %s]:" % str(self.endereco_cliente))
                    print("    [%s]" % dados_decodificados)
                return dados_decodificados
            except socket.error as e:
                print("[❌ Erro ao receber dados: %s]" % str(e))
            else:
                print("[❌ Nenhuma conexão ativa para receber dados]")
            return None

    def enviarBase64(self, base64_string):
        if self.socket_cliente:
            try:
                self.socket_cliente.send(base64_string)
            except socket.error as e:
                print("[❌ Erro ao enviar dados: %s]" % str(e))
        else:
            print("[❌ Nenhuma conexão ativa para enviar dados]")

    def enviarDados(self, mensagem):
        if self.socket_cliente:
            try:
                mensagem_codificada = mensagem.encode("utf-8")
                self.socket_cliente.send(mensagem_codificada)
            except socket.error as e:
                print("[❌ Erro ao enviar dados: %s]" % str(e))
        else:
            print("[❌ Nenhuma conexão ativa para enviar dados]")

    def aceitarConexao(self):
        print("[🎧 Servidor TCP em modo de escuta no endereço %s]" % str(self.maquina + ":" + str(self.porta)))
        self.socket_cliente, self.endereco_cliente = self.socket_servidor.accept()
        print("[✅ Conexão aceita de %s]" % str(self.endereco_cliente))

    def loop(self):
        while True:
            dados = self.socket_cliente.recv(self.buffer)
            if dados:
                print("[📦 dados recebidos de %s]:" % str(self.endereco_cliente))
                print("    [%s]" % dados.decode('utf-8'))
                self.socket_cliente.send("Olá, cliente =)".encode('utf-8'))
                self.socket_cliente.close()
                # TODO mais coisas


    def habilitarModoDeEscuta(self, tamanho_da_fila = 5):
        self.socket_servidor.listen(tamanho_da_fila)

    def configurarSocketParaEscutarNoEndereco(self, maquina, porta):
        endereco = (maquina, porta)
        self.socket_servidor.bind(endereco)
    
    def instanciarSocket(self, familia):
        familia_de_sockets = utils.getFamilia(familia)
        instancia = socket.socket(familia_de_sockets, socket.SOCK_STREAM)
        return instancia

    def __init__(self, familia, maquina, porta, buffer, fila):
        self.familia = familia
        self.maquina = maquina
        self.porta = int(porta)
        self.buffer = int(buffer)
        self.fila = int(fila)
        self.socket_cliente, self.endereco_cliente = None, None
        self.socket_servidor = self.instanciarSocket(self.familia)
        self.socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.configurarSocketParaEscutarNoEndereco(self.maquina, self.porta)
        self.habilitarModoDeEscuta(self.fila)

class ServidorUDP():
    def enviarBytes(self, mensagem, endereco):
        try: 
            mensagem_codificada = str.encode(mensagem)
            self.socket_servidor.sendto(mensagem_codificada, endereco)
        except socket.error as e:
            print("[❌ Erro ao enviar dados: %s]" % str(e))

    def receberBytes(self, tamanho_maximo):
        try:
            bytes_recebidos = self.socket_servidor.recvfrom(tamanho_maximo)
            return bytes_recebidos
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