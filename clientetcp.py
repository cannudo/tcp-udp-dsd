from clientes import ClienteTCP
import base64

cliente = ClienteTCP("ipv4", "localhost", 1234, 65536)
cliente.conectarAoServidor()

def enviarBase64PorPartes(base64_data, fragment_size=1024):
    total_size = len(base64_data)
    offset = 0
    while offset < total_size:
        end_offset = min(offset + fragment_size, total_size)
        fragment = base64_data[offset:end_offset]
        cliente.enviarBase64(fragment)
        offset = end_offset


imagem = open('entrada.png', 'rb') # deer.gif deve existir, senão dá erro
string_binaria_da_imagem = imagem.read() # binário da imagem (typo bytes)
base64_da_string = base64.b64encode(string_binaria_da_imagem) # TIPO BYTES
enviarBase64PorPartes(base64_da_string, 1024)

cliente.encerrarConexao()