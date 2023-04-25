import pandas as pd
import os
import csv

csvpath = "C:/Users/Owner/Desktop/python_challange3/PyPoll/Resources/election_data.csv"
Poll_data = []
Total_of_votes = 0
results = {}
with open (csvpath,encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    header =next(csv_reader)
    
    for row in csv_reader:
        #Poll_data.append(row)
        Total_of_votes =+ 1
    
    
    #for row in Poll_data:
        Candidate_name = row[2]

        if Candidate_name not in Poll_data:
            Poll_data.append(Candidate_name)
            results[Candidate_name] = 0
        
        
        results[Candidate_name] += 1
        




df = pd.read_csv("C:/Users/Owner/Desktop/python_challange3/PyPoll/Resources/election_data.csv")
df_Total_votes = len(df["Ballot ID"])



def Winner(name):
  return max(name, key = name.get)



vote_count_list = list(results.values())
winner = Winner(results)


print("Election Results")
print("---------------------")
print(f"Total Votes: {df_Total_votes}")
print("-----------------------")
for Candidate_name in results:
    vote_count = results.get(Candidate_name)
    vote_percentage = round(vote_count / len(df["Ballot ID"])*100)
    print(f"{Candidate_name}    {vote_percentage}%   ({vote_count})  ")
print(f"Winner: {winner}")

txtpath = "C:/Users/Owner/Desktop/python_challange3/PyPoll/analysis/output.txt"
with open (txtpath, "w") as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("---------------------\n")
    txtfile.write(f"Total Votes: {df_Total_votes}\n")
    txtfile.write("-----------------------\n")
    for Candidate_name in results:
        vote_count = results.get(Candidate_name)
        vote_percentage = round(vote_count / len(df["Ballot ID"])*100)
        txtfile.write(f"{Candidate_name}    {vote_percentage}%   ({vote_count}) \n ")
    txtfile.write(f"Winner: {winner}\n")