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

class MostrarHistorialAlquilerLocal(Funcionalidades):
    def __init__(self):
        super().__init__()
        self.mostrarHistorialAlquilerLocal()
    def mostrarHistorialAlquilerLocal(self):
        if self.plaza.obtenerCantidadLocales() == 0 and len(Local.getLocales())==0:
            print("No hay locales actualemente")
        else:
            indicesLocal= self.seleccionarLocal()
            local= Sector.getSectores().get(indicesLocal[0]).getLocales().get(indicesLocal[1])

            informacion = "Historial de alquiler del local con codigo: "+local.getCodigo()+"\n\n"
            totalDineroAdministracion = 0
            for contrato in Contrato.getContratos():
                informacion += contrato.retornarInformacion() + "\n"
                totalDineroAdministracion += contrato.getMontoMensual()
            informacion += "\nTotal de dinero recaudado perteneciente a admnistracion: $" + totalDineroAdministracion + "\n"
            print(informacion)