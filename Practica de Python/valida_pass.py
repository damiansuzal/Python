"""El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12. El nombre de usuario debe ser alfanumérico.
Nombre de usuario con menos de 6 caracteres, retorna el mensaje "El nombre de usuario debe contener al menos 6 caracteres".
Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede contener más de 12 caracteres".
Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre de usuario puede contener solo letras 
y números". Nombre de usuario válido, retorna True."""
from login import *
usuario= input(str("Ingrese un nombre de usuario: "))
contraseña= input(str("Ingrese una contraseña: "))
if user(usuario):
    print("Nombre de usuario valido")
else:
    print ("Nombre de usuario invalido")

    


