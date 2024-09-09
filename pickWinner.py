import re
import random
from collections import defaultdict

def read_comments_from_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def extract_valid_entries(comments):
    pattern = r"(\w+(?:[-.']\w+)*)'s profile picture\n@([\w.-]+)"
    matches = re.findall(pattern, comments, re.MULTILINE)
    
    entries = defaultdict(list)
    for commenter, mentioned in matches:
        entries[commenter].append(mentioned)
    
    return entries

def pick_winners(entries, num_winners=3):
    # Create a list of commenters, with each commenter appearing as many times as they have entries
    weighted_commenters = [commenter for commenter, mentions in entries.items() for _ in mentions]
    
    if len(weighted_commenters) < num_winners:
        return f"Not enough valid entries. Only {len(weighted_commenters)} available."
    
    return random.sample(weighted_commenters, num_winners)

# Get file path
file_path = "winner.txt"  # Assumes the file is in the same directory as the script

# Read comments from the file
try:
    comments = read_comments_from_file(file_path)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit(1)
except IOError:
    print(f"Error: There was an issue reading the file '{file_path}'.")
    exit(1)

valid_entries = extract_valid_entries(comments)
winners = pick_winners(valid_entries, 3)

total_entries = sum(len(mentions) for mentions in valid_entries.values())
print(f"Total valid entries: {total_entries}")
print(f"Unique commenters: {len(valid_entries)}")

if isinstance(winners, list):
    print("The winners are:")
    for i, winner in enumerate(winners, 1):
        print(f"{i}. {winner}")
else: # winners is a string
    print(winners)

print("\nEntry counts:")
sorted_entries = sorted(valid_entries.items(), key=lambda x: len(x[1]), reverse=True)
for commenter, mentions in sorted_entries:
    print(f"{commenter}: {len(mentions)} entries")
    for mention in mentions:
        print(f"  - @{mention}")