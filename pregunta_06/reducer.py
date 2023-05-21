#
import sys
import itertools
from operator import itemgetter

letras = []
numeros = []
datos = []
for linea in sys.stdin:
    clave, valor = linea.strip().split('\t')
    letras.append(clave)
    numeros.append(float(valor))
    datos = list(zip(letras,numeros))
#print(f"{datos}")

lista2 = []
for clave, grupo in itertools.groupby(datos,lambda x:x[0]):
    listanums = []
    for cont in grupo:
        listanums.append(cont[1])
    trio = (clave,max(listanums),min(listanums))
    lista2.append(trio)

for item in lista2:
    clave, maximo, minimo = item
    print(f"{clave}\t{maximo}\t{minimo}")
