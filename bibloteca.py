import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)



def validacion_codigo(codigo):
    validacion = False
    for libroInd in libros:
        for clave, valor in libroInd.items():
            if valor == codigo:
                validacion = True
                return validacion
                break
    if not validacion:
        print("Error, no existen libros con ese codigo")
def ejemplares_prestados():
    codigo=str(input("Ingrese el codigo del libro: "))
    validacion_codigo(codigo)
    if validacion_codigo == True:
        #Hacer funcion de gestion de prestamos de libros
        pass

    return None
ejemplares_prestados()
def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    #completar
    return None

def eliminar_ejemplar_libro():
    #completar
    return None

def prestar_ejemplar_libro():
    #completar
    return None

def devolver_ejemplar_libro():
    #completar
    return None

def nuevo_libro():
    #completar
    return None
