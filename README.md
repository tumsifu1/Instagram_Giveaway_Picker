# Instagram_Giveaway_Picker
Instagram Giveaway Picker
This Python script automates the process of selecting winners for an Instagram giveaway based on comments and mentions.
Description
The Instagram Giveaway Picker script processes a text file containing Instagram comments, extracts valid entries based on a specific pattern, and randomly selects winners from the commenters. It's designed to handle scenarios where commenters mention other users, and each mention counts as an entry for the commenter.
Features

Reads comments from a text file
Extracts valid entries based on the pattern "X's profile picture" followed by "@username" mentions
Allows multiple entries per commenter
Randomly selects winners, with chances proportional to the number of entries
Provides detailed output of entry counts and winner selection

Setup

Ensure you have Python 3.x installed on your system.
Clone this repository or download the pickWinner.py script.
Place your Instagram comments in a file named winner.txt in the same directory as the script.

Usage

Open a terminal or command prompt.
Navigate to the directory containing the script and winner.txt file.
Run the script using Python:
Copypython pickWinner.py

The script will process the comments and display the results, including the winners and entry counts.

Input File Format
The winner.txt file should contain Instagram comments in the following format:
Copyusername's profile picture
@mentioned_user
Reply
another_username's profile picture
@another_mentioned_user
Reply
Functions

read_comments_from_file(filepath): Reads the contents of the specified file.
extract_valid_entries(comments): Parses the comments and extracts valid entries.
pick_winners(entries, num_winners=3): Randomly selects winners from the valid entries.

Output
The script provides the following output:

Total number of valid entries
Number of unique commenters
List of winners
Detailed entry counts for each commenter, sorted by number of entries

Notes

The script assumes that each "X's profile picture" line is followed by one or more lines with "@username" mentions.
Comments that don't follow this pattern will be ignored.
The number of winners can be adjusted by modifying the num_winners parameter in the pick_winners() function call.

License
This project is open source and available under the MIT License.
Contributing
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.
Author
Aaron Moise
Acknowledgments

Thanks to Anthropic's Claude AI for assistance in documenting this script