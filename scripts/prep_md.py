#!/usr/bin/env python3

"""
Gets TIMIT prompts, processes them, saves to markdown style
for later conversion into pdf or revealjs
"""

from urllib.request import urlopen

webpage = "https://catalog.ldc.upenn.edu/docs/LDC93S1/PROMPTS.TXT"
output_filename = "prompts.md" # Call it whatever you want

html = urllib.request.urlopen(webpage).read()
all_text = BeautifulSoup(html, "lxml").get_text()
all_text = all_text.split("\n")

# Remove irrelevant lines at beginning and end, remove final paranthesis
relevant_text = [line[:-1] for line in all_text if len(line) > 0 and line[-1] == ")"]
# Split off codes from prompts
relevant_text = [line.split(" (") for line in relevant_text]

# Save as text file
output = ""
for prompt, code in relevant_text:
    line = "# " + prompt + "\n-" + code + "\n\n" # Adjust formatting as needed here
    output += line
with open(output_filename, "w") as f:
    f.write(output)
    
"""
To-do:
   Add audio
   Maybe improve formatting
Next steps: 
   pandoc -t revealjs -s -o presentation.html prompts.md
"""
