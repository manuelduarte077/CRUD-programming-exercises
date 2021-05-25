import os

from tabulate import tabulate

from libro import *

con = conectar()


def iniciar():
    os.system('cls')
    while True:
        print(' Seleccione una de las opciones: ')
        print('\t1. Añadir un libro: ')
        print('\t2. Ver todos los libros: ')
        print('\t3. Buscar un libro: ')
        print('\t4. Modificar un libro: ')
        print('\t5. Eliminar un libro: ')
        print('\t6. Salir de la aplicación: ')
        opcion = input('Escoja una opción: ')

        if opcion == '1':
            nuevo_libro()
        elif opcion == '2':
            ver_libros()
        elif opcion == '3':
            buscar_libro()
        elif opcion == '4':
            modificar_libro()
        elif opcion == '5':
            eliminar_libro()
        elif opcion == '6':
            break


# Funcion para registar los datos en la base de datos
def nuevo_libro():
    titulo = input('Ingrese el titulo: ')
    author = input('Ingrese el author: ')
    estado = input('Ingrese el estado: ')

    respuesta = registrar(titulo, author, estado)
    print(respuesta)


# Función para buscar un libro de la base de datos por medio del id
def ver_libros():
    datos = mostar()
    headers = ['ID', 'TITULO', 'AUTHOR', 'ESTADO']

    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)


def buscar_libro():
    id = input('Ingrese el id del libro')
    datos = buscar(id)
    headers = ['ID', 'TITULO', 'AUTHOR', 'ESTADO']
    tabla = tabulate(datos, headers, tablefmt='fancy_grid')
    print(tabla)


def modificar_libro():
    # Esta es otra forma de poder modificar un dato, teniendo la opción de modificar un campo en especifico
    id = input('Ingrese el id del libro a modificar: ')
    nuevo_valor = ''
    respuesta = ''
    campo = input('Seleccione el campo que desea modificar\n1. Título\n2. Autor\n3. Estado\n')
    if campo == '1':
        nuevo_valor = input('Ingrese el nuevo título del libro: ')
    elif campo == '2':
        nuevo_valor = input('Ingrese el nuevo autor del libro: ')
    elif campo == '3':
        nuevo_valor = input('Ingrese el nuevo estado del libro: ')
    respuesta = modificar(id, campo, nuevo_valor)
    print(respuesta)


def eliminar_libro():
    id = input('Ingrese el id del libro a eliminar')
    respuesta = eliminar(id)
    print(respuesta)


iniciar()
