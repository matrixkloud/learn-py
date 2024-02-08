import json

def clean_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Recursively clean all nested keys
    cleaned_data = clean_data_recursive(data)

    # Write cleaned JSON to output file
    with open(output_file, 'w') as f:
        json.dump(cleaned_data, f, indent=4)

def clean_data_recursive(data):
    cleaned_data = {}
    for key, value in data.items():
        if isinstance(value, list):
            cleaned_data[key] = value[:2]  # Keep only the first three values for lists
        elif isinstance(value, dict):
            cleaned_data[key] = clean_data_recursive(value)  # Recursively clean nested dictionaries
        else:
            cleaned_data[key] = value
    return cleaned_data

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python3 clean.py input.json output.json")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_json(input_file, output_file)
    print("Cleanup completed. Cleaned JSON saved to", output_file)
