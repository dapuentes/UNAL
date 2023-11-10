a = int(input())
lista = []
for i in range(a):
    b = int(input())
    lista.append(b)

for j in range(a):
    for k in range(j+1, a):
        if lista[j] + lista[k] == 10:
            lista[j], lista[k] = lista[k], lista[j]

for l in lista:
    print(l)