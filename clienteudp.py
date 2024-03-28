import socket

maquina = "localhost"
porta = 12345
buffer = 1024
mensagem = "Essa mensagem vai ser lida aí no servidor?"
mensagem_preparada_para_ser_enviada = str.encode(mensagem)

# DIFERENÇA DO CLIENTE E DO SERVIDOR: SERVIDOR TEM bind()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("Cliente OK...")

sock.sendto(mensagem_preparada_para_ser_enviada, (maquina, porta))
bytes_recebidos = sock.recvfrom(buffer)
print(bytes_recebidos[0].decode())
print(bytes_recebidos[1])