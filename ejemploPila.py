# Ejemplo de uso de Pilas o Stacks en un sistema que verifica si estan bien los parentesis de una funcion ingresada por el usuario

# Creamos las funcion
def verificar_balance(expresion):
    # Creamos una lista vacía "pila" que funcionará como pila
    pila = []
    # Definimos un diccionario que mapea cada paréntesis de cierre a su correspondiente paréntesis de apertura
    par_izq = {'(': ')', '[': ']', '{': '}'}

    # Recorremos cada carácter en la expresión ingresada por el usuario
    for caracter in expresion:
        # Si el carácter es un paréntesis de apertura, lo agregamos a la pila
        if caracter in par_izq.keys():
            pila.append(caracter)
        # Si el carácter es un paréntesis de cierre
        elif caracter in par_izq.values():
            # Verificamos si la pila está vacía o si el paréntesis de cierre coincide con el paréntesis superior de la pila
            if not pila or par_izq[pila.pop()] != caracter:
                # Si no coincide, la expresión no está balanceada, retornamos False
                return False
    
    # Al final del recorrido, la pila debe estar vacía para que la expresión esté balanceada
    return not pila

# Solicitamos al usuario que ingrese una expresión
print("----------------------------------")
print("    ¿Estan bien los paréntesis?   ")
print("----------------------------------")
expresion_usuario = input("Ingrese una expresión matemática con paréntesis: ")

# Verificamos si los paréntesis están balanceados en la expresión ingresada
if verificar_balance(expresion_usuario):
    print(f"La expresión: '{expresion_usuario}', tiene los paréntesis CORRECTAMENTE balanceados.")
else:
    print(f"La expresión: '{expresion_usuario}', tiene los paréntesis INCORRECTAMENTE balanceados.")
