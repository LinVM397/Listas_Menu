
print("-- Tablas de Multiplicar --")
num = int(input("Ingrese el número: "))
print("La tabla de multiplicar del ",num)

for i in range(1,13):
    t = num * i
    print(num,"x",i ,"=",t)
