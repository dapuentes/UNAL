#from baseDatos.deserializador import Deserializador
#from baseDatos.serializador import Serializador
from gestorAplicacion.infraestructura.plaza import Plaza
from uMain.Funcionalidades.agregarSector import AgregarSector
from uMain.Funcionalidades.alquilarLocal import AlquilarLocal
from uMain.Funcionalidades.funcionalidades import Funcionalidades
from uMain.Funcionalidades.mostrarHistorialAlquilerLocal import MostrarHistorialAlquilerLocal
from uMain.Funcionalidades.mostrarListadoContratoVigentes import MostrarListadoContratosVigentes
from uMain.Funcionalidades.mostrarLocalesDesocupados import MostrarLocalesDesocupados
from uMain.Funcionalidades.mostrarLocalesOcupados import MostrarLocalesOcupados
from uMain.Funcionalidades.registrarCliente import RegistrarCliente
from uMain.Funcionalidades.registrarCodeudor import RegistrarCodeudor
from uMain.Funcionalidades.registrarDuenho import RegistrarDuenho


class Main():
    def __init__(self):
        pass

    def run(self):
        opcion = -1
        #self.cargar()
        while opcion != 12:
            opc = self.menu()
            if opc == 1:
                obj= AgregarSector()
                obj.agregarSector()
                #self.guardar()
            elif opc == 2:
                obj= AgregarSector()
                obj.agregarLocal()
                #self.guardar()
            elif opc == 3:
                obj= RegistrarDuenho()
                obj.registrarDuenho()
                #self.guardar()
            elif opc == 4:
                obj = RegistrarCliente()
                obj.registrarCliente()
                #self.guardar()
            elif opc == 5:
                obj = RegistrarCodeudor()
                obj.registrarCodeudor()
                #self.guardar()
            elif opc == 6:
                obj= AlquilarLocal()
                obj.alquilarLocal()
            elif opc == 7:
                obj= MostrarLocalesDesocupados()
                obj.mostrarLocalesDesocupados()
            elif opc == 8:
                obj = MostrarLocalesOcupados()
                obj.mostrarLocalesOcupados()
            elif opc == 9:
                obj = MostrarHistorialAlquilerLocal()
                obj.mostrarHistorialAlquilerLocal()
            elif opc == 10:
                obj = MostrarListadoContratosVigentes()
                obj.mostrarListadoContratosVigentes()
            elif opc == 11:
                pass
                #obj.opcionesAvanzadas()
            elif opc == 12:
                print("Saliendo del sistema ...")
                self.guardar()
            else:
                print("Opcion no valida")

    def menu(self):
        print("Menu - Sistema de la plaza '" + Plaza.nombre + "'"
                            + "\n\n1) Agregar sector a la plaza"
                            + "\n2) Agregar local a un sector"
                            + "\n3) Registrar dueño"
                            + "\n4) Registrar cliente"
                            + "\n5) Registrar codeudor"
                            + "\n6) Alquilar local"
                            + "\n7) Mostrar locales desocupados"
                            + "\n8) Mostrar locales ocupados"
                            + "\n9) Mostrar historial de alquiler de un local"
                            + "\n10) Mostrar listado de contratos vigentes"
                            + "\n11) Opciones avanzadas"
                            + "\n12) Salir"
                            + "\n\nSeleccione una opcion")
        opc=int(input())
        return opc

inicio = Main()
inicio.run()