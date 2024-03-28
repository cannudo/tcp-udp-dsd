import socket

maquina = "localhost"
porta = 12345
buffer = 1024
mensagem = "Isto pode ser lido por você, cliente?"
mensagem_preparada_para_ser_enviada = str.encode(mensagem)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((maquina, porta))
print("Servidor no ar...")

while True:
    bytes_recebidos = sock.recvfrom(buffer)
    mensagem_recebida = bytes_recebidos[0]
    endereco_do_qual_a_mensagem_veio = bytes_recebidos[1]
    print(mensagem_recebida.decode())
    print(endereco_do_qual_a_mensagem_veio)
    
    sock.sendto(mensagem_preparada_para_ser_enviada, endereco_do_qual_a_mensagem_veio)