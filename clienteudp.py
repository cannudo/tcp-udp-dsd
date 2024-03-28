from clientes import ClienteUDP
c = ClienteUDP("ipv4", "localhost", 12345)
c.enviarBytes("Essa mensagem vai ser lida aí no servidor?")
bytes_recebidos = c.receberBytes(2048)
print(bytes_recebidos[0].decode())
print(bytes_recebidos[1])