
list = []

def Faherenheit(centigrados):
    gradosF = (centigrados * 9/5)+32
    return gradosF

def positivo_Negativo(number):
    if number > 0:
        print("El",number,"es un número positivo.")
    else:
        print("El", number, "es un número negativo.")

def par_impar(number):
    if number%2==0:
        print("El",number,"es un número par.")
    else:
        print("El", number, "es un número impar.")

def conversion_letra(number):
    if number==1:
        print(number,"=","Uno")
    elif number==2:
        print(number,"=","Dos")
    elif number==3:
        print(number,"=","Tres")
    elif number==4:
        print(number,"=","Cuatro")
    elif number==5:
        print(number,"=","Cinco")
    elif number==6:
        print(number,"=","Seis")
    elif number==7:
        print(number,"=","Siete")
    elif number==8:
        print(number,"=","Ocho")
    elif number==9:
        print(number,"=","Nueve")
    elif number==10:
        print(number,"=","Diez")

def suma_Nlista(list):
    i = 0
    sum = 0
    for i in list:
        sum = sum + i
        i+=1
    return sum
op = 0

while op!=6:
    print()
    print('---- Menú ----')
    print('1. Conversión de Centigrados a Fahrenheit.')
    print('2. Número positivo o negativo.')
    print('3. Número par o impar.')
    print('4. Convertisión de número a letra.')
    print('5. Suma de 5 números.')
    print('6. Salir.')
    op = int(input('Ingrese opción: '))
    print()

    if op==1:
        print('** Conversión de Centigrados a Fahrenheit **')
        centigrados = int(input('Ingrese los grados Centigrados: '))
        print("Los grados Fahrenheit son",Faherenheit(centigrados))

    elif op==2:
        print('** Número positivo o negativo **')
        number = int(input('Ingresa número: '))
        positivo_Negativo(number)

    elif op==3:
        print('** Número par o impar **')
        number = int(input('Ingresa número:'))
        par_impar(number)

    elif op==4:
        print('** Convertisión de número a letra **')
        print("Solo se aceptan números en el rango del 1 al 10.")
        number = int(input('Ingresa número:'))
        conversion_letra(number)

    elif op==5:
        i = 0
        print('** Suma de 5 números **')
        print("Solo se aceptan 5 números.")
        for i in range(5):
            number = int(input("Ingrese número:"))
            list.append(number)
            i = i + 1
        print("La suma de los números en lista es:",suma_Nlista(list))

    elif op==6:
        print("Sesión terminada!")