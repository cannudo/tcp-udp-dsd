from servidores import ServidorUDP
import threading

s = ServidorUDP("IPV4", "localhost", 12345)
threading.Thread(target = s.receberClientes).start()
while True:
    mensagem = input("Enviar para todos: ")
    s.enviarBytesPorBroadcast(mensagem)