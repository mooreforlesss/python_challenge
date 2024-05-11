import csv

month_count = 0
total_profit = 0

last_month_profit = 0
changes = []
month_changes = []

#set path for file
csvpath = "Resources/budget_data.csv"

#open CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

#Not finished 
    for row in csvreader:
        print(row)

        #count months
        month_count = month_count + 1 

        #add profit
        total_profit = total_profit + int(row[1])

        #need last month profit
        #subtrat this month profit - last month profit
        #append that change to the list

        #IF first row, there is no change
        if (month_count == 1):
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            changes.append(change)
            month_changes.append(row[0])

    print(month_count)
    print(total_profit)

    avg_change = sum(changes) / len(changes)
    print(avg_change)
    
    max_change = max(changes)
    max_month_index = changes.index(max_change)
    max_month = month_changes[max_month_index]

    print(max_change)
    print(max_month)

    # min_change = min(change)
    # min_month_index = changes.index(min_change)
    # min_month = month_changes[min_month_index]

    # print(min_change)
    # print(min_month)
