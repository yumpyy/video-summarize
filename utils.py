import re

pattern_list = [
    "[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3} --> [0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{3}",  # for matching 00:00:00,000 --> 00:00:39,410
    "[0-9]{1,10}",                                                                  # for matching lines starting with numbers
]

def filter(data):
    data = re.sub("|".join(pattern_list), "", data)

    filtered_data = []
    for line in data.split('\n'):
        if line.strip():
            filtered_data.append(line)
    
    filtered_data = " ".join(filtered_data)
    return filtered_data

