#import data
import csv
import os

#read in csv path
csvpath = "Resources/election_data.csv"
vote_count = 0
candidate_dict = {}

#oen the csv, got os from Kourt
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    #Find total number of votes
    #How many votes does each candidate have
    for row in csvreader:
        vote_count += 1

        row_candidate = row[2]
        if row_candidate in candidate_dict.keys():
            candidate_dict[row_candidate] += 1
        else:
            candidate_dict[row_candidate] = 1


print(vote_count)
print(candidate_dict)


#create output, got from Prof
output = f"""Election Results
---------------------
Total Votes = {vote_count}
---------------------\n"""

max_cand = ""
max_votes = 0
for candidate in candidate_dict.keys():
    votes = candidate_dict[candidate]
    perc = 100 * (votes / vote_count)

    line = f"{candidate} {round(perc, 3)}% ({votes})\n"
    output += line

    if votes > max_votes:
        max_cand = candidate
        max_votes = votes

last_line = f"""----------------
winner: {max_cand}
--------------------"""
output += last_line
print(output)

with(open("output_PyPoll.txt", "w") as f):
    f.write(output)