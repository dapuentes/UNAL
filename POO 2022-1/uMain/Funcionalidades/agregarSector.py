from tkinter import Frame, BOTH, messagebox, Label, Button, LEFT, RIGHT

import tk as tk

from uMain.excepciones.excepcionTipoFloat import ExcepcionTipoFloat
from uMain.excepciones.excepcionTipoString import ExcepcionTipoString


from uMain.excepciones.excepcionPresenciaDatos import ExcepcionPresenciaDatos
from uMain.excepciones.excepcionTipoInt import ExcepcionTipoInt
from gestorAplicacion.clientes.cliente import Cliente
from gestorAplicacion.clientes.codeudor import Codeudor
from gestorAplicacion.clientes.duenho import Duenho
from gestorAplicacion.infraestructura.Sector import Sector
from gestorAplicacion.infraestructura.contrato import Contrato
from gestorAplicacion.infraestructura.local import Local
from gestorAplicacion.infraestructura.plaza import Plaza
from uMain.Funcionalidades.funcionalidades import Funcionalidades
from uMain.ObtenerDatos import ObtenerDatos
import datetime

from uMain.fieldFrame import FieldFrame


class AgregarSector(Frame):

    def __init__(self):
        super().__init__()
        nombre = Label(master=self, text="Agregar Sector", font = ("Helvetica", 12))
        info = "Hola"
        descripcion = Label(master=self, text=info, font = ("Helvetica", 12))
        nombre.pack(fill=BOTH, padx=5, pady=5)
        descripcion.pack(fill=BOTH, padx=5, pady=5)


        self.criterios = ["Ingrese el nombre del sector", "Ingrese el precio base por m2 del sector"]

        self.valores = ["", 0]

        self.habilitados = [True, True]

        self.combobox = None

        self.dialogos = FieldFrame(self)
        self.dialogos.pack(padx=5, pady=5)

        botones = Frame(master=self)
        aceptar = Button(master=botones, text="Aceptar", font=("Helvetica", 12), command=self.aceptar)
        aceptar.pack(side=LEFT, padx=5, pady=5)
        borrar = Button(master=botones, text="Borrar", font=("Helvetica", 12), command=self.borrar)
        borrar.pack(side=RIGHT, padx=5, pady=5)

    def borrar(self):
        self.dialogos.getComponente("Ingrese el nombre del sector").set("")
        self.dialogos.getComponente("Ingrese el precio base por m2 del sector").set(0)

    def aceptar(self):
        nombre = self.dialogos.getComponente("Ingrese el nombre del sector").get()
        precio = self.dialogos.getComponente("Ingrese el precio base por m2 del sector").get()
        if nombre == "" or precio == "":
            messagebox.showinfo("Error", "Debe ingresar todos los datos")
        else:
            try:
                precio = float(precio)
                sector = Sector(nombre, precio)
                sector.agregarSector()
                messagebox.showinfo("Exito", "Sector agregado")
            except ExcepcionTipoFloat:
                messagebox.showinfo("Error", "El precio debe ser un numero")
            except ExcepcionTipoString:
                messagebox.showinfo("Error", "El nombre debe ser un string")
            except ExcepcionPresenciaDatos:
                messagebox.showinfo("Error", "El sector ya existe")
            except ExcepcionTipoInt:
                messagebox.showinfo("Error", "El precio debe ser un numero")
            except Exception as e:
                messagebox.showinfo("Error", "Error desconocido")
                print(e)



