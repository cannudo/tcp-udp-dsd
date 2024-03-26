import servidores

servidor = servidores.ServidorTCP("ipv4", "localhost", 1234)
servidor.aceitarConexao()
servidor.receberDados(65500)
servidor.enviarDados("E aí, clieeente =D")