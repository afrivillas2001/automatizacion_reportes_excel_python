from logging import NullHandler
from operator import index
from turtle import pd
from unicodedata import name
from array import *
import numpy as np
import os
import pandas 
import sys
import matplotlib.pyplot as plt
import openpyxl


class dfConsolidated:
  dfTot = pandas.DataFrame()

  def addfiledf (self, dffile):
      self.dfTot = pandas.concat([self.dfTot, dffile])
  def output (self, path):
    self.dfTot.to_excel(path+'\\TOTAL.xlsx', sheet_name='Datos',index=False)  
    #Escribir codigo que haga la grafica de un servidor
    # Servidor RNEC-MGT-01 - Variable Average Response Time (ms)
    valores = self.dfTot[['RNEC-MGT-01'],['Average Response Time (ms)']]
    ax = valores.plot.bar(x="RNEC-MGT-01", y="Variable Average Response Time (ms)", rot = 0)
    plt.show()    
  def setrank(self):
    #Obtener servidores por variable
    df= self.dfTot.groupby(['Entity' ,'Metric']).agg({'Value': ['mean', 'max']})
    #Generar un excel de nombre RANKS.xlsx en la ubicacion de excel de metricas
    df.to_excel("RANKS.xlsx")
class myFile:
  findBroken = 'Custom Chart'  
  dfTotal = pandas.DataFrame()

  def __init__(self, pname):
      self.name = pname

  def parsefile (self):
      print ('Init parse for '+ self.name)
      csvFile = open(self.name,  encoding="utf8") 
      data=csvFile.read()
      data = data.replace(',,',',')
      csvFile.close()
      csvFile = open(self.name, mode="wt",  encoding="utf8")
      csvFile.write(data)
      csvFile.close() 
      csvFile = open(self.name,  encoding="utf8")
      csvLines = csvFile.readlines()
      csvFile.close()      
      #Obtener los separadores de cada bloque de información
      n=1
      linesid =[]
      for line in csvLines:
        if self.findBroken in line:
          linesid.append(n)
        n += 1
      #Obtener inicio y fin de cada bloque de información
      limits = [[0 for x in range(2)] for y in range(len(linesid))]
      for n in range(len(linesid)):
        if n < len(linesid)-1:
          limits[n][0]= linesid[n]+1
          limits[n][1]= linesid[n+1] - 2
        else:
          limits[n][0]= linesid[n]+1
          limits[n][1]= len(csvLines)-1
      #print(limits)
      #Armar los bloques para los CSV leyendo con read_csv cada parte del archivo
      for n in range (len(limits)):
        df = pandas.read_csv(self.name, skiprows=limits[n][0]-1,nrows=limits[n][1]-limits[n][0], quotechar='"',encoding='utf-8')
        # Hacer join entre el DataFrame df y el DataFrame dfTotal
        self.dfTotal = pandas.concat([df, self.dfTotal])
  
  def getdf(self):
    return self.dfTotal

  

      
        
#Recibir 2 parametros tipo:PERF/EVT y el directorio de trabajo
#en listdir colocar el directorio de trabajo concatenado con el tipo
#eso mismo pasarlo como variable a la clase myFile (directorio de trabajo\x)
tipo = sys.argv[1]
dir = sys.argv[2]

dir_list =  dir + '\\' + tipo 

# print(dir_list)
dfCon = dfConsolidated()

for x in os.listdir(dir_list):
  if x.endswith(".csv"):
    csv= myFile (dir_list+'\\'+x)
    csv.parsefile() 
    dfCon.addfiledf(csv.getdf())

dfCon.setrank()
dfCon.output(dir_list)



        


