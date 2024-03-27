import base64, sys
from servidores import ServidorTCP

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Uso: python3 <familia_de_sockets> <maquina> <porta> <tamanho_do_buffer> <tamanho_da_fila>")
        sys.exit(1)


FAMILIA_DE_SOCKETS = sys.argv[1]
MAQUINA = sys.argv[2]
PORTA = sys.argv[3]
BUFFER = sys.argv[4]
FILA = sys.argv[5]

def receberBase64PorPartes(self):
    base64_data = b''  # Inicializa uma string de bytes vazia para armazenar os dados recebidos
    while True:
        fragment = self.receberBase64()  # Recebe um fragmento de dados
        if not fragment:  # Verifica se não há mais dados para receber
            break
        base64_data += fragment  # Concatena o fragmento recebido à string de bytes
    return base64_data

servidor = ServidorTCP(FAMILIA_DE_SOCKETS, MAQUINA, PORTA, BUFFER, FILA)
servidor.aceitarConexao()

base64_recebido = receberBase64PorPartes(servidor)
string_do_base64 = base64.b64decode(base64_recebido) # ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO 
resultado = open('saida.png', 'wb') # cria uma imagem e permite escrever nela
resultado.write(string_do_base64)