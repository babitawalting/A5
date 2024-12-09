import pandas as pd
from datetime import datetime
import lib_bamboo as bamboo
import os

os.system("cls")
print("Working...")

dataBavaria = pd.read_excel("A5/excelfiles/Voetbal_Bavaria League_tussenstand.xlsx")
dataBavaria["datum"] = pd.to_datetime(dataBavaria["datum"], format="%d/%m/%Y")
dataBavaria = dataBavaria.sort_values("datum")

dataBrand = pd.read_excel("A5/excelfiles/Voetbal_Brand League_tussenstand.xlsx")
dataBrand["datum"] = pd.to_datetime(dataBrand["datum"], format="%d/%m/%Y")
dataBrand = dataBrand.sort_values("datum")

dataHeineken = pd.read_excel("A5/excelfiles/Voetbal_Heineken League_tussenstand.xlsx")
dataHeineken["datum"] = pd.to_datetime(dataHeineken["datum"], format="%d/%m/%Y")
dataHeineken = dataHeineken.sort_values("datum")

dataJupiler = pd.read_excel("A5/excelfiles/Voetbal_Jupiler League_tussenstand.xlsx")
dataJupiler["datum"] = pd.to_datetime(dataJupiler["datum"], format="%d/%m/%Y")
dataJupiler = dataJupiler.sort_values("datum")

#Informatievraag 1



#Informatievraag 2



#Informatievraag 3



#Informatievraag 4









print("Done!")
