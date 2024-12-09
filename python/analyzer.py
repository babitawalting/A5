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
file = open("files/total.txt", "w", encoding="UTF-8")
file.write(f"{totalViolations}")
file.close()

#Informatievraag 2

averageViolations = dataBavaria["overtredingen"].mean()
file2 = open("files/average.txt", "w", encoding="UTF-8")
file2.write(f"{averageViolations}")
file2.close()

#Informatievraag 3
dataSorted = dataBavaria.sort_values("overtredingen", ascending=False)
top10 = dataSorted.head(10)

file3 = open("files/zwartboek.txt", "w", encoding="UTF-8")
file3.write(bamboo.prettify(top10, type="zwartboek"))
file3.close()


#Informatievraag 4



print("Done!")
