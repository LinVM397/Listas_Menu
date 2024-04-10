
lista = []

print('++++ Calculo de Medidas de Tendencia central +++')
print('Solo se aceptan 10 números')
a=0
for a in range(10):
    num = int(input('Ingrese número:'))
    lista.append(num)
    a = a + 1
print('Lista completa!')

import pandas as pd
df = pd.DataFrame(lista)
media = df.mean()
mediana = df.median()
moda = df.mode()
minimo = df.min()
maximo = df.max()
DEstandar = df.std()
print('Media =',media)
print('Mediana =',mediana)
print('Moda =',moda)
print('Número minimo =',minimo)
print('Número maximo =',maximo)
print('Desviación estándar =',DEstandar)