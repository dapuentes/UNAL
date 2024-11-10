from uMain.Funcionalidades.funcionalidades import Funcionalidades
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
from uMain.ObtenerDatos import ObtenerDatos
import datetime

class AgregarLocal(Funcionalidades):
    def __init__(self):
        super().__init__()
        self.agregarLocal()
    def agregarLocal(self):
        criterio= ["codigo de sector"]
        if len(self.plaza.getSectores()) == 0 and len(Sector.getSectores())== 0 :
            print("Antes de agregar locales debe de agregar sectores a la plaza ")
        elif len(self.plaza.getDuenhos())==0 and len(Duenho.getDuenhos())== 0:
            print("Antes de agregar locales debe agregar dueños")
        else:
            codigoSector = -1
            indiceSector= -1
            while indiceSector == -1:

                print("Ingrese el codigo del sector donde sera agregado el local "+ self.plaza.mostrarSectores())
                codigoSector = int(input())
                try:
                    ExcepcionPresenciaDatos.presenciaDatos(criterio,codigoSector)
                except ExcepcionPresenciaDatos:
                    return

                try:
                    ExcepcionTipoInt.tipoInt(criterio,codigoSector)
                except ExcepcionTipoInt:
                    return
                indiceSector = self.plaza.buscarSector(codigoSector)
                if indiceSector== -1:
                    print("Ingrese un codigo de sector valido ")
            self.agregarLocales(Duenho.getDuenhos(), self.plaza.obtenerCantidadLocales())