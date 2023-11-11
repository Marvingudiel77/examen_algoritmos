# Lista para Almacenar
vehiculos = {}

# funciones por oden


def listar_vehiculos():
    print("Lista de vehiculos:")
    for codigo, producto in vehiculos.items():
        print(
            f"Código: {codigo}, Marca: {producto['marca']}, Precio: Q {producto['precio']}, Kilometraje: {producto['kilometraje']}")


def crear_vehiculo():
    codigo = input("Ingrese el código del vehiculo: ")
    marca = input("Ingrese la marca del vehiculo: ")
    precio = float(input("Ingrese el precio del vehiculo: "))
    kilometraje = int(input("Ingrese el kilometraje del vehiculo: "))
    vehiculos[codigo] = {'marca': marca,
                         'precio': precio, 'kilometraje': kilometraje}
    print("Automovil creado con éxito.")


def Editar_vehiculo():
    codigo = input("Ingrese el código del vehiculo que desea actualizar: ")
    if codigo in vehiculos:
        marca = input("Ingrese el nuevo nombre del vehiculo: ")
        precio = float(input("Ingrese el nuevo precio del vehiculo: "))
        kilometraje = int(input("Ingrese el kilometraje del automovil: "))
        vehiculos[codigo] = {'marca': marca,
                             'precio': precio, 'kilometraje': kilometraje}
        print("Automovil actualizado con éxito.")
    else:
        print("El Automovil no existe.")


def eliminar_vehiculo():
    codigo = input("Ingrese el código del vehiculo que desea eliminar: ")
    if codigo in vehiculos:
        del vehiculos[codigo]
        print("Automovil eliminado con éxito.")
    else:
        print("El Automovil no existe.")


# Menus de opciones


while True:
    print("\nOpciones:")
    print("INGRESE LA OPCION DE LA EMPRESA DE VEHICULOS QUE NECESITE: ")
    print("1. Vehiculos")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("\nGestión de Vehiculos:")
        print("1. Lista de vehiculos")
        print("2. Crear vehiculos")
        print("3. Actualizar vehiculo")
        print("4. Eliminar vehiculo")
        subopcion = input("Seleccione una opción: ")

        if subopcion == '1':
            listar_vehiculos()
        elif subopcion == '2':
            crear_vehiculo()
        elif subopcion == '3':
            Editar_vehiculo()
        elif subopcion == '4':
            eliminar_vehiculo()
        else:
            print("Seleccione una opcion valida.")

    elif opcion == '2':
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
