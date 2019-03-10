import csv

file_name = 'election_data.csv'

with open(file_name, newline = '') as csvfile:
    votereader = csv.reader(csvfile)
    headers = next(votereader)
    voted_for = [row[2] for row in votereader]

candidates = set(voted_for)
total_votes = len(voted_for)

out_string = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------"""
vote_counts = []
for cand in candidates:
   vote_counts.append([cand, voted_for.count(cand)])

vote_counts.sort(reverse = True, key = lambda x: x[1])

winner = vote_counts[0][0]

for votes in vote_counts:
    out_string += "\n{}: {:.3f}% ({})".format(votes[0],round(votes[1] / total_votes, 5)*100,votes[1])

out_string += f"""\n-------------------------
Winner: {winner}
-------------------------"""

print(out_string)

out_file = 'out.txt'

with open(out_file, 'w+') as out:
    out.write(out_string)