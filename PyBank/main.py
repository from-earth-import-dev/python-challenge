import os
import csv
from statistics import mean 

budget_csv = os.path.join(".", "budget_data.csv")

# Convert number to currency format
def currency(amount):
    return '${:,.2f}'.format(amount)

# Find total months, total profit, and monthly profit differential
months = 0
monthly_total_profit = []
monthly_diff = []
max_profit = 0

with open(budget_csv) as budget_csv:
    csv_reader = csv.reader(budget_csv, delimiter=",")
    next(csv_reader)
    for row in csv_reader:
        if row[0]:
            months += 1
        monthly_total_profit.append((row[0], int(row[1])))
total_sum = currency(sum([month[1] for month in monthly_total_profit]))

for index in range(len(monthly_total_profit) - 1):
    if monthly_total_profit[index + 1]:
        monthly_diff.append((monthly_total_profit[index + 1][0], (monthly_total_profit[index+1][1] - monthly_total_profit[index][1])))

# Find the best & worst months for gains & losses
best_month = []
worst_month = []
best_gain = 0
worst_gain = 0

for month in monthly_diff:
    if month[1] > best_gain:
        best_gain = month[1]
        best_month = [month[0], month[1]]
    elif month[1] < worst_gain:
        worst_gain = month[1]
        worst_month = [month[0], month[1]]

average_monthly_diff = currency(mean([month[1] for month in monthly_diff]))

# Display results of analysis
print('\nFinancial Analysis')
print('-' * len('Financial Analysis'))
print(f'Total Months: {months}')
print(f'Total: {total_sum}')
print(f'Average Change: {average_monthly_diff}')
print(f'Greatest Increase in Profits: {best_month[0]} ({currency(best_month[1])})')
print(f'Greatest Decrease in Profits: {worst_month[0]} ({currency(worst_month[1])})\n')

# Output results to a .txt file
output = os.path.join(".", "pybank_analyis_output.txt")
with open(output, "w") as file:
    file.write('\nFinancial Analysis\n')
    file.write('-' * len('Financial Analysis'))
    file.write(f'\nTotal Months: {months}')
    file.write(f'\nTotal: {total_sum}')
    file.write(f'\nAverage Change: {average_monthly_diff}')
    file.write(f'\nGreatest Increase in Profits: {best_month[0]} ({currency(best_month[1])})')
    file.write(f'\nGreatest Decrease in Profits: {worst_month[0]} ({currency(worst_month[1])})\n')
