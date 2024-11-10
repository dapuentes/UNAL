from tkinter import Frame, BOTH

from excepciones.excepcionPresenciaDatos import ExcepcionPresenciaDatos
from excepciones.excepcionTipoInt import ExcepcionTipoInt
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


class RegistrarDuenho(Funcionalidades):
    def __init__(self):
        super().__init__()
        self.registrarDuenho()

    def registrarDuenho(self):
        obj = ObtenerDatos()
        cedulaDuenho = -1
        cedulaExistente = True

        while cedulaExistente:
            cedulaDuenho = int(input("Ingrese la cedula del dueño "))

            if self.plaza.buscarDuenho(cedulaDuenho) != -1:
                print("Esta cedula ya existe, por favor ingrese una distinta ")
            else:
                cedulaExistente = False
        nuevoDuenho = Duenho()
        nuevoDuenho.setCedula(cedulaDuenho)
        obj.obtenerDatosDuenho(nuevoDuenho)

        self.plaza.getDuenhos().append(nuevoDuenho)
        print("Dueño registrado correctamente")