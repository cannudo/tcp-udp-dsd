from clientes import ClienteUDP

c = ClienteUDP("ipv4", "localhost", 12345)
c.receberMensagensEmBroadcast()