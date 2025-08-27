#CALCULADORA CON FUNCIONES

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error: división por cero")
        
        
def calculadora():
    print("Bienvenido a Calculadora")
    
    try:
        num_1=int(input("Ingrese primer número: "))
        num_2=int(input("Ingrese segundo número: "))
        operacion= input("Ingrese la operación deseada: suma, resta, multiplicación, división").strip()
        
        if operacion=="suma":
            resultado=sumar(num_1, num_2)
        elif operacion=="resta":
            resultado=restar(num_1, num_2)
        elif operacion=="multiplicación":
            resultado=multiplicar(num_1,num_2)
        elif operacion=="división":
            resultado=dividir(num_1, num_2)
        
        else:
            print("Operacion inválida.")
            
        print(f"Resultado:{resultado}")          
        
    except ValueError:
        print("Error: Ingrese solo valores numéricos.")
        
    except ZeroDivisionError:
        print("Error: No es posible dividir por cero")
        
        
        
calculadora   ()             