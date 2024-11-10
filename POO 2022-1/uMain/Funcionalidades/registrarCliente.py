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

class RegistrarCliente(Funcionalidades):
    def __init__(self):
        super().__init__()
        self.registrarCliente()
    def registrarCliente(self):
        obj = ObtenerDatos()
        if len(self.plaza.getCodeudores())==0 and len(self.plaza.getCodeudores()) == 1 or len(Codeudor.getCodeudores())==0 and len(Codeudor.getCodeudores()) == 1:
            print("Para registrar un cliente deben existir por lo menos 2 codeudores ")
        else:
            cedulaCliente = -1
            cedulaExistente=True

            while cedulaExistente:
                cedulaCliente= int(input("Ingrese la cedula del cliente"))
                try:
                    ExcepcionPresenciaDatos.presenciaDatos(["cedula"],cedulaCliente)
                except ExcepcionPresenciaDatos:
                    return
                try:
                    ExcepcionTipoInt.tipoInt(["cedula"],cedulaCliente)
                except ExcepcionTipoInt:
                    return
                if self.plaza.buscarCliente(cedulaCliente) != -1:
                    print("Esta cedula ya existe, por favor ingrese una distinta ")
                else:
                    cedulaExistente = False
            nuevoCliente = Cliente()
            nuevoCliente.setCedula(cedulaCliente)
            obj.obtenerDatosCliente(nuevoCliente)
            cedulaCodeudor1 = Codeudor.getCodeudores()[self.seleccionarCodeudor(1)].getCedula()
            cedulaCodeudor2 = cedulaCodeudor1
            while cedulaCodeudor1 == cedulaCodeudor2:
                cedulaCodeudor2= Codeudor.getCodeudores()[self.seleccionarCodeudor(2)].getCedula()
                if cedulaCodeudor1 == cedulaCodeudor2:
                    print("Los codeudores deben ser distintos")
            Cliente.getClientes().append(nuevoCliente)
            print("Cliente registrado correctamente ")