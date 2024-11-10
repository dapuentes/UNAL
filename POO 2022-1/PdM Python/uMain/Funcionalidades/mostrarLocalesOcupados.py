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

class MostrarLocalesOcupados(Funcionalidades):
    def __init__(self):
        super().__init__()
        self.mostrarLocalesOcupados()
    def mostrarLocalesOcupados(self):
        local= Local()
        listado= "Listado de los locales ocupados\n\n"

        for i in range(len(local.getLocales())):
            local = Local.getLocales()[i]
            if local.isOcupado() == True:
                listado += "\n" + local.retornarInformacion()+"\n\n"
            else:
                print("No hay locales ocupados\n")

            print(listado)