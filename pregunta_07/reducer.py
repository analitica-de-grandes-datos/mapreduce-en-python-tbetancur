#
import sys

datos2 = []
for linea in sys.stdin:
    valor, valor1, valor2 = linea.strip().split('\t')
    datos2.append((valor,valor1,int(valor2)))    
datos2.sort(key=lambda x: (x[0], x[2], x[1]))

for item in datos2:
      clave, valor1, valor2 = item
      print(f"{clave}   {valor1}   {valor2}")
