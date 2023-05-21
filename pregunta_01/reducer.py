#
import sys

current_key = None
count = 0
for linea in sys.stdin:
    clave, valor = linea.strip().split('\t')  
    if clave != current_key:
        if current_key is not None:
            print(f"{current_key}\t{count}")
        current_key = clave
        count = 0
    count += int(valor)

# Devolviendo resultado en consola
if current_key is not None:
    print(f"{current_key}\t{count}")
