a = int(input())
est = []

for i in range(a):
    ord = {}
    b = input()
    b = b.split("/")
    ord["Nombre"] = b[0]
    ord["Notas"] = [float(k) for k in b[1:]]
    est.append(ord)
   
for ord in est:
    notas = ord["Notas"]
    prom = round(float(notas[0])*0.2 + float(notas[1])*0.1 + float(notas[2])*0.2 + float(notas[3])*0.1 + float(notas[4])*0.2 + float(notas[5])*0.1 + float(notas[6])*0.1, 1)
    ord["Prom"] = prom
    
est_ord = sorted(est, key=lambda e: e["Prom"], reverse=True)

for j, ord in enumerate(est_ord):
    print(j+1, ord["Nombre"], ord["Prom"])
