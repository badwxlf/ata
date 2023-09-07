import csv
from datetime import datetime

wrong_names = []
grups = {}

with open('nomes_teste.csv') as csvfile:C:\
    spamreader = csv.reader(csvfile, delimiter=';')
    next(spamreader)
    for row in spamreader:
        grups[row[0]] = []

with open('input_2.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    next(spamreader)
    for row in spamreader:
        name,entrada,saida = row
        
        if name in grups:
            entrada = datetime.strptime(entrada,"%H:%M")
            saida = datetime.strptime(saida,"%H:%M")
            res1 = saida - entrada
            hours = int(res1.seconds/3600)
            minutes = (res1.seconds % 3600) / 60
            print (hours,  minutes) 
            grups[name].append(minutes)
        else:
            wrong_names.append(row)

#for row in grups:
 #   print (grups[row])