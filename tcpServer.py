import utils, socket

def iniciar_servidor(host, porta):
    familia = utils.getFamilia("IPV4")
    tipo_socket = utils.getTipoDeSocket("TCP")
    servidor_socket = utils.instanciarSocket(familia, tipo_socket)
    utils.configurarSocket(servidor_socket, host, porta)
    utils.escutar(servidor_socket, 50)

    utils.log("[👂] Servidor escutando em {}".format(utils.getPathStr(host, porta)))

    while True:
        utils.log("\t[🌐] Aguardando conexões...")
        cliente_socket, endereco_cliente = utils.aceitarConexao(servidor_socket)
        utils.log("\t\t[🔗] Conexão estabelecida com {}".format(utils.getPathStr(endereco_cliente[0], endereco_cliente[1])))

        # Lida com a interação com o cliente
        interagir_com_cliente(cliente_socket, endereco_cliente)

        # Fecha o socket do cliente após a interação
        cliente_socket.close()

def interagir_com_cliente(cliente_socket, endereco_cliente):
    try:
        while True:
            dados = utils.receberDados(cliente_socket)
            if not dados:
                break  # Se não houver mais dados, a conexão foi encerrada pelo cliente

            mensagem = utils.decodificarDados(dados)
            utils.log("\t\t[📨] Mensagem recebida de {}".format(utils.getPathStr(endereco_cliente[0], endereco_cliente[1])))
            utils.log("\t\t\t[📩] Conteúdo: {}".format(mensagem))

            # Responda ao cliente
            resposta = input("Digite a resposta: ")
            dados_resposta = utils.encodificarDados(resposta)
            utils.enviarDados(cliente_socket, dados_resposta, tipo_socket)

    except KeyboardInterrupt:
        print("Servidor encerrado.")


host = utils.setAny('127.0.0.1')
porta = utils.setAny(1234)
buffer_size = utils.setAny(1024)
tipo_socket = utils.getTipoDeSocket("TCP")
familia = utils.getFamilia("IPV4")

iniciar_servidor(host, porta)