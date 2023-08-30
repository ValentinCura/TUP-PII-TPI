# Crear un diccionario para cada libro
libro1 = {'cod': 'CRBJsAkS', 'cant_ej_ad': 3, 'cant_ej_pr': 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}
libro2 = {'cod': 'QgfV4j3c', 'cant_ej_ad': 4, 'cant_ej_pr': 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry"}
libro3 = {'cod': 'adOd09UE', 'cant_ej_ad': 1, 'cant_ej_pr': 0, "titulo": "El código Da Vinci", "autor": "Dan Brown"}

def nuevo_libro():
    codigoLibro = str(input("\nIngrese el codigo del libro que desea registrar: "))
    cantidadEjemplares = int(input("\nIngrese la cantidad de ejemplares adquiridos: "))
    cantidadEPrestada = int(input("\nIngrese la cantidad de ejemplares prestados: "))                  
    tituloLibro = str(input("\nIngrese su titulo: "))
    autorLibro = str(input("\ningrese su autor: "))
    nuevoLibro = {'cod': codigoLibro, 'cant_ej_ad': cantidadEjemplares, 'cant_ej_pr': cantidadEPrestada, "titulo": tituloLibro, "autor": autorLibro}
    return nuevoLibro

def generar_codigo():
    #completar
    return None