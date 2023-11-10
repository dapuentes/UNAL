lineas = []
for i in range(14):
    a = input()
    lineas.append(a)
  
cuarteto1 = lineas[:4]
cuarteto2 = lineas[4:8]
terceto1 = lineas[8:11]
terceto2 = lineas[11:]        

if cuarteto1[0][-2:] == cuarteto1[3][-2:] and cuarteto1[1][-2:] == cuarteto1[2][-2:] and \
    cuarteto2[0][-2:] == cuarteto2[3][-2:] and cuarteto2[1][-2:] == cuarteto2[2][-2:]:
    if terceto1[0][-2:] == terceto1[2][-2:] and terceto2[0][-2:] == terceto2[2][-2:]:
        print("Es un soneto")
    else:
        print("No es un soneto")
else:
    print("No es un soneto")
