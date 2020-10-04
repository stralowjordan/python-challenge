import pandas as pd
from datetime import datetime
from dateutil import relativedelta
import numpy as np

#Calculate Total Number of Months

budgetdata = pd.read_csv("/Users/Jorda/Desktop/Python Homework/PyBank/Resources/budgetdata.csv")

Dates = budgetdata["Date"]

startdate = datetime.strptime(Dates[0],"%b-%y")
enddate = datetime.strptime(Dates[85], "%b-%y")

totalmonths = relativedelta.relativedelta(enddate,startdate)

#numbertotalmonths = totalmonths.years * 12 + totalmonths.months

numbertotalmonths = len(budgetdata)
print(numbertotalmonths)

#Calculate Total Profit/Losses

profit_losses = budgetdata["Profit/Losses"]
Total_profit = np.sum(profit_losses)

#Calculate Average Change in Profit/Losses

monthlychange = [profit_losses[i+1] - profit_losses[i] for i in range(85)]
totalmonthlychange = np.sum(monthlychange)/85

#Calculate Greatest Profit/Losses Change

monthlychangedates = [[Dates[i+1], profit_losses[i+1] - profit_losses[i]] for i in range(85)] 

greatestdecrease = min(monthlychangedates, key=lambda x: x[1])

greatestincrease = max(monthlychangedates, key=lambda x: x[1])

financial_analysis =[
    ["Financial Analysis"],
    ["------------------"],
    ["Total Months: " + str(numbertotalmonths)],
    ["Total:" + str(Total_profit)],
    ["Average Change: " + str(totalmonthlychange)],
    ["Greatest Increase: " + str(greatestincrease)[2:8] + " ($" + str(greatestincrease[1])+")"],
    ["Greatest Decrease: " + str(greatestdecrease)[2:8] + " ($" + str(greatestdecrease[1])+")"]
]

with open("C:/Users/Jorda/Desktop/Python Homework/PyBank/Analysis/analysis.txt", "w") as output:
    output.write(str(financial_analysis)+ "\n")

    