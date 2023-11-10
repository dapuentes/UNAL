a = int(input())
goles = []
goleador = {}
for i in range(a):
    b = int(input())
    goles.append(b)
    c = input()
    c = c.split("-")
    for j in c:
        if j not in goleador:
            goleador[j] = 1
        else:
            goleador[j] += 1
            
prom = round(sum(goles) / a, 1)

max_goleador = max(goleador, key=goleador.get)

print("El promedio de goles fue", prom)
print("El goleador mayor fue", max_goleador)
print("los goleadores fueron:")
for c, b in goleador.items():
    print(c, b)



