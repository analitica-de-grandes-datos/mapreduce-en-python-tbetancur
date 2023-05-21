#
import sys

for linea in sys.stdin:
    lista = linea.split(" ")
    campo1 = lista[0]
    campo2 = int(lista[6])
    print(f"{campo1}\t{campo2}")
