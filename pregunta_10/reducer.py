#
import sys
import itertools
from operator import itemgetter

letras = []
numeros = []
datos = []
for linea in sys.stdin:
    key, value = linea.strip().split(',')
    letras.append(key)
    numeros.append(int(value))
    datos = list(zip(letras,numeros))
#print(f"{datos}")

lista2 = []
for clave, grupo in itertools.groupby(datos,lambda x:x[0]):
    listanums = []
    for cont in grupo:
        listanums.append(cont[1])
    trio = (clave,sorted(listanums))
    lista2.append(trio)
#print(f"{lista2}")


for item in lista2:
     #clave, valor = item
     nums = ",".join(str(valor) for valor in (item[1]))
     print(f"{item[0]}\t{str(nums)}")
