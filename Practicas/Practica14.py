""" pasa una cadena de mayusculas a minusculas """

cadena = 'QUE TAL AMIGO'

print(cadena)

minusculas = cadena.lower()

print(minusculas)

valor = cadena.isupper() 
""" isupper te dice si toda la cadena es mayusculas pero si solo una letra es minuscula
    te manda false y si todas son mayusculas te manda true
    así funciona tambien islower
"""

print(valor)

valor = cadena.islower()

print(valor)