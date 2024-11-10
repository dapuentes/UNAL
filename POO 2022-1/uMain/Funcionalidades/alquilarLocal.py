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

class AlquilarLocal(Funcionalidades):
    def __init__(self):
        super().__init__()
        self.alquilarLocal()
    def alquilarLocal(self):
        if len(self.plaza.getClientes())==0 and len(Cliente.getClientes())==0:
            print("Para alquilar un local primero debe de registrar clientes")
        elif len(self.plaza.getSectores())==0 and len(Sector.getSectores()) == 0:
            print("Para alquilar un local primero debe agregar sectores ")
        elif self.plaza.obtenerCantidadLocales() == 0 and len(Local.getLocales())==0:
            print("Para alquilar un local primero debe de agregar locales")
        else:
            cedulaCliente = Cliente.getClientes()[self.seleccionarCliente()].getCedula()
            indiceLocal= self.seleccionarLocal()
            Sector.getSectores()[indiceLocal[0]].getLocales()[indiceLocal[1]].setOcupado(True)
            local  = Sector.getSectores()[indiceLocal[0]].getLocales()[indiceLocal[1]]
            codigoLocal= local.getCodigo()
            motoMensual= local.getPrecioBase() +( Sector.getSectores()[indiceLocal[0]].getPrecioBaseM2() * local.getTamanho())
            if local.getTecho():
                motoMensual *= Plaza.PORCENTAJE_AUMENTO_CON_TECHO
            else:
                motoMensual  *= 1
            if local.getCamaraRefrigerante():
                motoMensual *= Plaza.PORCENTAJE_AUMENTO_CON_CAMARA_REFRIGETANTE
            else:
                motoMensual *= 1
            motoMensual *= 1.2
            obj = ObtenerDatos()
            contrato = Contrato()
            contrato.setNumero(len(Contrato.getContratos())+1)
            contrato.setCedulaCliente(cedulaCliente)
            contrato.setCodigoLocal(codigoLocal)
            contrato.setMontoMensual(motoMensual)
            obj.obtenerDatosContrato(contrato)
            Contrato.getContratos().append(contrato)
            print("Alquiler completado correctamente")