import utils, socket

def iniciar_cliente(host, porta):
    familia = utils.getFamilia("IPV4")  # Use o padrão IPv4
    tipo_socket = utils.getTipoDeSocket("TCP")  # Use o padrão TCP
    cliente_socket = utils.instanciarSocket(familia, tipo_socket)

    try:
        utils.conectarSocket(cliente_socket, host, porta)
        utils.log("[🔗] Conectado ao servidor em {}".format(utils.getPathStr(host, porta)))

        while True:
            mensagem = input("\t[⌨️] Digite uma mensagem para enviar ao servidor (ou 'sair' para encerrar): ")
            if mensagem.lower() == 'sair':
                break

            dados = utils.encodificarDados(mensagem)
            utils.enviarDados(cliente_socket, dados, tipo_socket)

            # Recebe a resposta do servidor
            dados_resposta = utils.receberDados(cliente_socket)
            if not dados_resposta:
                break

            resposta = utils.decodificarDados(dados_resposta)
            utils.log("\t[📨] Mensagem recebida do servidor: {}".format(resposta))

    except KeyboardInterrupt:
        print("Cliente encerrado.")
    finally:
        cliente_socket.close()


host = utils.setAny("127.0.0.1")
porta = utils.setAny(1234)

iniciar_cliente(host, porta)
