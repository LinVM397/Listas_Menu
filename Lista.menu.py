#Menu listas
opcion = 0
elem = 0
position = 0
lista_1 = []

while 4 != opcion:
    print('===============')
    print('  Menú Listas  ')
    print('===============')
    print('1. Agregar elemento')
    print('2. Borrar elemento')
    print('3. Mostrar lista')
    print('4. Salir')
    opcion = int(input('Ingrese opción: '))
    if opcion == 1:
        print('--- Agregar elemento ---')
        elem = input('Ingrese elemento: ')
        lista_1.append(elem)
        print('Se agrego el elemento exitosamente!')
    elif opcion == 2:
        print('--- Borrar elemento ---')
        for x in lista_1:
            print(x)
        position = int(input('Ingrese posición del elemento (considere que el primer elemento es 0): '))
        elem = lista_1.pop(position)
        print('Se borro de la lista el elemento ',elem)
    elif opcion == 3:
        print('---Lista---')
        for i in lista_1:
            print(i)
    elif opcion == 4:
        print('La sesión a terminado.')
