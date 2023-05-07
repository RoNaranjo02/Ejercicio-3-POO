from manejadorTemperatura import ManejadorT
manej = ManejadorT()
class Menuopc:
    __opcion = None
    def __init__(self):
        self.__opcion=None
    
    def menu_opciones(self):
        manej.readFile()
        print("---Menu de Opciones---")
        print("1. Mostrar para cada variable el día y hora de menor y mayor valor: ")
        print("2.Indicar la temperatura promedio mensual por cada hora: ")
        print("3.Ingrese dia para mostrar temperatura, humedad y presion atmosferica: ")
        self.__opcion=input("Seleccione una opcion: ")
        if self.__opcion =='1':
            manej.maximo()
            manej.minimo()
        elif self.__opcion == '2':
            manej.promedio()
        elif self.__opcion == '3':
            manej.temp()
    