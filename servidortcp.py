import base64, sys, datetime
from servidores import ServidorTCP

def nomeDeUmaNovaImagem(nome_do_cliente):
    agora = datetime.datetime.now()
    return str(nome_do_cliente + " ({}h{}m{}s).png".format(agora.hour, agora.minute, agora.second))

def receberBase64PorPartes(self):
    receptor_do_base64 = b''
    while True:
        fragmento = self.receberBase64()
        if not fragmento:
            break
        receptor_do_base64 += fragmento
    base64_completo = receptor_do_base64
    return base64_completo

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 servidortcp.py <maquina> <tamanho_da_fila>")
        sys.exit(1)


MAQUINA = sys.argv[1]
FILA = sys.argv[2]


servidor = ServidorTCP("ipv4", MAQUINA, 1234, 2048, FILA)
while True:
    servidor.aceitarConexao()
    nome_do_cliente = servidor.receberDados()
    base64_recebido = receberBase64PorPartes(servidor)
    string_do_base64 = base64.b64decode(base64_recebido) 
    resultado = open('imagens/' + nomeDeUmaNovaImagem(nome_do_cliente), 'wb')
    resultado.write(string_do_base64)