import libro as l

# Crear una lista vacía para almacenar los libros
libros = []

# Añadir los diccionarios a la lista
libros.append(l.libro1)
libros.append(l.libro2)
libros.append(l.libro3)

def validacion_codigo(codigo):  #Definimos una nueva funcion para validar el codigo de los libros.
    validacion = False
    for libroInd in libros:
        for clave, valor in libroInd.items():
            if valor == codigo:
                validacion = True
                return validacion
                break
    if not validacion:
        print("Error, no existen libros con ese codigo")
def ejemplares_prestados(): #Funcion de gestion de prestamos de libros
    codigo=str(input("Ingrese el codigo del libro: "))
    codigoVal = validacion_codigo(codigo)
    if codigoVal:
        for x in range(0,3):
            if libros[x]["cod"] == codigo:
                if libros[x]["cant_ej_ad"] > 0:
                    print(f'Autor: {libros[x]["autor"]}\nTitulo: {libros[x]["titulo"]}\nCantidad de ejemplares disponibles: {libros[x]["cant_ej_ad"]}')
                    variableConfirmacion = int(input("\n\nDesea confirmar el prestamo? \n1.Si\n2.No\n"))
                    if variableConfirmacion == 1:
                        libros[x]["cant_ej_ad"] -= 1
                        libros[x]["cant_ej_pr"] += 1
                    else: print("Prestamo cancelado.")
                else: print("No quedan ejemplares para prestar")
    return None
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
