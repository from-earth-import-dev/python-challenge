import os
import csv

election_csv = os.path.join(".","election_data.csv")

# Iterate through rows, add candidates as key if not in candidates_dict, tally votes
total_votes = 0
candidates_dict = {}

with open(election_csv) as election_csv:
    csv_reader = csv.reader(election_csv, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        if row[2] in candidates_dict:
            candidates_dict[row[2]] += 1
        else:
            candidates_dict[row[2]] = 1
        total_votes += 1

# Display election results
print(f'\nElection Results')
print('-' * len('Election Results'))
print(f'Total Votes: {total_votes}')
print('-' * len('Election Results'))
# Tally votes per candidate, divide by total votes for each candidate and print their vote % along with individual votes
candidate_tallies = [f'{candidate}: {str(round((votes / total_votes) * 100, 2))}% ({votes})' for candidate, votes in candidates_dict.items()]
for candidate in candidate_tallies:
    print(candidate)
# Declare the winner by popular vote
winner = max(candidates_dict, key=candidates_dict.get)
print('-' * len('Election Results'))
print(f'Winner: {winner}')
print('-' * len('Election Results'))
print()

# Write results to text file
output = os.path.join(".", "pypoll_analysis_output.txt")
with open(output, "w") as output:
    output.write('\nElection Results\n')
    output.write('-' * len('Election Results'))
    output.write(f'\nTotal Votes: {total_votes}\n')
    output.write('-' * len('Election Results'))
    output.write('\n')
    for candidate in candidate_tallies:
        output.write(f'{candidate}\n')
    output.write('-' * len('Election Results'))
    output.write(f'\nWinner: {winner}\n')
    output.write('-' * len('Election Results'))
    output.write('\n')

