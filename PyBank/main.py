import os
import csv

herepath = os.path.dirname(os.path.abspath(__file__))
budget_data = os.path.join(herepath,'budget_data.csv')

with open(budget_data) as budgetfile:
    reader = csv.reader(budgetfile)
    header = next(reader)
    data = [row for row in reader]
    totalmonths = len(data)
    
    proflos = []
    suma = 0
    for row in data:
        proflos.append(int(row[1]))

    for i in proflos:
        suma = suma + i
    

    changes = []
    n=0
   
    for i in proflos:
        n = n+1
        if n == 86:
             n = 0
        a = i - proflos[n]
        changes.append(a)
        
    changes.pop()
    
    totalchanges = 0
    for y in changes:
        totalchanges = totalchanges + y

    average = totalchanges/85  
    
    changes.insert(0, int(0))
    
    Alldata = zip(data,changes)

    print(Alldata)
        
    
    
