import json

# Open the input and output files
with open('sensors.json', 'r') as f_in, open('data.json', 'w') as f_out:
    for line in f_in:
        # Load the JSON object from the current line
        data = json.loads(line)
        # Check if the "state" key is in the current object
        if "state" in data:
            # Write the current object to the output file
            json.dump(data, f_out)
            f_out.write('\n')  # add a newline after each object
