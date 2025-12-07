import json
import os

# Define paths
directory = r"c:\Users\akhil\OneDrive\Desktop\PAN\PANW-Case-Study\training\data"
input_path = os.path.join(directory, "train_updated.jsonl")
output_path = os.path.join(directory, "train_updated.jsonl") # Overwriting as requested "replace" implies modifying, but let's be safe and write to a temp file then rename or just read all lines then write.

print(f"Processing {input_path}...")

# Read all lines
with open(input_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

processed_lines = []
count = 0

for line in lines:
    if line.strip():
        data = json.loads(line)
        if data.get('label') == 'anxious':
            data['label'] = 'negative_low_energy'
            count += 1
        processed_lines.append(json.dumps(data))

# Write back to file
with open(input_path, 'w', encoding='utf-8') as f:
    for line in processed_lines:
        f.write(line + '\n')

print(f"Successfully replaced {count} 'anxious' labels with 'negative_low_energy' in {input_path}")
