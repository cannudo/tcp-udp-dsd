import sys
import clientes


cliente = clientes.ClienteTCP("ipv4", "localhost", 1234, 65500)
cliente.conectarAoServidor()
cliente.enviarDados("Olá, servidor! =D")
print(cliente.receberResposta())