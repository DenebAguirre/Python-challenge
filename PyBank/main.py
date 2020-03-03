import os
import csv

herepath = os.path.dirname(os.path.abspath(__file__))
budget_data = os.path.join(herepath,'budget_data.csv')

with open(budget_data) as budgetfile:
    reader = csv.reader(budgetfile)
    header = next(reader)
    data = [row for row in reader]
    totalmonths = len(data)
    print(totalmonths)
    proflos = []
    suma = 0
    for row in data:
        proflos.append(int(row[1]))

    for i in proflos:
        suma = suma + i
    
    print(suma)

  

