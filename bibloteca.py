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
def prestar_ejemplar_libro(): #Funcion de gestion de prestamos de libros
    codigo=str(input("Ingrese el codigo del libro: "))
    codigoVal = validacion_codigo(codigo)
    if codigoVal:
        for libro in libros:
            if libro["cod"] == codigo:
                if libro["cant_ej_ad"] > 0:
                    print(f'Autor: {libro["autor"]}\nTitulo: {libro["titulo"]}\nCantidad de ejemplares disponibles: {libro["cant_ej_ad"]}')
                    variableConfirmacion = int(input("\n\nDesea confirmar el prestamo? \n1.Si\n2.No\n"))
                    if variableConfirmacion == 1:
                        libro["cant_ej_ad"] -= 1
                        libro["cant_ej_pr"] += 1
                    else: print("Prestamo cancelado.")
                else: print("No quedan ejemplares para prestar")
                break
    return None

def devolver_ejemplar_libro():
    codigo=str(input("Ingrese el codigo del libro a devolver: "))
    codigoVal = validacion_codigo(codigo)
    if codigoVal:
        for libro in libros:
            if libro["cod"] == codigo:
                if libro["cant_ej_pr"] > 0:
                    variableConfirmacion = int(input("\n\nDesea confirmar la devolucion? \n1.Si\n2.No\n"))
                    if variableConfirmacion == 1:
                        libro["cant_ej_ad"] += 1
                        libro["cant_ej_pr"] -= 1
                    else: print("Devolucion cancelada.")
                else: print("No hay ejemplares prestados")
                break
    return None

def registrar_nuevo_libro():
    nuevo_libro = l.nuevo_libro()
    libros.append(nuevo_libro)

def eliminar_ejemplar_libro():
    codigo=str(input("Ingrese el codigo del libro que desea eliminar: "))
    codigoVal = validacion_codigo(codigo)
    if codigoVal:
        for libro in libros:
            if libro["cod"] == codigo:
                libros.remove(libro)
                print("\nLibro eliminado.\n")
                break
def ejemplares_prestados():
    #completar
    return None

def nuevo_libro():
    #completar
    return None