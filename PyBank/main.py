import csv
from statistics import mean

file_name = 'budget_data.csv'

with open(file_name, newline = '') as csvfile:
    bankreader = csv.reader(csvfile)
    profit_loss = [int(item) for item in [row[1] for row in bankreader][1:]]

max_increase = max(profit_loss)
max_decrease = min(profit_loss)

with open(file_name, newline = '') as csvfile:
    bankreader = csv.reader(csvfile)
    months = [row[0] for row in bankreader][1:]

out_string = f"""Financial Analysis
----------------------------
Total Months: {len(months)}
Total: ${sum(profit_loss)}
Average Change: ${round(mean(profit_loss),2)}
Greatest Increase in Profits: {months[profit_loss.index(max_increase)]} ${max_increase}
Greatest Decrease in Profits: {months[profit_loss.index(max_decrease)]} ${max_decrease}"""

print(out_string)

out_file = 'out.txt'

with open(out_file, 'w+') as out:
    out.write(out_string)