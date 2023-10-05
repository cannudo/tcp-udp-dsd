import socket
import utils

def iniciar_cliente_udp(host, porta):
    familia = utils.getFamilia("IPV4")
    tipo_socket = utils.getTipoDeSocket("UDP")
    cliente_socket = utils.instanciarSocket(familia, tipo_socket)

    try:
        while True:
            mensagem = input("[⌨️] Digite uma mensagem para enviar ao servidor (ou 'sair' para encerrar): ")
            if mensagem.lower() == 'sair':
                break

            dados = utils.encodificarDados(mensagem)
            utils.enviarDados(cliente_socket, dados, tipo_socket, (host, porta))

            dados_resposta, endereco_servidor = utils.receberDados(cliente_socket, tipo_de_socket=tipo_socket)
            resposta = utils.decodificarDados(dados_resposta)
            utils.log("\t[📨] Mensagem recebida do servidor: {}".format(resposta))

    except KeyboardInterrupt:
        print("Cliente encerrado.")
    finally:
        cliente_socket.close()

host = "127.0.0.1"
porta = 4321

iniciar_cliente_udp(host, porta)
