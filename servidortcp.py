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

servidor = ServidorTCP(FAMILIA_DE_SOCKETS, MAQUINA, PORTA, BUFFER, FILA)
servidor.aceitarConexao()

base64_recebido = servidor.receberBase64() # TIPO BYTES

string_do_base64 = base64.b64decode(base64_recebido) # ERROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO 
resultado = open('saida.png', 'wb') # cria uma imagem e permite escrever nela
resultado.write(string_do_base64)