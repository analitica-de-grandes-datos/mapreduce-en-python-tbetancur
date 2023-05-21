#
import sys
from collections import Counter

datos = []
for line in sys.stdin:
    key = line.strip().split('\n')
    datos.append(key[0])
    #registros = sorted(datos.items())
    registros = sorted(list(Counter([x[0] for x in datos]).items()))
    #campo1 = line[0].strip()
#print(f"{registros}")


for item in registros:
    clave, valor = item
    print(f"{clave},{valor}")
