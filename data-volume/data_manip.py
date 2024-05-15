import csv
import random

def shuffle_and_add_id(input_file, output_file):
    # Read the input CSV file
    with open(input_file, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter='\t')
        data = list(reader)

    # Randomize the order of rows
    random.shuffle(data)

    # Add an extra "id" column
    for i, row in enumerate(data):
        row.insert(0, i + 1)  # Insert the ID column

    # Write the modified data to the output CSV file
    with open(output_file, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter='\t')
        writer.writerows(data)

if __name__ == "__main__":
    input_file = input("Enter the path to the input CSV file: ")
    output_file = input("Enter the path to the output CSV file: ")
    shuffle_and_add_id(input_file, output_file)
    print("CSV file has been processed.")