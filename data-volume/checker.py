from openai import OpenAI
import csv
import os
import pprint

input_tsv_path = os.path.join(os.path.dirname(__file__), 'aggregate_data.tsv')
output_tsv_path = os.path.join(os.path.dirname(__file__), 'aggregate_data_checked.tsv')
array_path = os.path.join(os.path.dirname(__file__), "array_data.txt")

client = OpenAI(api_key="")

BASE_PROMPT = 'Does this sentence have gender bias? Answer only "Yes" or "No."\n'

def extract_sentence_strings_from_tsv(input_file):
    sentence_list = []

    # Get the directory path relative to where the script is located
    script_directory = os.path.dirname(__file__)
    
    # Specify the relative path to the TSV file
    relative_tsv_path = os.path.join(script_directory, input_file)
    
    with open(relative_tsv_path, 'r', newline='', encoding='utf-8') as tsvfile:
        reader = csv.DictReader(tsvfile, delimiter='\t')
        
        # Extract strings from the "sentence" column
        for row in reader:
            sentence = row.get('sentence', '').strip()
            if sentence:
                sentence_list.append(sentence)

    return sentence_list

def map_strings_to_dicts(input_array, base_prompt=BASE_PROMPT):
    mapped_dicts = []

    for string in input_array:
        mapped_dict = {
            "role": "user",
            "content": base_prompt + string
        }
        mapped_dicts.append(mapped_dict)

    return mapped_dicts

def parse_result(value):
    if value == "Yes" or value == "Yes.":
        return 1
    elif value == "No" or value == "No.":
        return 0
    else:
        # Handle other cases if needed
        return None  # or any default value

def generate_tsv_from_list_of_dicts(list_of_dicts, output_file):
    # Extract column names from the first dictionary
    column_names = list(list_of_dicts[0].keys())

    with open(output_file, 'w', newline='', encoding='utf-8') as tsvfile:
        # Write column headers
        tsvfile.write('\t'.join(column_names) + '\n')
        
        # Write data rows
        for row in list_of_dicts:
            values = [str(row.get(col, '')) for col in column_names]
            tsvfile.write('\t'.join(values) + '\n')

sentences_list = extract_sentence_strings_from_tsv(input_tsv_path)
message_map = map_strings_to_dicts(sentences_list)
# mini_map = [message_map[2]]

results = []

for msg in message_map:
    # Run the command using subprocess module or any other method
    # For simplicity, we'll just print the command here
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[msg]
    )
    result_str = completion.choices[0].message.content
    results.append(result_str)

# Write the array to a file
with open(array_path, 'w') as file:
    for item in results:
        file.write(f"{item}\n")

final_results = []
for i in range(len(results)):
    try:
        temp_dict = {}
        temp_dict['sentence'] = sentences_list[i]
        temp_dict['new_label'] = parse_result(results[i])
        pprint.pprint(temp_dict)
        final_results.append(temp_dict)
    except Exception as e:
        # Code to handle the exception
     # For example, logging the error, displaying a message, etc.
        print(f"An error occurred: {e}")
    
generate_tsv_from_list_of_dicts(final_results, output_tsv_path)
    