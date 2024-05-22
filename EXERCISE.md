# Leveraging ChatGPT to Modify Data

ChatGPT can provide a quick and easy way to generate scripts to manipulate data in your datasets. This exercise is a supplement for the course materials available [here](https://github.com/aqy88/lychee-course/tree/main).

By the end of this exercise, you will have successfully prompted ChatGPT to provide a Python script that will restructure `sexism_data_orig.csv` so that it can be used with `distilled-llm_exericse.ipynb`.

**NOTE**: Since ChatGPT-4 requests are limited, and you may run out in the course of this exercise, stick to 3.5 for consistent results.

## Exercise

### Step 1. Compare working dataset and desired dataset, then determine what changes we need to make.

The code in `distilled-llm_exercise.ipynb` that imports our dataset looks like this:
```
# Import Hugging Face datasets lib
from datasets import load_from_disk, DatasetDict

dataset = load_from_disk("./dataset_revised")
```

It imports from a directory that contains data files compatible with the Hugging Face `datasets` Python library, which is built off of `aggregate_data_revised.tsv`. That file has data that looks like this:

![aggregate_data_revised.tsv sample](https://imgur.com/MyBQ3w8.png)
We can see that it has 3 columns: `id`, `sentence`, and `label`. We know that `label` is `0` if gender bias **is not** detected, and `1` if gender bias **is** detected. 

We can compare this to  `sexism_data_orig.csv`: 

![sexism_data_orig.csv sample](https://imgur.com/TVDR2mL.png)
We know right off the bat that we don't care for the `dataset` , `toxicity` , and `of_id` columns. We also notice that `sexist` appears to use labels `TRUE` and `FALSE` instead of `1` and `0`, and that the column names are different. We could convert this data into a Hugging Face dataset, but that would require us to modify code in Jupyter Notebook. To avoid this, we can use ChatGPT to create a script to create a Hugging Face dataset that's already compatible with our notebook code.

### Step 2. Design a prompt and procure a script.

We need to ask our script accept a `.csv` file as input, to drop (remove) the columns we don't care about, rename the columns to match the dataset we were already using, and map the `sexist` column's values to `0` and `1` from `FALSE` and `TRUE` respectively.

Start with "Give me a Python script that..." and ask it to do the above operations.

**NOTE**: For reasons beyond the scope of this exercise, add this sentence to the end of the prompt: "Do NOT use the pandas library."

### Step 3. Test the script, then modify the prompt.
To test our script with minimal setup, we will use the Jupyter Lab instance you've already deployed at http://127.0.0.1:8888.

1. Click the `+` sign.
![step_1](https://imgur.com/YVHcfGH.png)
2. Create a new Jupypter notebook.
![step_2](https://imgur.com/pxWixAa.png)
3. Paste in the generated script.
![step_3](https://imgur.com/W8qW6zp.png)
4. Check the script.
It's more than likely that the generated script will include a block of code resembling these:
```
if  __name__  ==  "__main__":
    input_file  =  'input.csv'  # Replace with your input file path
    output_file  =  'output.csv'  # Replace with your desired output file path
    process_csv(input_file, output_file)
```
You will need to replace `input_file` with `sexism_data_orig.csv`. The name of the output file does not matter, but it is recommended to pick something that is clearly named and does **not** share a name with any file that already exists in the `data-volume/` folder (e.g. do NOT set the `output_file` to also be `sexism_data_orig.csv`, as it will overwrite the original file).

5. Run the script.
![step_5](https://imgur.com/ACtogbE.png)6. Examine the output data.
![step_6](https://imgur.com/b9U1e2k.png)This data was generated from a script matching this prompt:
```
Give me a Python script that accepts a `.csv` file as input, to drop (remove) columns "dataset", "of_id", and "toxicity", rename the `text` column to `sentence` and `sexist` to `label`, then map the `label` column's values to `0` and `1` from `FALSE` and `TRUE` respectively. Do NOT use the pandas library.
```
It appears to have dropped the `id` column, which we want to keep if our objective is to match the data schema in `aggregate_data_revised.tsv`.

We can tell ChatGPT: 
```
This script drops the "id" column, which I did not ask you to do.
```
It should respond with a revised script. You can continue to prompt ChatGPT and repeat steps 3-6 until the output data matches the desired structure.


### Step 4. Complete the script.
Earlier on, it was mentioned that  `distilled-llm_exercise.ipynb` imports a dataset from a directory that contains data files compatible with the Hugging Face `datasets` Python library. Now that we have tested and verified that our script cleans up the input dataset in the way that we want, we can tell ChatGPT to output the cleaned dataset into a directory compatible with Hugging Face `datasets`. 

`distilled-llm_exercise.ipynb` also uses `load_from_disk()` to import the data, which means, according to the Hugging Face documentation, we must create the saved data with `save_to_disk()`. Incorporating the feedback from the above investigation and the need to save data with `save_to_disk()`, rewrite a single prompt that meets all of our needs, then run the provided script. Take note of the `output_dir` field.

### Step 5. Plug and play!
If your script is working correctly, you should see something like this at the bottom of your notebook running the script:
![save_to_disk example](https://imgur.com/5R0ZMjw.png)
We can then open `distilled-llm_exercise.ipynb` and swap in our value for the `output_dir` and re-run the exercise:

![swap_data_in](https://imgur.com/8BGvLcF.png)
Congratulations! You've now successfully used ChatGPT to save yourself the effort of writing a Python script that manipulates a dataset.

## Answer Key

### Example Working Prompt

```
Give me a Python script that accepts a `.csv` file as input, to drop (remove) columns "dataset", "of_id", and "toxicity", rename the `text` column to `sentence` and `sexist` to `label`, keep the `id` column, then map the `label` column's values to `0` and `1` from `FALSE` and `TRUE` respectively. Then, output the data into a Hugging Face dataset directory using `save_to_disk`. Do NOT use the pandas library.
```

### Example Working Script
```
import csv
import os
import json
from datasets import Dataset

def process_csv(input_file):
    # Initialize an empty list to store rows
    rows = []

    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)

        # Process each row in the input file
        for row in reader:
            # Create a new row dictionary, keeping only necessary columns and renaming them
            new_row = {
                'sentence': row['text'],
                'label': '1' if row['sexist'] == 'TRUE' else '0',
                'id': row['id']
            }
            rows.append(new_row)

    # Create a Hugging Face dataset
    dataset = Dataset.from_dict({'data': rows})

    return dataset

def main(input_file, output_dir):
    # Process the CSV file
    dataset = process_csv(input_file)

    # Save the dataset to disk
    dataset.save_to_disk(output_dir)

# Example usage
input_file = 'sexism_data_orig.csv'
output_dir = 'exercise_output_dataset'
main(input_file, output_dir)
```
