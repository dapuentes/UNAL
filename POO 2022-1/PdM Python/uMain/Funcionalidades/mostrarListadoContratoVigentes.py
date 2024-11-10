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

class MostrarListadoContratosVigentes(Funcionalidades):
    def __init__(self):
        super().__init__()
        self.mostrarListadoContratosVigentes()
    def mostrarListadoContratosVigentes(self):
        try:
            fechaBusquedaSTR = input("Ingrese la fecha a buscar (Año/Mes/Dia)")
            fechaBusqueda = datetime.datetime.strptime(fechaBusquedaSTR, "%Y/%m/%d")
            listado = "Listado de contratos vigentes\n\n" + fechaBusquedaSTR + "\n\n"
            for contrato in self.plaza.getContratos():
                if fechaBusqueda-contrato.getFechaInicio() >= datetime.timedelta(days=0) and fechaBusqueda-contrato.getFechaFin() < datetime.timedelta(days=0):
                    listado += contrato.retornarInformacion() + "\n"
            for contrato in Contrato.getContratos():
                if fechaBusqueda - contrato.getFechaInicio() >= datetime.timedelta(
                        days=0) and fechaBusqueda - contrato.getFechaFin() < datetime.timedelta(days=0):
                    listado += contrato.retornarInformacion() + "\n"
            print(listado)
        except ValueError:
            print("La fecha ingresada no es valida" + "\n")