from gestion_de_ramos.flor import Flor
from gestion_de_ramos.inventario_flores import InventarioFlores
from gestion_de_ramos.ramo import Ramo


def ver_inventario(inventario):
    for i, flor in enumerate(inventario.flores):
        print(f"la flor numero {i} es de tipo {flor.nombre}, con un precio de {flor.precio}, un color {flor.color}, y hay {flor.cantidad} de estas flores en el inventario")


def vender_ramo(inventario):
    print("vender_ramo")
    for i, ramo in enumerate(inventario.ramos):
        print(f"el ramo {i} vale {ramo.precio()} y posee {ramo.tamano()} flores")
    if inventario.ramos:
        respuesta_usuario = int(input("Cual es el numero del ramo que desea vender?"))
        inventario.ramos.pop(respuesta_usuario)
    else:
        print("No hay ramos armados para vender")

def crear_ramo(inventario):
    ramito = Ramo()
    ver_inventario(inventario)

    def pregunta_ramo():
        return int(input("ingrese 1 para agregar flor, 2 para ver precio del ramo, 3 ver para ver el tamaño, "
                         "4 para salir"))

    respuesta_usuario = pregunta_ramo()
    while respuesta_usuario != 4:
        if respuesta_usuario == 1:
            numero_flor = int(input("Ingrese el numero de la flor"))
            ramito.agregar_flor(inventario.flores[numero_flor])
            inventario.baja(numero_flor, 1)
        elif respuesta_usuario == 2:
            print(f"el precio del ramo es {ramito.precio()}")
        elif respuesta_usuario == 3:
            print(f"el tamaño del ramo es {ramito.tamano()}")
        respuesta_usuario = pregunta_ramo()
    inventario.ramos.append(ramito)


def anadir_flores(inventario):
    nombre = input("Ingrese el nombre de la flor")
    precio= float(input("Ingrese el precio de la flor"))
    color = input("Ingrese el color de la flor")
    cantidad = int(input("Ingrese la cantidad de la flor"))
    flor_a_actualizar:Flor = None
    for flor in inventario.flores:
        if flor.nombre == nombre and flor.color == color:
            flor_a_actualizar = flor
    if flor_a_actualizar:
        flor_a_actualizar.precio = precio
        flor_a_actualizar.cantidad += cantidad
    else:
        inventario.flores.append(Flor(nombre=nombre, cantidad=cantidad, precio=precio, color=color))


def hacer_pregunta():
    return int(
        input("Ingrese:\n1 para crear un ramo.\n2 para añadir flores al inventario.\n3 para ver el inventario.\n"
              "4 para vender ramo.\n5 para salir:\n"))


def main():
    respuesta_usuario = hacer_pregunta()
    inventario = InventarioFlores()
    while respuesta_usuario != 5:
        if respuesta_usuario == 1:
            crear_ramo(inventario)
        elif respuesta_usuario == 2:
            anadir_flores(inventario)
        elif respuesta_usuario == 3:
            ver_inventario(inventario)
        elif respuesta_usuario == 4:
            vender_ramo(inventario)
        respuesta_usuario = hacer_pregunta()


if __name__ == '__main__':
    main()
