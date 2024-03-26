from clientes import ClienteTCP
import base64

imagem = open('entrada.png', 'rb') # deer.gif deve existir, senão dá erro
string_binaria_da_imagem = imagem.read() # binário da imagem
base64_da_string = base64.b64encode(string_binaria_da_imagem) # TIPO BYTES

cliente = ClienteTCP("ipv4", "localhost", 1234, 65536)
cliente.conectarAoServidor()
cliente.enviarBase64(base64_da_string)

cliente.encerrarConexao()