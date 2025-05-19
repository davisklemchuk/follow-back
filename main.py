import json

def extract_values(filename, key):
    # Extracts "value" fields
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            values = set()

            # Check to see if file is a dict
            if isinstance(data, dict):
                data = data.get(key, [])

            # Adds the 'value' field to the set
            for item in data:
                if 'string_list_data' in item and isinstance(item['string_list_data'], list):
                    for entry in item['string_list_data']:
                        if 'value' in entry:
                            values.add(entry['value'])

            return values
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading {filename}: {e}")
        return set()

followers_set = extract_values('followers.json', None) # followers.json is just a list
following_set = extract_values('following.json', "relationships_following")  # following.json has a dict

# Create the list of usernames of people that don't follow you back
non_followers = sorted(following_set - followers_set)

# Print results
print("List of users who don't follow you back:")
print("\n".join(non_followers))
