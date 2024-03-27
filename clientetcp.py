from clientes import ClienteTCP
import base64

cliente = ClienteTCP("ipv4", "localhost", 1234, 65536)
cliente.conectarAoServidor()

def enviarBase64PorPartes(base64_completo, fragment_size=1024):
    tamanho_do_base64 = len(base64_completo)
    deslocamento = 0
    while deslocamento < tamanho_do_base64:
        fim_do_deslocamento = min(deslocamento + fragment_size, tamanho_do_base64)
        fragmento = base64_completo[deslocamento:fim_do_deslocamento]
        cliente.enviarBase64(fragmento)
        deslocamento = fim_do_deslocamento


imagem = open('entrada.png', 'rb') # deer.gif deve existir, senão dá erro
string_binaria_da_imagem = imagem.read() # binário da imagem (typo bytes)
base64_da_string = base64.b64encode(string_binaria_da_imagem) # TIPO BYTES
enviarBase64PorPartes(base64_da_string, 1024)

cliente.encerrarConexao()