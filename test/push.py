import csv

def read_csv_file(file_path):
    data = []

    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if len(row) >= 5 and 'UPI' in row[3]:
                amount = row[4]
                data.append((row[3], amount))

    return data

# Usage example
csv_data = read_csv_file('file.csv')
for transaction, amount in csv_data:
    print("Transaction:", transaction)
    print("Amount:", amount)
    print()