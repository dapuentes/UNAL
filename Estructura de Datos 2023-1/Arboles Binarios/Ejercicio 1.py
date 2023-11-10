class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, value):
        node = Node(value)
        self.root = node

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return True
        aux = self.root
        while True:
            if node.value >= aux.value:
                if aux.right is None:
                    aux.right = node
                    return True
                aux = aux.right
            else:
                if aux.left is None:
                    aux.left = node
                    return True
                aux = aux.left

    def post_orden(self, node):
        if node is None:
            return
        self.post_orden(node.left)
        self.post_orden(node.right)
        print(node.value, end=' ')

    def estudiantes(self, node):
        if node is None:
            return 0
        return 1 + self.estudiantes(node.left) + self.estudiantes(node.right)

    def notas(self, node, ganadores, perdedores):
        if node is None:
            return
        if node.value >= 3:
            ganadores.append(node.value)
        else:
            perdedores.append(node.value)
        self.notas(node.left, ganadores, perdedores)
        self.notas(node.right, ganadores, perdedores)

    def promedio(self, notas):
        if len(notas) > 0:
            return sum(notas) / len(notas)
        return 0
    
    def analisis(self):
        ganadores = []
        perdedores = []
        self.notas(self.root, ganadores, perdedores)
        aux = ganadores[1:]
        cantidad_ganadores = len(aux)
        cantidad_perdedores = len(perdedores)
        prom_ganadores = self.promedio(aux)
        prom_perdedores = self.promedio(perdedores)
        if cantidad_ganadores > cantidad_perdedores:
            print("han ganado mas estudiantes con un total de", cantidad_ganadores)
        elif cantidad_ganadores < cantidad_perdedores:
            print("han perdido mas estudiantes con un total de", cantidad_perdedores)
        else:
            print("han perdido y ganado el mismo numero de estudiantes con un total de", cantidad_ganadores)

        
        print("el promedio de los que perdieron es", round(prom_perdedores,1))
        print("el promedio de los que ganaron es", round(prom_ganadores,1))
        arbol.post_orden(arbol.root)  
        
a = int(input())
arbol = BinaryTree(3)
for i in range(a):
    b = float(input())
    arbol.insert(b)
arbol.analisis()  
