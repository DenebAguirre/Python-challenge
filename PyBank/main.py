import os
import csv

herepath = os.path.dirname(os.path.abspath(__file__))
budget_data = os.path.join(herepath,'budget_data.csv')

with open(budget_data) as budgetfile:
    reader = csv.reader(budgetfile)
    header = next(reader)
    data = [row for row in reader]
    
    print(header)
    print(data[0])
