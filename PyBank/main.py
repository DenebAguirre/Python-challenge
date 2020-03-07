import os
import csv

herepath = os.path.dirname(os.path.abspath(__file__))
budget_data = os.path.join(herepath,'budget_data.csv')

with open(budget_data) as budgetfile:
    reader = csv.reader(budgetfile)
    header = next(reader)
    data = [row for row in reader]
    totalmonths = len(data)
    
    #get all profit losts data in one variable
    proflos = []
    suma = 0
    for row in data:
        proflos.append(int(row[1]))

    #I get the total for once
    for i in proflos:
        suma = suma + i


    #substract each profit/losts data and get the results in changes variable
    changes = []
    n=0
   
    for i in proflos:
        n = n+1
        if n == 86:
             n = 0
        a = i - proflos[n]
        changes.append(a)
        
    #discard the last result 
    changes.pop()
    
    #Sum all changes data and get the average
    totalchanges = 0
    for y in changes:
        totalchanges = totalchanges + y
    average = totalchanges/len(changes)
    changes.insert(0, int(0))

    #Add changes results to the original data as a unified list.
    #This is where i find lot of problems, because to make proper operations i had to use integer
    #And i couldn´t paste those results to the original data. I tried it changing the int as list format
    
        #changes2 = []
        #for i in proflos:
        #    n = n+1
        #   if n == 86:
        #        n = 0
        #    a = [i - proflos[n]]
        #    changes2.append(a)

    # But it didn´t work. I tried Zip functions but if just added the data like this [´month´, ´num´] [´change´] not in the same list
        #for a in zip(data,changes):
        #    alldata.append(list(a))

    #The closest i could get to this was by a list comphrehension 
        #[x + changes2[1] for x in data]
    #This add the data in the right format but it just pasted the same value to all data
    #I tried by a iteration but it just pasted all the list data to one value

    #####By this
    #for i in changes
    #    data = [x + changes2[i] for x in data]

    ####Or by this
    # p = 0
   
    #for x in data:
    #    data = [x + changes2[p]]
    #    p = p + 1
    #    if p == 86:
    #        p = 0
    
    #So I decided to complete the tasks with the separate data
    # Firs I identifie the lowest and greates in data
    lowest2 = 0
    greatest2 = 0
    lowmonth = " "
    greatmonth2 = " "

    for row in data:
        if (int(row[1])) > greatest2:
            greatest2 = (int(row[1]))
            greatmonth = row[0]
        if (int(row[1])) < lowest2:
            lowest2 = (int(row[1]))
            lowmonth = row[0]


    #Then i identified the bigest lost and win in changes

    lowest = 0
    greatest = 0
    count1 = 0
    count2 = 0
    for row in changes:
        if row < greatest:
            greatest = row
        if row > lowest:
            lowest = row

    lowest = (-lowest)
    greatest = (-greatest)

    print("Total Months: ", totalmonths)
    print("Total: $", suma)
    print("Average change: $", round(average,2))
    print("Greatest increase in profits: ", greatmonth, "$", greatest)
    print("Greatest decrease in profits: ", lowmonth, "$", lowest)

    with open('PyBankHomework.txt', "w") as txt_file:
        txt_file.write('Total Months:' + str(totalmonths) + '\n)')
        txt_file.write("Total: $" + str(suma) + '\n)')
        txt_file.write("Average change: $" + str(round(average,2)) + '\n' )
        txt_file.write("Greatest increase in profits: " + str(greatmonth) + " $" + str(greatest) + '\n')
        txt_file.write("Greatest decrease in profits: " + str(lowmonth) + " $" + str(lowest))
        txt_file.close()
