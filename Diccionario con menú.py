dictionary = {}

op=0
while op!=5:
    print('---- Menú ----')
    print('1. Agregar elemneto')
    print('2. Modificar elemento')
    print('3. Borrar elemento')
    print('4. Mostrar diccionario')
    print('5. Salir')
    op=int(input('Ingrese opción: '))
    print()

    if op==1:
        print('== Agregar elemento ==')
        print('Ingrese la llave y el valor')
        llave = input('Llave: ')
        valor = input('Valor: ')
        dictionary[llave] = valor
        print('Se guardo exitosamente!')

    elif op==2:
        print('== Modificar elemento ==')
        for i in dictionary:
            print(i,'=',dictionary[i])
        print('Ingrese elemento a modificar')
        llave = input('Llave: ')
        valor = input('Nuevo valor: ')
        dictionary[llave] = valor
        print('Modificación exitosa!')

    elif op==3:
        print('== Borrar elemento ==')
        for i in dictionary:
            print(i,'=', dictionary[i])
        print('Ingrese la llave del elemento a borrar')
        llave = input('Llave: ')
        dictionary.pop(llave)
        print('Se elimino el elemento')

    elif op==4:
        print('** Diccionario **')
        for x in dictionary:
            print('Dato:',x,'=',dictionary[x])

    elif op==5:
        print('Sesión terminada.')