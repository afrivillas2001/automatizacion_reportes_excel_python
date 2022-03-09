from operator import index
import pandas as pd
import openpyxl
import webbrowser
import time
import numpy as np

book = openpyxl.load_workbook("./TIGO.xlsx", data_only=True)
hoja = book.active
celdas = hoja["F2":"F98"]
n = 1
opcion = ["evt", "perf", "alerts"]
print("Opcion: " + "0 = perf, 1 = evt, 2= alerts")
opcion_url = int(input())




for fila in celdas:
    codigo = [celdas.value for celdas in fila]
    if codigo != [None]:
        if opcion_url == 0:
            url= f"https://solarwinds.une.com.co/ui/perfstack/?context=0_Orion.Nodes_{codigo[0]}&withRelationships=true&charts=0_Orion.Nodes_{codigo[0]}-Orion.CPULoad.AvgLoad;0_Orion.Nodes_{codigo[0]}-Orion.CPULoad.MaxLoad;0_Orion.Nodes_{codigo[0]}-Orion.CPULoad.AvgPercentMemoryUsed;0_Orion.Nodes_{codigo[0]}-Orion.CPULoad.MaxMemoryUsed;0_Orion.Nodes_{codigo[0]}-Orion.CPULoad.AvgMemoryUsed;0_Orion.Nodes_{codigo[0]}-Orion.ResponseTime.AvgResponseTime;&startTime=2022-01-01T05:00:00.000Z&endTime=2022-03-01T05:00:00.000Z"
        else:
            if opcion_url == 1:
                url= f"https://solarwinds.une.com.co/ui/perfstack/?context=0_Orion.Nodes_{codigo[0]}&withRelationships=true&charts=0_Orion.Nodes_{codigo[0]}-Orion.PerfStack.Events;0_Orion.Nodes_{codigo[0]}-Orion.PerfStack.Status;0_Orion.Nodes_{codigo[0]}-Orion.PerfStack.Changes.ScmChanges;&startTime=2022-01-01T05:00:00.000Z&endTime=2022-03-01T05:00:00.000Z"
            else:
                if opcion_url == 2:
                    url= f"https://solarwinds.une.com.co/ui/perfstack/?context=0_Orion.Nodes_{codigo[0]}&withRelationships=true&charts=0_Orion.Nodes_{codigo[0]}-Orion.PerfStack.Alerts;&startTime=2022-01-01T05:00:00.000Z&endTime=2022-03-01T05:00:00.000Z"
                else:
                    print ("Opción NO Valida")        
        if n <= 1:
          webbrowser.open_new_tab(url)
          time.sleep(25)
        else:
          n=0 
          #input("press enter to continue...")
          webbrowser.open_new_tab(url)
          time.sleep(25)
        n = n+1   
        
