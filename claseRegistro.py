class registro:
    __temperatura = None
    __humedad = None
    __presionAtmosf = None
    
    def __init__(self,  temperatura=float, humedad=None, presionAtmosf=None):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presionAtmosf = presionAtmosf
    
    def __str__(self):
        return("Temperatura: {}",self.__temperatura,"Humedad: {}",self.__humedad,"Presion Atmosferica: {}",self.__presionAtmosf)
    
    def gettemp(self):
        return self.__temperatura
    