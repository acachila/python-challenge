import csv
import os

# choose 1 or 2
file_num = 2

# create file path and save as file
file = os.path.join('raw_data', 'budget_data_'+ str(file_num) +'.csv')

#emply lists for month and revenue data
months = []
Profit_Losses = []

#read csv and parse data into lists
#Profit_Losses list will be list of integers
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        Profit_Losses.append(int(row[1]))

#find total months
total_months = len(months)

#create greatest increase, decrease variables and set them equal to the first revenue entry
#set Profit_Losses = 0 
greatest_inc = Profit_Losses[0]
greatest_dec = Profit_Losses[0]
Total_Profit_Losses = 0

#loop through revenue indices and compare # to find greatest inc and dec
#also add each revenue to total revenue
for r in range(len(Profit_Losse)):
    if Profit_Losses[r] >= greatest_inc:
        greatest_inc = Profit_Losses[r]
        great_inc_month = months[r]
    elif Profit_Losses[r] <= greatest_dec:
        greatest_dec = Profit_Losses[r]
        great_dec_month = months[r]
    Total_Profit_Loss += Profit_Losses[r]

#calculate average_change
average_change = round(total_Profit_Loss/total_months, 2)

#sets path for output file
output_dest = os.path.join('Output','pybank_output_' + str(file_num) + '.txt')

# opens the output destination in write mode and prints the summary
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Profit/Loss: $' + str(Profit_Losses) + '\n')
    writefile.writelines('Average Profit Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profit: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Loss: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#opens the output file in r mode and prints to terminal
with open(output_dest, 'r') as readfile:
    print(readfile.read())
