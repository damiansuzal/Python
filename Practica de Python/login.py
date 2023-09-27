def user(usuario):
    
    if len(usuario) < 6:
        return "El nombre de usuario debe contener al menos 6 caracteres."
    elif len(usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres."
    elif not usuario.isalnum():
        return "El nombre de usuario puede contener solo letras y números."
    else:
        return True

def pasw(contraseña):
    
    if len(contraseña) == 0:
        print ("Contraseña no valida")