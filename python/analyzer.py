import pandas as pd
from datetime import datetime
import lib_bamboo as bamboo
import os

os.system("cls")
print("Working...")

dataBavaria = pd.read_excel("excelfiles/Voetbal_Bavaria League_tussenstand.xlsx")
dataBavaria["datum"] = pd.to_datetime(dataBavaria["datum"], format="%d/%m/%Y")
dataBavaria = dataBavaria.sort_values("datum")


#Informatievraag 1

totalViolations = dataBavaria["overtredingen"].sum()

#Informatievraag 2

averageViolations = dataBavaria["overtredingen"].mean()

#Informatievraag 3



#Informatievraag 4


print("Done!")
