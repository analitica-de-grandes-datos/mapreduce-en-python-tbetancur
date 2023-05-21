#
import sys
from collections import Counter

datos = []
for linea in sys.stdin:
    key = linea.strip().split('\n')
    datos.append(key)
    registros = sorted(list(Counter([x[0] for x in datos]).items()))


for item in registros:
    clave, valor = item
    print(f"{clave}\t{valor}")
