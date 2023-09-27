def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def producto(a,b):
    return a*b

def division (a,b):
    if a == 0 or b == 0:
        print("No se puede dividir entre cero")
        exit()
    return int(a/b)
