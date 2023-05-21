#
import sys

for linea in sys.stdin:
  lista = linea.split(",")
  purpose = lista[3]
  amount = lista[4]
  print(f"{purpose}\t{amount}")