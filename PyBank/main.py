import csv
from statistics import mean

file_name = 'budget_data.csv'

with open(file_name, newline = '') as csvfile:
    bankreader = csv.reader(csvfile)
    profit_loss = [int(item) for item in [row[1] for row in bankreader][1:]]

# Calculate changes by taking the profits and losses and subtracting the previous month
changes = [month2-month1 for month1, month2 in zip(profit_loss[:-1],profit_loss[1:])]

max_increase = max(changes)
max_decrease = min(changes)

with open(file_name, newline = '') as csvfile:
    bankreader = csv.reader(csvfile)
    months = [row[0] for row in bankreader][1:]

out_string = f"""Financial Analysis
----------------------------
Total Months: {len(months)}
Total: ${sum(profit_loss)}
Average Change: ${round(mean(changes),2)}
Greatest Increase in Profits: {months[changes.index(max_increase)+1]} ${max_increase}
Greatest Decrease in Profits: {months[changes.index(max_decrease)+1]} ${max_decrease}"""

print(out_string)

out_file = 'out.txt'

with open(out_file, 'w+') as out:
    out.write(out_string)