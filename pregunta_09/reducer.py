#
import sys
from operator import itemgetter

datos2 = []
for linea in sys.stdin:
    clave, valor1, valor2 = linea.strip().split('\t')
    datos2.append((clave,valor1,int(valor2)))
datos2.sort(key=itemgetter(2))    

for item in datos2:
      clave, valor1, valor2 = item
      if valor2 <= 7:
        print(f"{clave}   {valor1}   {valor2}")
