#
import sys

for linea in sys.stdin:
    lista = linea.split(" ")
    campo1 = lista[0]
    campo2 = float(lista[6])
    print(f"{campo1}\t{campo2}")
