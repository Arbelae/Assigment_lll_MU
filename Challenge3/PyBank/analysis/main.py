import csv

with open('budget_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    data = list(reader)
   
# Calculate total number of months
total_months = len(data)

# Calculate net total amount of "Profit/Losses"
net_total = sum(int(row[1]) for row in data)

# Calculate changes in "Profit/Losses" over the entire period
changes = [int(data[i][1]) - int(data[i-1][1]) for i in range(1, total_months)]

# Calculate average of those changes
average_change = sum(changes) / len(changes)

# Calculate greatest increase in profits (date and amount)
greatest_increase = max(changes)
greatest_increase_date = data[changes.index(greatest_increase)+1][0]

# Calculate greatest decrease in profits (date and amount)
greatest_decrease = min(changes)
greatest_decrease_date = data[changes.index(greatest_decrease)+1][0]

# Print to terminal
print(f'Financial Analysis\n{"-"*30}\nTotal Months: {total_months}\nTotal: ${net_total}\nAverage Change: ${average_change:.2f}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

# Write to file
with open('financial_analysis.txt', 'w') as outfile:
    outfile.write(f'Financial Analysis\n{"-"*30}\nTotal Months: {total_months}\nTotal: ${net_total}\nAverage Change: ${average_change:.2f}\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')