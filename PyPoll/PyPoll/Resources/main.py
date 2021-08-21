import os
import csv

filename = "election_data.csv"

#open and read csv
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    #skip the headers
    next(csvreader)

    #create a variable to calculate the total number of votes cast
    num_rows=0

    #create an empty list to store all candidates from column Candidate
    candidatelist=[]

    #create an empty list to store the name of each candidate
    updated_candidatelist=[]

    #loop through each row in the dataset
    for row in csvreader:

        num_rows+=1

        #appending all candidates name onto candidatelist
        candidatelist.append(row[2])

    #loop through every element in candidatelist
    for i in candidatelist:

        #add the name of the candidate from candidatelist to updated_candidatelist if the name cannot be found in updated_candidatelist
        if i not in updated_candidatelist:
            updated_candidatelist.append(i) 

    print("Election Results")

    print("----------------------")

    #print the total number of votes cast
    print("Total Votes: "+str(num_rows))   

    print("----------------------")
    
    #create a variable to find the greatest votes count
    max_votes=0
    
    #loop through each candidate in the updated_candidatelist
    for candidate in updated_candidatelist:

        #percentage of votes each candidate won=(total number of votes each candidate won/total number of votes cast)x100%
        percent_votes=round((candidatelist.count(candidate)/num_rows)*100,3)
        #count the total number of votes each candidate won
        total_votes=candidatelist.count(candidate)

        #compare the total number of votes each candidate won with the variable and assign to the variable if they are greater
        if total_votes>max_votes:
            max_votes=total_votes
            winner=candidate

        #A complete list of candidates who received votes
        #The percentage of votes each candidate won
        #The total number of votes each candidate won
        print(candidate+": "+str(percent_votes)+"%"+" ("+str(total_votes)+")")

    print("----------------------")

    print("Winner: "+winner)

    print("----------------------")

    #export results to a text file
    output_path=os.path.join("Analysis","pypoll.txt")
    txt_file=open("output_path","w")
    txt_file.write("Election Results\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Total Votes: {num_rows}\n")
    txt_file.write("-----------------------------\n")
    for candidate in updated_candidatelist:

        percent_votes=round((candidatelist.count(candidate)/num_rows)*100,3)
        total_votes=candidatelist.count(candidate)

        txt_file.write(f"{candidate}: {percent_votes}% ({total_votes})\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Winner: {winner}\n")
    txt_file.write("-----------------------------\n")
    txt_file.close()
        