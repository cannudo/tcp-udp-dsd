from servidores import ServidorUDP
s = ServidorUDP("ipv4", "localhost", 12345)
bytes_recebidos = s.receberBytes(1024)
mensagem_recebida = bytes_recebidos[0].decode()
endereco_do_qual_a_mensagem_veio = bytes_recebidos[1]
print(mensagem_recebida)
print(endereco_do_qual_a_mensagem_veio)
s.enviarBytes("Isto pode ser lido por você, cliente?", endereco_do_qual_a_mensagem_veio)