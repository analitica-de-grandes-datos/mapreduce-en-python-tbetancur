#
import sys
from operator import itemgetter

datos2 = []
for linea in sys.stdin:
    campo1 = linea[0].strip()
    campo2 = linea[2].strip()
    datos2.append((campo1,campo2))
datos2.sort(key=itemgetter(1))    

for item in datos2:
     clave, valor = item
     print(f"{clave},{valor}")
