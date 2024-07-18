import json

def load_jsonl(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        return [json.loads(line) for line in file]

def save_jsonl(data, file_path):
    with open(file_path, 'w', encoding="utf8") as file:
        for item in data:
            json.dump(item, file)
            file.write('\n')

def filter_input_data(input_data, output_data):
    output_prompts = set(item['prompt'] for item in output_data)
    return [item for item in input_data if item['prompt'] in output_prompts]

# File paths
input_file = 'input_data.jsonl'
output_file = 'output_data.jsonl'
filtered_input_file = 'filtered_input_data.jsonl'

# Load data
input_data = load_jsonl(input_file)
output_data = load_jsonl(output_file)

# Filter input data
filtered_input_data = filter_input_data(input_data, output_data)

# Save filtered input data
save_jsonl(filtered_input_data, filtered_input_file)

print(f"Filtered input data saved to {filtered_input_file}")
print(f"Original input count: {len(input_data)}")
print(f"Filtered input count: {len(filtered_input_data)}")