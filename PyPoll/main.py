import os
import csv

#I found this os function, to refer the actual path
herepath = os.path.dirname(os.path.abspath(__file__))
election_data = os.path.join(herepath,'election_data.csv')

#Open files
with open(election_data) as electionfile:
    reader = csv.reader(electionfile)
    header = next(reader)
    data = [row for row in reader]
    #Totalvotes
    totalvotes = len(data)

    #Identifie candidates
    candidates = []
    for row in data:
        if row[2] not in candidates:
            candidates.append(row[2])
    
    #Make a counter between a dictionary
    votes = {i : 0 for i in candidates}

    #Count votes
    for row in data:
        if row[2] in votes:
           votes[row[2]] = votes[row[2]] + 1
    
    #Find winner
    winner = max(votes, key=votes.get)

    #Make percentages 
    percentages = {i : ("{:.2%}".format(votes[i]/totalvotes)) for i in candidates}

    #Print results
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes: ", totalvotes)
    print("-----------------------------------")
    for x in candidates:
        print(x,":", percentages[x],votes[x])
    print("-----------------------------------")
    print("Winner: ", winner) 

    with open("PyPollHomework.txt", "w") as text_file:
        text_file.write("Election Results" + "\n")
        text_file.write("-----------------------------------" + "\n")
        text_file.write("Total Votes: " + str(totalvotes) + "\n")
        text_file.write("-----------------------------------" + "\n")
        for x in candidates:
            text_file.write(str(x) + ":" + str(percentages[x]) + str(votes[x]) + "\n")
        text_file.write("-----------------------------------" + "\n")
        text_file.write("Winner: " + str(winner))
        text_file.close()



   

            
    
   

        

   


  



 
 