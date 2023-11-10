Fis = input()
Fis = Fis.split(" ")
Mat = input()
Mat = Mat.split(" ")
Est = input()
Est = Est.split(" ")

lista = []

Todos = len(set(Fis) | set(Mat) | set(Est))
a = "Tiene " +  str(Todos-1) + " estudiantes en total"
lista.append(a)

Fis_NoEst = len(Fis) - len(set(Fis) & set(Est))
b = ("Tiene " + str(Fis_NoEst-1) + " estudiantes de fisica que no tienen estadistica")
lista.append(b)

Mat_Fis = len(set(Mat) & set(Fis))
c = ("Tiene " + str(Mat_Fis) + " estudiantes que ven matematicas y fisica")
lista.append(c)

Mat_Est = set(Mat) | set(Est)
Mat_Est_NoFis = Mat_Est - set(Fis)
Mat_Est_NoFis = list(sorted(Mat_Est_NoFis))
d = "Lista de estudiantes en matematicas y estadistica que no ven fisica"
lista.append(d)
for i in Mat_Est_NoFis:
    e = i
    lista.append(e)

Est_Mat = set(Est) <= (set(Mat))
if Est_Mat == True:
    f = "todos los estudiantes de estadistica estan en matematicas"
else:
    f = "no todos los estudiantes de estadistica estan en matematicas"

lista.append(f)
    
for j in lista:
    print(j)


