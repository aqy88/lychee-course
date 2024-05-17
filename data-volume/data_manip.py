import csv
import random
import pandas as pd
import sys
from datasets import Dataset

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

def process_and_append_tsv(input_file, base_file, output_file, start_id=554):
    # Read the input TSV file with UTF-8 encoding, ignoring unrecognized characters
    with open(input_file, 'r', encoding='utf-8', errors='ignore') as file:
        reader = csv.reader(file, delimiter='\t')
        data = list(reader)

    # Remove the top row
    data = data[1:]

    # Add an extra "id" column with monotonically increasing numbers starting from `start_id`
    for i, row in enumerate(data):
        row.insert(0, start_id + i)

    # Read the base TSV file with UTF-8 encoding, ignoring unrecognized characters
    with open(base_file, 'r', encoding='utf-8', errors='ignore') as file:
        base_data = file.readlines()

    # Write the combined data to the output TSV file with UTF-8 encoding
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')

        # Write the base data
        file.writelines(base_data)

        # Add a new row to separate base data from new data
        writer.writerow([])

        # Write the modified input data
        writer.writerows(data)

def create_huggingface_dataset(tsv_file, output_dir):
    # Read the TSV file into a pandas DataFrame
    df = pd.read_csv(tsv_file, delimiter='\t', encoding='utf-8', encoding_errors='ignore')

    # Convert the pandas DataFrame to a Hugging Face Dataset
    dataset = Dataset.from_pandas(df)

    # Save the dataset to the specified output directory
    dataset.save_to_disk(output_dir)

if __name__ == "__main__":
    # input_file = input("Enter the path to the input TSV file: ")
    # base_file = input("Enter the path to the base TSV file: ")
    # output_file = input("Enter the path to the output TSV file: ")
    # output_dir = input("Enter the path to the data output directory: ")
    
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    create_huggingface_dataset(input_file, output_dir)
    # shuffle_and_add_id(input_file, output_file)
    # process_and_append_tsv(input_file, base_file, output_file)
    
    print("Script complete.")