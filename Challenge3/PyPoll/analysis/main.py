import csv
from collections import Counter

with open('election_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    data = list(reader)

# Calculate total number of votes
total_votes = len(data)

# List of candidates who received votes
candidates = [row[2] for row in data]

# Calculate votes each candidate won
votes = Counter(candidates)

# Print to terminal
print(f'Election Results\n{"-"*30}\nTotal Votes: {total_votes}\n{"-"*30}')
for candidate, vote in votes.items():
    print(f'{candidate}: {vote/total_votes*100:.3f}% ({vote})')
print(f'{"-"*30}\nWinner: {votes.most_common(1)[0][0]}\n{"-"*30}')

# Write to file
with open('election_results.txt', 'w') as outfile:
    outfile.write(f'Election Results\n{"-"*30}\nTotal Votes: {total_votes}\n{"-"*30}\n')
    for candidate, vote in votes.items():
        outfile.write(f'{candidate}: {vote/total_votes*100:.3f}% ({vote})\n')
    outfile.write(f'{"-"*30}\nWinner: {votes.most_common(1)[0][0]}\n{"-"*30}')