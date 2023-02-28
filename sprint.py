import random
import string

# Lista de nombres de usuarios
usuarios = ['Clemente', 'Ignacio', 'Teresa', 'Fanny', 'Denis', 'Alfonso', 'Helen', 'Carolina', 'Matias', 'Francisco']

# Función para crear una contraseña aleatoria
def crear_contrasena():
    longitud = 8
    caracteres = string.ascii_letters + string.digits
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

# Diccionario para almacenar las cuentas y contraseñas de los usuarios
cuentas = {}

# Recorrer la lista de usuarios y crear una cuenta para cada uno
for usuario in usuarios:
    while True:
         contrasena = crear_contrasena()
         print(f'Se ha creado una cuenta para el usuario {usuario} con la contraseña {contrasena}.')
         numero_telefono = input(f'Ingrese el número telefónico para contactarse con {usuario}:')
         if len(numero_telefono) != 8 or not numero_telefono.isdigit():
            print('El número telefónico debe tener 8 digitos numericos. Intentelo nuevamete.')
         else:    
            cuentas[usuario] = {'contrasena': contrasena, 'numero_telefono': numero_telefono}
            break
    

# Imprimir el diccionario de cuentas y contraseñas
print(cuentas)
