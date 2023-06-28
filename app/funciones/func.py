
def pedir_numero():

    while True:
        try:
            numero = int(input("¿En qué número estás pensando?: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            return numero

num = pedir_numero()

def validacion(num):
    
    if num %2 == 0:
        print(f"{num} es un numero par")
    else:
        print(f"{num} es un numero impar")
        
        
validacion(num)



        
    
    
    
    
