# Autores: Daniel Felipe Puentes Rocha, Ricardo Willian Salazar Espinal

class Libro:
    def __init__(self, nombre, autor, categoria, estado='libre', veces_prestado=0):
        self.nombre = nombre
        self.autor = autor
        self.categoria = categoria
        self.estado = estado
        self.veces_prestado = veces_prestado


class Biblioteca:
    def __init__(self):
        self.libros = {}

    def cargar_libros_desde_archivo(self, archivo):
        with open(archivo, 'r', encoding='utf-8') as file:
            for line in file:
                nombre, autor, categoria = line.strip().split(' - ')
                nombre = nombre.replace('"', '')
                self.agregar_libro(nombre, autor, categoria)

    def agregar_libro(self, nombre, autor, categoria):
        if nombre in self.libros:
            print("El libro", nombre, "ya existe en la biblioteca.")
        else:
            self.libros[nombre] = Libro(nombre, autor, categoria)
            print("Libro", nombre, "agregado correctamente.")

    def eliminar_libro(self, nombre):
        if nombre in self.libros:
            del self.libros[nombre]
            print("Libro", nombre, "eliminado correctamente.")
        else:
            print("El libro no existe en la biblioteca.")

    def prestar_libro(self, nombre):
        if nombre in self.libros:
            libro = self.libros[nombre]
            if libro.estado == 'libre':
                libro.estado = 'prestado'
                libro.veces_prestado += 1
                print("Libro", nombre, "prestado correctamente.")
            else:
                print("El libro", nombre, "ya está prestado. Se ha prestado en", libro.veces_prestado, "ocacion(es)")
        else:
            print("El libro no existe en la biblioteca.")

    def devolver_libro(self, nombre):
        if nombre in self.libros:
            libro = self.libros[nombre]
            if libro.estado == 'prestado':
                libro.estado = 'libre'
                print("Libro devuelto correctamente.")
            else:
                print("El libro no está prestado.")
        else:
            print("El libro no existe en la biblioteca.")

    def mostrar_libros_categoria(self, categoria):
        libros_categoria = []
        for nombre, libro in self.libros.items():
            if libro.categoria == categoria:
                libros_categoria.append((nombre, libro))
        if libros_categoria:
            print(f"Libros en la categoría '{categoria}':")
            for nombre, libro in libros_categoria:
                print(f"- {nombre}, {libro.autor} - {libro.categoria}")
        else:
            print(f"No existen libros en la categoría '{categoria}'.")


    def mostrar_libros_autor(self, autor):
        libros_autor = []
        for nombre, libro in self.libros.items():
            if libro.autor == autor:
                libros_autor.append((nombre, libro))
        if libros_autor:
            print(f"Libros del autor '{autor}':")
            for nombre, libro in libros_autor:
                print(f"- {nombre}: {libro.categoria}")
        else:
            print(f"No existen libros del autor '{autor}'.")


    def libro_mas_prestado(self):
        libros_mas_prestados = []
        max_prestamos = 0
        for libro in self.libros.values():
            if libro.veces_prestado > max_prestamos:
                libros_mas_prestados = [libro]
                max_prestamos = libro.veces_prestado
            elif libro.veces_prestado == max_prestamos:
                libros_mas_prestados.append(libro)
        
        if libros_mas_prestados:
            print("Libros más prestados:")
            for libro in libros_mas_prestados:
                print(f"- {libro.nombre} ({libro.autor}): {libro.categoria}")
        else:
            print("No hay libros en la biblioteca.")



    def categoria_mas_prestada(self):
        categorias_prestadas = {}
        max_prestamos = 0
        for libro in self.libros.values():
            categoria = libro.categoria
            if categoria in categorias_prestadas:
                categorias_prestadas[categoria] += libro.veces_prestado
            else:
                categorias_prestadas[categoria] = libro.veces_prestado
            max_prestamos = max(max_prestamos, categorias_prestadas[categoria])

        if categorias_prestadas:
            categorias_mas_prestadas = [categoria for categoria, prestamos in categorias_prestadas.items() if prestamos == max_prestamos]
            print("Categorías más prestadas:")
            for categoria in categorias_mas_prestadas:
                print(f"- {categoria}")
        else:
            print("No hay libros en la biblioteca.")


    def categorias_menos_prestadas(self):
        categorias_prestadas = {}
        for libro in self.libros.values():
            categoria = libro.categoria
            if categoria in categorias_prestadas:
                categorias_prestadas[categoria] += libro.veces_prestado
            else:
                categorias_prestadas[categoria] = libro.veces_prestado
        if categorias_prestadas:
            prestamos_minimos = min(categorias_prestadas.values())
            categorias_menos_prestadas = [categoria for categoria, prestamos in categorias_prestadas.items() if prestamos == prestamos_minimos]
            print("Categorías con menos prestamos:")
            for categoria in categorias_menos_prestadas:
                print(f"- {categoria}")
        else:
            print("No hay libros en la biblioteca.")

    def mostrar_categorias_libros(self):
        categorias_libros = {}
        for libro in self.libros.values():
            categoria = libro.categoria
            if categoria in categorias_libros:
                categorias_libros[categoria].append(libro)
            else:
                categorias_libros[categoria] = [libro]

        if categorias_libros:
            print("Categorías y número de libros:")
            for categoria, libros in sorted(categorias_libros.items(), key=lambda x: len(x[1]), reverse=True):
                print(f"Categoría: {categoria}")
                print(f"Número de libros: {len(libros)}")
                print("Libros:")
                for libro in libros:
                    print(f"- {libro.nombre}: {libro.autor}")
                print("---")
        else:
            print("No hay libros en la biblioteca.")


    
    # Funcion adicional 1
    # Esta función muestra todos los libros que están actualmente prestados en la biblioteca.
    def mostrar_libros_prestados(self):
        libros_prestados = []
        for nombre, libro in self.libros.items():
            if libro.estado == 'prestado':
                libros_prestados.append((nombre, libro))

        if libros_prestados:
            print("Libros prestados:")
            for nombre, libro in libros_prestados:
                print(f"- {nombre}: {libro.autor} - {libro.categoria}")
        else:
            print("No hay libros prestados en la biblioteca.")


    # Funcion adicional 2
    # Esta función permite actualizar la información de un libro existente en la biblioteca, como el autor, la categoría, el estado y el número de veces prestado. El unico dato obligatorio es el nombre del libro
    def actualizar_informacion_libro(self, nombre, autor=None, categoria=None, estado=None, veces_prestado=None):
        if nombre in self.libros:
            libro = self.libros[nombre]
            if autor:
                libro.autor = autor
            if categoria:
                libro.categoria = categoria
            if estado:
                libro.estado = estado
            if veces_prestado is not None:
                libro.veces_prestado = veces_prestado
            print("Información del libro actualizada correctamente.")
        else:
            print("El libro no existe en la biblioteca.")




# Ejemplo de uso
biblioteca = Biblioteca()

biblioteca.cargar_libros_desde_archivo("C:/Users/Daniel/Desktop/Estructura de Datos/Taller/biblioteca.txt")
"\n"

biblioteca.agregar_libro("El Psicoanalista", "John Katzenbach", "Thriller")
biblioteca.prestar_libro("El Psicoanalista")
biblioteca.devolver_libro("El Psicoanalista")
biblioteca.eliminar_libro("El Psicoanalista")
biblioteca.prestar_libro("El Psicoanalista")
print("\n")

biblioteca.prestar_libro("Rayuela")
biblioteca.prestar_libro("El código Da Vinci")
biblioteca.prestar_libro("Mujercitas")
biblioteca.prestar_libro("Cien años de soledad")
biblioteca.devolver_libro("Rayuela")
print("\n")

biblioteca.mostrar_libros_categoria("Clásico")
biblioteca.mostrar_libros_autor("Gabriel García Márquez")
print("\n")
biblioteca.libro_mas_prestado()
biblioteca.categoria_mas_prestada()
biblioteca.categorias_menos_prestadas()
biblioteca.mostrar_categorias_libros()
print("\n")

biblioteca.mostrar_libros_prestados()
biblioteca.actualizar_informacion_libro("El código Da Vinci", autor="Dan Brown", categoria="Clásico", estado="prestado", veces_prestado=5)


