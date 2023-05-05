import json

# Open the input and output files
with open('filtered.json', 'r') as f_in, open('needed.json', 'w') as f_out:
    for line in f_in:
        # Load the JSON object from the current line
        data = json.loads(line)
        # Check if the "state" key is in the current object
        new_data = {"state": data["state"], "timestamp": data["timestamp"]}
        json.dump(new_data, f_out)
        f_out.write('\n') 
