#This par was just to import moduels
import pandas as pd
import os
import csv
# This part of the code tells python what path im using to get to the csv file
csvpath = "C:/Users/Owner/Desktop/python_challange3/PyBank/Resources/budget_data.csv"
# This opens the csv and tells it what kind of csv, it also tells it the values are seperated by commas
with open(csvpath, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #This skips the header 
    header =next(csv_reader)
    #These are empty lists to store values will later be appended
    months_total = []
    total_profit_loss = []
    
    


    # This is my for functions which tells the program I want to read each row in the csv
    for row in csv_reader:

        date = row[0]
        net_profit_loss = int(row[1])

        total_profit_loss.append(net_profit_loss)
        months_total.append(date)
#this print first three variables
    print("Financial Analysis")
    print(f"Total Months:{len(months_total)}")
    print(f"Total: {sum(total_profit_loss)}")
#this loads in pandas
df = pd.read_csv("C:/Users/Owner/Desktop/python_challange3/PyBank/Resources/budget_data.csv")
#this makes a new df call profit change which is the difference in profit losses column
df_profit_change = df["Profit/Losses"].diff()
# this rounds profit change and gives average
df_average_change = round(df_profit_change.mean())
# these are the dataframes that give me max and min for the whole row in the data fram for profit/losses
df_greatest_increase = df.loc[df["Profit/Losses"].idxmax()]
df_great_decrease = df.loc[df["Profit/Losses"].idxmin()]
# this give me increase/decrease in date 
df_greatest_increase_date = df_greatest_increase["Date"]
df_greatest_decrease_date = df_great_decrease["Date"]
# this makes two new dataframes that store the values of greates increase/decrease
df_greatest_increase_value = df_greatest_increase["Profit/Losses"]
df_greatest_decrease_value = df_great_decrease["Profit/Losses"]

#this prints to module
print(f"Average Change: {df_average_change}")
print(f"Greatest Increase in Profits:{df_greatest_increase_date} : {df_greatest_increase_value}") 
print(f"Greatest Decrease in Profits:{df_greatest_decrease_date} :  {df_greatest_decrease_value}")
#this makes textfile
txtpath = "C:/Users/Owner/Desktop/python_challange3/PyBank/analysis_2/output.txt"
with open (txtpath, "w") as txtfile:

    txtfile.write("Financial Analysis \n")
    txtfile.write(f"Total Months:{len(months_total)}\n")
    txtfile.write(f"Total: {sum(total_profit_loss)}\n")
    txtfile.write(f"Average Change: {df_average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:{df_greatest_increase_date} : {df_greatest_increase_value}\n") 
    txtfile.write(f"Greatest Decrease in Profits:{df_greatest_decrease_date} :  {df_greatest_decrease_value}\n")