#
import sys

for linea in sys.stdin:
  lista = linea.split(",")
  campo1 = lista[0].strip()
  campo2 = int(lista[1].strip())
  print(f"{campo1}\t{campo2}")