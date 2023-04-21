import pandas as pd
import os
import csv

csvpath = "C:/Users/Owner/Desktop/challange 3/python_challange3/PyBank/Resources/budget_data.csv"

with open(csvpath, encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header =next(csv_reader)
    months_total = []
    total_profit_loss = []
    #df = pd.DataFrame(csv_reader, columns=header)
    



    for row in csv_reader:

        date = row[0]
        net_profit_loss = int(row[1])

        total_profit_loss.append(net_profit_loss)
        months_total.append(date)

    print("Financial Analysis")
    print(f"Total Months:{len(months_total)}")
    print(f"Total: {sum(total_profit_loss)}")

df = pd.read_csv("C:/Users/Owner/Desktop/challange 3/python_challange3/PyBank/Resources/budget_data.csv")

df_profit_change = df["Profit/Losses"].diff()

df_average_change = round(df_profit_change.mean())

df_greatest_increase = df.loc[df["Profit/Losses"].idxmax()]
df_great_decrease = df.loc[df["Profit/Losses"].idxmin()]
df_greatest_increase_date = df_greatest_increase["Date"]
df_greatest_decrease_date = df_great_decrease["Date"]

df_greatest_increase_value = df_greatest_increase["Profit/Losses"]
df_greatest_decrease_value = df_great_decrease["Profit/Losses"]


print(f"Average Change: {df_average_change}")
print(f"Greatest Increase in Profits:{df_greatest_increase_date} : {df_greatest_increase_value}") 
print(f"Greatest Decrease in Profits:{df_greatest_decrease_date} :  {df_greatest_decrease_value}")
