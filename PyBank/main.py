''' PyBank Instructions
 
Your task is to create a Python script that analyzes the records to calculate each of the following values:

Financial Analysis
----------------------------
Total Months: 86
Total: $22564198
Average Change: $-8311.11
Greatest Increase in Profits: Aug-16 ($1862002)
Greatest Decrease in Profits: Feb-14 ($-1825558)

In addition, your final script should both print the analysis to the terminal and export a text file with the results.'''


#import modules
import os
import csv

#path to collect data 
budget_data_csv = os.path.join ("Resources", "budget_data.csv")

#set variables
total_months = 0
total_amount = 0
previous_income = 0
income_change = 0
income_average = 0

    #lists
income = []
monthly_change = []
income_changes_list = []
greatest_profit_increase = ["", 0]
greatest_profit_decrease = ["", 9999999]

#read the csv file
with open(budget_data_csv) as csvfile:
    
    #open and read the CSV
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
    #loop through the data to find total months
    for row in csvreader:
        
        #count the total months (+= add 1 to total months and assign the result)
        total_months += 1
        
        #calculate the total
        total_amount = total_amount + float(row[1])
        
        #calculate total change over the months
        income_change = income_change + float(row[1])
        
        #average change in income over the months
        income_change = float(row[1]) - previous_income
        previous_income = float(row[1])
        income_changes_list = income_changes_list + [income_change]
        monthly_change = [monthly_change] + [row[0]]
        
        #greatest increase
        if income_change > greatest_profit_increase[1]:
            greatest_profit_increase[1] = income_change
            greatest_profit_increase[0] = row[0]
        
        #greatest decrease
        if income_change < greatest_profit_decrease[1]:
            greatest_profit_decrease[1] = income_change
            greatest_profit_decrease[0] = row[0]
    income_average = sum(income_changes_list) / len(income_changes_list)
        
        
    
    
#print results 
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {int(total_months)}")
print(f"Total: ${int(total_amount)}")
print(f"Average Change: ${int(income_average)}")
print(f"Greatest Increase In Profits: {(greatest_profit_increase[0], greatest_profit_increase[1])}")
print(f"Greatest Decrease In Profits: {(greatest_profit_decrease[0], greatest_profit_decrease[1])}")


#output results to txt
with open('analysis.txt', 'w') as f:

    #print results into folder
    f.write("Financial Analysis")
    f.write("-------------------------------------")
    f.write(f"Total Months: {int(total_months)}")
    f.write(f"Total: ${int(total_amount)}")
    f.write(f"Average Change: ${int(income_average)}")
    f.write(f"Greatest Increase In Profits: {(greatest_profit_increase[0], greatest_profit_increase[1])}")
    f.write(f"Greatest Decrease In Profits: {(greatest_profit_decrease[0], greatest_profit_decrease[1])}")
        


