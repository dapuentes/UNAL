from tkinter import Tk, messagebox, Menu, Frame, Label, Button, BOTH, TOP, RIGHT, LEFT, BOTTOM, ttk, FALSE
from PIL import Image, ImageTk

#from baseDatos.deserializador import Deserializador
#from baseDatos.serializador import Serializador
from gestorAplicacion.infraestructura.plaza import Plaza
from uMain.Funcionalidades.agregarSector import AgregarSector
from uMain.excepciones.excepcionPresenciaArchivo import ExcepcionPresenciaArchivos
from uMain.excepciones.excepcionPresenciaImagenes import ExcepcionPresenciaImagenes


#def guardar(self):
    #Serializador.serializarTodo()


#def cargar(self):
    #Deserializador.deserializarTodo()


# cargar()
#Deserializador.deserializarTodo()


def inicio():
    a = ["Imagenes/Plaza/1.jpg", "Imagenes/Plaza/2.jpg", "Imagenes/Plaza/3.jpg"]
    b = ["Imagenes/Yo/1.jpg"]
    dir = a + b
    try:
        # ExcepcionPresenciaArchivos.presenciaArchivos(["baseDatos/temp/Clientes.txt", "baseDatos/temp/Duenhos.txt", "baseDatos/temp/Codeudores.txt", "baseDatos/temp/Locales.txt", "baseDatos/temp/Contratos.txt"])
        ExcepcionPresenciaImagenes.presenciaImagenes(dir)
        # cargar()
        #Deserializador.deserializarTodo()
    except ExcepcionPresenciaArchivos:
        return "Error en la presencia de archivos"
    except ExcepcionPresenciaImagenes:
        return "Error en la presencia de imagenes"


inicio()

ventana = Tk()
ventana.title("Menu - Sistema de la plaza '" + Plaza.nombre + "'")
ventana.geometry("+10+10")
ventana.resizable(1, 1)
ventana.option_add("*tearOff", FALSE)
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_rowconfigure(0, weight=1)


def ocultar():
    ventanaInicio.pack_forget()
    ventanaUsuario.pack_forget()
    ventanaAgregarSector.pack_forget()
    """ventanaAgregarLocal.pack_forget()
    ventanaRegistrarDuenho.pack_forget()
    ventanaRegistrarCliente.pack_forget()
    ventanaRegistrarCodeudor.pack_forget()
    ventanaAlquilarLocal.pack_forget()
    ventanaMostrarLocalesDesocupados.pack_forget()
    ventanaMostrarLocalesOcupados.pack_forget()
    ventanaMostrarHistorialAlquiler.pack_forget()
    ventanaMostrarListadoContratosVigentes.pack_forget()
    ventanaAutomatizacion.pack_forget()
    ventanaMostrarDatosGuardados.pack_forget()"""


def borrarTodo():
    ventanaAgregarSector.borrar()
    #ventanaAgregarLocal.borrar()
    #ventanaRegistrarDuenho.borrar()
    #ventanaRegistrarCliente.borrar()
    #ventanaRegistrarCodeudor.borrar()
    #ventanaAlquilarLocal.borrar()
    #ventanaMostrarLocalesDesocupados.borrar()
    #ventanaMostrarLocalesOcupados.borrar()
    #ventanaMostrarHistorialAlquiler.borrar()
    #ventanaMostrarListadoContratosVigentes.borrar()
    #ventanaAutomatizacion.borrar()
    #ventanaMostrarDatosGuardados.borrar()


vida = "Hola"

pi = 1


def cambiarImagen():
    global pi
    pi += 1
    if pi == 3:
        pi = 1
    foto = ("imagenes/pi" + str(pi) + ".jpg").resize((400, 400), Image.ANTIALIAS)
    foto = ImageTk.PhotoImage(foto)
    labelFotoPlaza.configure(image=foto)
    labelFotoPlaza.image = foto


pi2 = 0


def cambiarImagen2():
    global pi2
    pi2 += 1
    if pi2 == 3:
        pi2 = 1
    foto = ("imagenes/pi" + str(pi2) + ".jpg").resize((400, 400), Image.ANTIALIAS)
    foto = ImageTk.PhotoImage(foto)
    # labelfoto2.configure(image=foto)
    # labelfoto2.image = foto


def descripcion():
    a = "Esto es una prueba"
    messagebox.showinfo(title="Descripcion", message=a)


def salir():
    a = messagebox.askyesno(title="Salir", message="¿Esta seguro que desea salir?")
    if a:
        #guardar()
        ventana.destroy()


def ingresar():
    ocultar()
    borrarTodo()
    ventanaUsuario.pack()
    ventana["menu"] = menuVentanaUsuario


def agregarSector():
    ocultar()
    borrarTodo()
    ventanaAgregarSector.pack()

"""
def agregarLocal():
    ocultar()
    borrar()
    ventanaAgregarLocal.pack()


def registrarDuenho():
    ocultar()
    borrar()
    ventanaRegistrarDuenho.pack()


def registrarCliente():
    ocultar()
    borrar()
    ventanaRegistrarCliente.pack()


def registrarCodeudor():
    ocultar()
    borrar()
    ventanaRegistrarCodeudor.pack()


def alquilarLocal():
    ocultar()
    borrar()
    ventanaAlquilarLocal.pack()


def mostrarLocalesDesocupados():
    ocultar()
    borrar()
    ventanaMostrarLocalesDesocupados.pack()


def mostrarLocalesOcupados():
    ocultar()
    borrar()
    ventanaMostrarLocalesOcupados.pack()


def mostrarHistorialAlquiler():
    ocultar()
    borrar()
    ventanaMostrarHistorialAlquiler.pack()


def mostrarListadoContratosVigentes():
    ocultar()
    borrar()
    ventanaMostrarListadoContratosVigentes.pack()


def automatizacion():
    ocultar()
    borrar()
    ventanaAutomatizacion.pack()


def mostrar2():
    ocultar()
    borrar()
    ventanaMostrarDatosGuardados.pack()

"""
def aplicacion():
    a = "Esto es una prueba"
    messagebox.showinfo(title="Informacion", message=a)


def salirUsuario():
    a = messagebox.askyesno(title="Salir", message="¿Esta seguro que desea regresar al inicio?")
    if a:
        ocultar()
        ventanaInicio.pack()
        ventana["menu"] = menuVentanaInicio


def ayuda():
    a = """Autor(es):

    - Daniel Felipe Puentes Rocha
    """
    messagebox.showinfo(title="Acerca de", message=a)


menuVentanaInicio = Menu(ventana, font="Helvetica 11", fg="red")

menuInicio = Menu(menuVentanaInicio, font="Helvetica 12")

menuVentanaInicio.add_cascade(label="Inicio", menu=menuInicio)

menuInicio.add_command(label="Descripcion", command=descripcion)

menuInicio.add_command(label="Salir", command=salir)

ventana["menu"] = menuVentanaInicio

menuVentanaUsuario = Menu(ventana, font="Helvetica 12")

menuArchivo = Menu(menuVentanaUsuario, font="Helvetica 12")

menuVentanaUsuario.add_cascade(label="Archivo", menu=menuArchivo)

menuArchivo.add_command(label="Aplicacion", command=aplicacion)

menuArchivo.add_command(label="Salir", command=salirUsuario)

menuProcesos = Menu(menuVentanaUsuario, font="Helvetica 12")

menuVentanaUsuario.add_cascade(label="Procesos", menu=menuProcesos)

menuProcesos.add_command(label="Agregar sector a la plaza", command=agregarSector)
"""
menuProcesos.add_command(label="Agregar local a la plaza", command=agregarLocal)

menuProcesos.add_command(label="Registrar duenho", command=registrarDuenho)

menuProcesos.add_command(label="Registrar cliente", command=registrarCliente)

menuProcesos.add_command(label="Registrar codeudor", command=registrarCodeudor)

menuProcesos.add_command(label="Alquilar local", command=alquilarLocal)

menuProcesos.add_command(label="Mostrar locales desocupados", command=mostrarLocalesDesocupados)

menuProcesos.add_command(label="Mostrar locales ocupados", command=mostrarLocalesOcupados)

menuProcesos.add_command(label="Mostrar historial de alquiler", command=mostrarHistorialAlquiler)

menuProcesos.add_command(label="Mostrar listado de contratos vigentes", command=mostrarListadoContratosVigentes)

menuOpciones = Menu(menuProcesos, font="Helvetica 12")

menuProcesos.add_cascade(label="Opciones avanzadas", menu=menuOpciones)

menuOpciones.add_command(label="Acceder al menu de automatizacion", command=automatizacion)

menuOpciones.add_command(label="Mostrar datos guardados", command=mostrar2)

menuAyuda = Menu(menuVentanaUsuario, font="Helvetica 12")
menuVentanaUsuario.add_cascade(label="Ayuda", menu=menuAyuda)
menuAyuda.add_command(label="Acerca de", command=ayuda)
"""

ventanaInicio = Frame()
P1 = Frame(master=ventanaInicio, highlightbackground="black", highlightthickness=2)
P2 = Frame(master=ventanaInicio, highlightbackground="black", highlightthickness=2)
P3 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P4 = Frame(master=P1, highlightbackground="black", highlightthickness=2)
P5 = Frame(master=P2, highlightbackground="black", highlightthickness=2)
P6 = Frame(master=P2, highlightbackground="black", highlightthickness=2)

saludo = Label(master=P3, text="""Bienvenido al sistema de alquiler de locales""", font="Helvetica 12")

ingreso = Button(master=P4, text="Ingresar", font="Helvetica 12", bg="grey", fg="white", borderwidth=5, relief="groove",
                 command=ingresar)

tituloVida = Label(master=P5, text="Biografia de lo(s) autor(es)", font="Helvetica 12")

cuerpoVida = Label(master=P5, text=vida, font="Helvetica 12", anchor="w")

fotoAnimal = (Image.open("Imagenes/Plaza/1.jpg")).resize((400, 400), Image.ANTIALIAS)
fotoAnimal = ImageTk.PhotoImage(fotoAnimal)
foto1 = (Image.open("Imagenes/Yo/1.jpg")).resize((200, 200), Image.ANTIALIAS)
foto1 = ImageTk.PhotoImage(foto1)
foto2 = (Image.open("Imagenes/Yo/1.jpg")).resize((200, 200), Image.ANTIALIAS)
foto2 = ImageTk.PhotoImage(foto2)
foto3 = (Image.open("Imagenes/Yo/1.jpg")).resize((200, 200), Image.ANTIALIAS)
foto3 = ImageTk.PhotoImage(foto3)
foto4 = (Image.open("Imagenes/Yo/1.jpg")).resize((200, 200), Image.ANTIALIAS)
foto4 = ImageTk.PhotoImage(foto4)

labelFotoPlaza = Label(master=P4, image=fotoAnimal)
labelFoto1 = Label(master=P6, image=foto1)
labelFoto1.grid(row=0, column=0, padx=3, pady=3)
labelFoto2 = Label(master=P6, image=foto2)
labelFoto2.grid(row=0, column=1, padx=3, pady=3)
labelFoto3 = Label(master=P6, image=foto3)
labelFoto3.grid(row=1, column=1, padx=3, pady=3)
labelFoto4 = Label(master=P6, image=foto4)
labelFoto4.grid(row=1, column=1, padx=3, pady=3)

ventanaInicio.pack()
P1.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
P2.pack(side=RIGHT, fill=BOTH, padx=5, pady=5)
P3.pack(side=TOP, fill=BOTH, padx=5, pady=5)
P4.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
P5.pack(side=TOP, fill=BOTH, padx=5, pady=5)
P6.pack(side=BOTTOM, fill=BOTH, padx=5, pady=5)
saludo.pack(padx=5, pady=5)
ingreso.pack(side=BOTTOM, padx=5, pady=5)
labelFotoPlaza.pack(side=TOP, padx=10, pady=10)
tituloVida.pack(padx=5, pady=5)
cuerpoVida.pack(padx=5, pady=5)

tutorial = "Aca va el tutorial xd"

ventanaUsuario = Frame()
tituloInfo = Label(master=ventanaUsuario, text="¿Cómo usar esta aplicación y qué puede hacer con ella?", font="Helvetica 11 bold")
info = Label(master=ventanaUsuario, text=tutorial, font="Helvetica 10")
tituloInfo.pack(fill=BOTH, padx=5, pady=5)
info.pack(fill=BOTH, padx=5, pady=5)




ventanaAgregarSector = AgregarSector()
ventanaAgregarSector.pack_forget()

"""
class AgregarLocal:
    def pack_forget(self):
        pass


ventanaAgregarLocal = AgregarLocal()
ventanaAgregarLocal.pack_forget()


class RegistrarDuenho:
    def pack_forget(self):
        pass


ventanaRegistrarDuenho = RegistrarDuenho()
ventanaRegistrarDuenho.pack_forget()


class RegistrarCliente:
    def pack_forget(self):
        pass


ventanaRegistrarCliente = RegistrarCliente()
ventanaRegistrarCliente.pack_forget()


class RegistrarCodeudor:
    def pack_forget(self):
        pass


ventanaRegistrarCodeudor = RegistrarCodeudor()
ventanaRegistrarCodeudor.pack_forget()


class AlquilarLocal:
    def pack_forget(self):
        pass


ventanaAlquilarLocal = AlquilarLocal()
ventanaAlquilarLocal.pack_forget()


class MostrarLocalesDesocupados:
    def pack_forget(self):
        pass


ventanaMostrarLocalesDesocupados = MostrarLocalesDesocupados()
ventanaMostrarLocalesDesocupados.pack_forget()


class MostrarLocalesOcupados:
    def pack_forget(self):
        pass


ventanaMostrarLocalesOcupados = MostrarLocalesOcupados()
ventanaMostrarLocalesOcupados.pack_forget()


class MostrarHistorialAlquiler:
    def pack_forget(self):
        pass


ventanaMostrarHistorialAlquiler = MostrarHistorialAlquiler()
ventanaMostrarHistorialAlquiler.pack_forget()


class MostrarListadoContratosVigentes:
    def pack_forget(self):
        pass


ventanaMostrarListadoContratosVigentes = MostrarListadoContratosVigentes()
ventanaMostrarListadoContratosVigentes.pack_forget()


class Automatizacion:
    def pack_forget(self):
        pass


ventanaAutomatizacion = Automatizacion()
ventanaAutomatizacion.pack_forget()


class MostrarDatosGuardados:
    def pack_forget(self):
        pass


ventanaMostrarDatosGuardados = MostrarDatosGuardados()
ventanaMostrarDatosGuardados.pack_forget()
"""

style = ttk.Style()
style.theme_use("default")
style.map("Treeview")
style.configure("Treeview", font="Helvetica 10")
style.configure("Treeview.Heading", font="Helvetica 10")

ventana.mainloop()