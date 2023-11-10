a = int(input())
lista = []
for i in range(a):
    b = int(input())
    lista.append(b)
c = 0
for j in lista:
    if j % 2 == 0:
        c += 1
    else:
        None
print("La lista tiene", c, "elementos pares")



