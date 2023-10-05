import utils, socket

def iniciar_servidor_udp(host, porta):
    familia = utils.getFamilia("IPV4")
    tipo_socket = utils.getTipoDeSocket("UDP")
    servidor_socket = utils.instanciarSocket(familia, tipo_socket)

    try:
        utils.configurarSocket(servidor_socket, host, porta)
        utils.log("[👂] Servidor escutando em {}".format(utils.getPathStr(host, porta)))

        while True:
            dados, endereco_cliente = utils.receberDados(servidor_socket, tipo_de_socket=tipo_socket)
            mensagem = utils.decodificarDados(dados)
            utils.log("\t[📨] Mensagem recebida de {}".format(utils.getPathStr(endereco_cliente[0], endereco_cliente[1])))
            utils.log("\t\t[📩] Conteúdo: {}".format(mensagem))

            resposta = input("\t[⌨️] Digite a resposta: ")
            dados_resposta = utils.encodificarDados(resposta)
            utils.enviarDados(servidor_socket, dados_resposta, tipo_socket, endereco_cliente)

    except KeyboardInterrupt:
        print("Servidor encerrado.")
    finally:
        servidor_socket.close()

host = utils.setAny("127.0.0.1")
porta = utils.setAny(4321)

iniciar_servidor_udp(host, porta)
