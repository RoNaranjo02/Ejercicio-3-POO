import csv
from claseRegistro import registro
reg = registro()
class ManejadorT():
     __listaB=[]
     def __init__(self):
        self.__listaB = []

     def readFile(self):
         d = 30
         h = 24
         archivo = open("temperatura.csv")
         reader = csv.reader(archivo,delimiter=',')
         next(reader)
         for i in range(d):
             self.__listaB.append([registro(0,0,0)]*h)
         for fila in reader:
             dia = (fila[0])
             hora = (fila[1])
             reg = registro(fila[2], float(fila[3]), fila[4])
             self.__listaB[dia-1][hora-1]=reg
             
     def maximo(self):
         max = 0
         for i in range(self.__listaB):
             for j in range(self.__listaB):
                 if max < self.__lista[i][j].gettemp():
                     max = self.__lista[i][j]
             print("La temperatura maxima del dia {}",i,"fue de {}", max)
     def minimo(self):
        min= 99999999
        for i in range(self.__listaB):
             for j in range(self.__listaB):
                 if min> self.__lista[i][j].gettemp():
                     min = self.__lista[i][j]
             print("La temperatura minima del dia {}",i,"fue de {}", min)
     def promedio(self):
        for i in range(len(self.__listaB[0])):
            promedio = 0.0
            for j in range(len(self.__listaB)):
                    promedio += self.__listaB[j][i].getTemperatura()
            print("Promedio de temperatura mensual hora {}: {}".format(i,promedio/len(self.__listaB)))
     def temp(self):
        dia = int(input("indicar numero de dia: "))
        print ("    Hora       Temperatura       Humedad       Presion")
        for i in range(len(self.__listaB[dia-1])):
                print("    {}           {}                  {}            {}".format(i,self.__listaB[dia-1][i].getTemperatura(),self.__listaB[dia-1][i].getHumedad(),self.__listaB[dia-1][i].getPresion()))
            
    #  def mostrar(self):
    #         for dia in self.lista:
    #             print("-------Dia: {}".format(self.__lista.index(dia)+1))
    #             for fila in dia: 
    #                 print(fila)



        
#     def readFile(self):
#         reg = registro()
#         archivo = open("temperatura.csv")
#         reader = csv.reader(archivo, delimiter=',')
#         for fila in reader:
#             reg = registro(fila[2], fila[3], fila [4])
#             self.__listaB.append(reg)
#         archivo.close()
        
#     def mostrar(self):
#         print(self.__listaB)        
        