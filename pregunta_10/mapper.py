#
import sys

for l in sys.stdin:
    lista = l.strip().split("\t")
    for x in lista[1].split(","):
        print(f'{x},{int(lista[0])}')
