# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os
print("Current working directory:", os.getcwd())

# Files to load and output (update with correct file paths)
input_file =   os.path.join( "Resources", "budget_data.csv")  # Input file path
output_file = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
months = []
profits = []
changes = []

# Open and read the csv
with open(input_file) as budget_data:
    reader = csv.reader(budget_data)

    # Skip the header row
    header = next(reader)
    #print(header)
#add the month and profit/loss to the list
    for row in reader:
        months.append(row[0])  # Add the month to the list
        profits.append(int(row[1]))  # Add profit/loss to the list


# Track the total and net change
total_months = len(months)
total_profit_loss = sum(profits)
#print the total and net change
print(f"Total Months: {total_months}")
print(F"Total: {total_profit_loss}")


    # itterate through each row of data
for i in range(1, total_months):
        changes.append(profits[i] - profits[i - 1])
# calculate the average_change
average_change = round(sum(changes) / len(changes),2)
# print the average_change
print(f"Average Change: {average_change}")

        # Calculate the greatest increase in profits (month and amount)
greatest_increase = max(changes)
greatest_increase_month = months[changes.index(greatest_increase) + 1]
#the greatest increase in profits
print(F"Greatest Increase in Profits: {greatest_increase_month} {greatest_increase}")

# Calculate the greatest decrease in losses (month and amount)
greatest_decrease = min(changes)
greatest_decrease_month = months[changes.index(greatest_decrease) + 1]
#print greatest decrease in losses
print(F"Greatest Decrease in Profits:{greatest_decrease_month} {greatest_decrease}")

with open(output_file, 'w') as file:
    
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total Profit/Loss: ${total_profit_loss}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase}\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease}\n")




    
