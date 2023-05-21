#
import sys

for linea in sys.stdin:
    lista = linea.split(" ")
    campo1 = str(lista[3][5:7])
    print(f"{campo1}")
