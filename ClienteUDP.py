import utils
import socket

class ClienteUDP():
    receberDados(self, tamanho_maximo): # IMPORTANTE: atualmente receberDados() retorna uma str UTF-8 decodificada
        dados_codificados = self.socket_servidor.recvfrom(tamanho_maximo)
        dados_decodificados = dados_codificados.decode('utf-8')
        return dados_decodificados

    def enviarDados(self, mensagem, maquina_servidor, porta_servidor):
        if self.socket_cliente:
            try:
                endereco_do_servidor = (maquina_servidor, porta_servidor)
                mensagem_codificada = mensagem.encode('utf-8')
                self.socket_cliente.sendto(mensagem_codificada, endereco_do_servidor)
            except socket.error as e:
                print("[❌ erro ao enviar dados: %s ❌]" % str(e))
        else:
            print("[❌ Nenhuma conexão ativa para enviar dados]")

    def instanciarSocket(self, familia):
        familia_de_sockets = utils.getFamilia(familia)
        instancia = socket.socket(familia_de_sockets, socket.SOCK_DGRAM)
        return instancia
    
    def __init__(self, familia, maquina_servidor, porta_servidor):
        self.familia = familia
        self.maquina_servidor = maquina_servidor
        self.porta_servidor = porta_servidor
        self.socket_cliente = self.instanciarSocket(self.familia)