import servidores

servidor = servidores.ServidorTCP("ipv4", "localhost", 1234, 65500, 10)
servidor.aceitarConexao()
servidor.receberDados()
servidor.enviarDados("E aí, clieeente =D")