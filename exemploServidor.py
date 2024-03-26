import sys
import servidores

if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Uso: python3 <familia_de_sockets> <maquina> <porta> <tamanho_do_buffer> <tamanho_da_fila>")
        sys.exit(1)


FAMILIA_DE_SOCKETS = sys.argv[1]
MAQUINA = sys.argv[2]
PORTA = sys.argv[3]
BUFFER = sys.argv[4]
FILA = sys.argv[5]

servidor = servidores.ServidorTCP(FAMILIA_DE_SOCKETS, MAQUINA, PORTA, BUFFER, FILA)
servidor.aceitarConexao()
servidor.receberDados()
servidor.enviarDados("E aí, clieeente =D")