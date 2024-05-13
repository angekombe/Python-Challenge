#import os and csv modules: 
#load budget_data.csv file using os.joint()   

#track the following:
#totalmonths  by initialize to 0 
#total net profit / losses by initialize to 0 
#list of changes between months of profit/losses by initialize to []

#read the csv file and convert 

#   csv reader that separarted data using the "," as delimiter 
#   skip the header using next()  
#        index 0 represents date / month 
#        index 1 represents   profit /loss 

#   add 1 on to the month 
#   total months = total months + 1 -> use +=1 here 
#   get the first row by calling next() 
#   add on to the total net profit loss -> total net profit loss +=first row [1] 
#   initialize your previous data as first row [1]

#  loop trought the rest of the csv reader (row):
#   for row in reader 
#       add 1 on to the month 
#       total months = total months + 1 -> use +=1 here
#       add on to the total net profit loss -> total net profit loss +=first row [1] 
#       track the net change -> row [1] - previous 
#       add the net change to the list of the net change  then used .append(net change) 
#       update previous to row  

import os 
import csv

fileLoad = os.path.join("Resources","budget_data.csv") 
FinacialAnalysis = os.path.join("Financial Analysis.txt")

totalMonths = 0 
totalRevenue = 0 
monthlychanges = []  
months = []
greatestIncrease =["", 0] 
greatestDecrease =["", 999999]

with open(fileLoad) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",") 

    header = next(csvreader)  
    FirstRow = next(csvreader) 

    totalMonths += 1  
    totalRevenue += float(FirstRow[1]) 
    previousRevenue = float(FirstRow[1])

    for row in csvreader: 
        totalMonths += 1 
        totalRevenue += float(row[1])  
        netChange = float(row[1]) - previousRevenue
        monthlychanges.append(netChange) 
        months.append(row[0])
        previousRevenue = float(row[1]) 

#calculate th e average net change per month 
averagechangePerMonth = sum(monthlychanges)/ len(monthlychanges) 

#greatestIncrease =["", 0] 
#greatestDecrease =["", 0]
for m in range (len(monthlychanges)): 
    if monthlychanges[m]> greatestIncrease[1]:
        greatestIncrease[1] = monthlychanges[m] 
        greatestIncrease[0] = months[m]

    if monthlychanges[m]< greatestDecrease[1]:
        greatestDecrease[1] = monthlychanges[m] 
        greatestDecrease[0] = months[m] 


#netchange = float(row[1]) - previousRevenue

output = f"Total months = {(totalMonths)}" 

output = (
    f"\nFinancial Data Analysis \n"
    f"------------------------ \n"
    f"\tTotal months = {(totalMonths)} \n" 
    f"\tTotal Revenue = ${totalRevenue: .0f} \n"  
    f"\taverage change Per Month = ${averagechangePerMonth: .0f} \n" 
    f"\tgreatestIncrease {greatestIncrease[0]} $({ greatestIncrease[1]: .0f}) \n" 
    f"\tgreatestDecrease {greatestDecrease[0]} $({ greatestDecrease[1]: .0f}) \n" 
    ) 
print(output) 
with open("outputFile", "w") as textFile: 
    textFile.write(output) 



