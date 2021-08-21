import os
import csv

filename = "budget_data.csv"

#open and read csv
with open(filename) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    
    #skip the headers
    next(csvreader)

    #create an empty list to store the date
    months=[]

    #create a variable to store the net_total
    net_total =0

    #create an empty list to store the profitloss
    list=[]

    #loop through each row in the dataset
    for row in csvreader:

        #convert the list "profit/loss" into integer
        profitloss=int(row[1])

        #add the date into the list
        months.append(row[0])

        #add profit/loss to the net_total
        net_total=net_total+profitloss

        #add all the profit/loss into the list
        list.append(profitloss)

        change=0

        greatest_increase=0

        greatest_decrease=0

        #loop through all the profitloss value in the list
        for i in range(len(list)-1):
            
            #calculate the average of the changes in "Profit/Losses" over the entire period, round to 2 d.p
            change=change+((list[i+1])-list[i])
            average_change=round(change/(len(months)-1),2)

            #find the greatest increase in profits 
            if ((list[i+1])-list[i])>greatest_increase:
                greatest_increase=((list[i+1])-list[i])
                #find the index for the greatest increase in profits
                greatest_increase_index=i+1

            #find the greatest decrease in profits
            if ((list[i+1])-list[i])<greatest_decrease:
                greatest_decrease=((list[i+1])-list[i])
                #find the index for the greatest decrease in profits
                greatest_decrease_index=i+1

    print("Financial Analysis")

    print("-----------------------------")

    #print the total number of months included in the dataset
    print("Total Months: "+str(len(months)))

    #print the net total amount of profit/lossess over the entire period 
    print("Total: $"+str(net_total))

    #print the average of the changes in "Profit/Lossess"over the entire period       
    print("Average Change: $"+str(average_change))

    #print the greatest increase in profits (date and amount) over the entire period
    print("Greatest Increase in Profits: "+months[greatest_increase_index]+" ($"+str(greatest_increase)+")")
      
    #print the greatest increase in profits (date and amount) over the entire period
    print("Greatest Decrease in Profits: "+months[greatest_decrease_index]+" ($"+str(greatest_decrease)+")")

    #export the result to a text file
    output_path=os.path.join("Analysis","pybank.txt")
    txt_file=open("output_path","w")
    txt_file.write("Financial Analysis\n")
    txt_file.write("-----------------------------\n")
    txt_file.write(f"Total Months: {len(months)}\n")
    txt_file.write(f"Total: ${net_total}\n")
    txt_file.write(f"Average Change: ${average_change}\n")
    txt_file.write(f"Greatest Increase in Profits: {months[greatest_increase_index]} (${greatest_increase})\n")
    txt_file.write(f"Greatest Decrease in Profits: {months[greatest_decrease_index]} (${greatest_decrease})\n")
    txt_file.close()