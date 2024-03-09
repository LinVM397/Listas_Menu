
mult = 1
print("+++ Factorial +++")

num = int(input("Ingrese el número: "))

for i in range(num):
    i+=1
    mult = mult * i
for i in range(1,num):
    print(i,"x", end="")
print(num)
print("El Factorial de",num,"es",mult)