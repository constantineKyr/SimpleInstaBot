import csv

def readCsvFile(path):
    accounts = []
    with open(path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            accounts.append(row[1])

    return accounts