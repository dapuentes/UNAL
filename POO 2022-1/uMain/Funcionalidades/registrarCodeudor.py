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

class RegistrarCodeudor(Funcionalidades):
    def __init__(self):
        super().__init__()
        self.registrarCodeudor()
    def registrarCodeudor(self):
        obj = ObtenerDatos()
        cedulaCodeudor= -1
        cedulaExistente = True
        while cedulaExistente:
            cedulaCodeudor = int(input("Ingrese la cedula del codeudor"))
            try:
                ExcepcionPresenciaDatos.presenciaDatos(["cedula"],cedulaCodeudor)
            except ExcepcionPresenciaDatos:
                return
            try:
                ExcepcionTipoInt.tipoInt(["cedula"],cedulaCodeudor)
            except ExcepcionTipoInt:
                return
            if self.plaza.buscarCodeudor(cedulaCodeudor)!= -1:
                print("Esta cedula ya existe, por favor ingrese una distinta")
            else:
                cedulaExistente= False
        nuevoCodeudor= Codeudor()
        nuevoCodeudor.setCedula(cedulaCodeudor)
        obj.obtenerDatosCodeudor(nuevoCodeudor)
        self.plaza.setCodeudores(nuevoCodeudor)
        print("Codeudor registrado correctamente")