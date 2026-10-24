puntos = 32768
n = 40
l = 0

while 2**l < puntos:
    l = l + 1

total_esquemas = 3**l
por_individuo = 2**l
inferior = por_individuo
superior = n * por_individuo
if superior > total_esquemas:
    superior = total_esquemas

print("Longitud binaria:", l)
print("Puntos de busqueda:", 2**l)
print("Esquemas posibles:", total_esquemas)
print("Esquemas compatibles con un individuo:", por_individuo)
print("Cota inferior general:", inferior)
print("Cota superior general:", superior)
