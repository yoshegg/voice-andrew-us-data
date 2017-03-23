import re
import os

def get_dict(prompt_filename):
    # Dictionary of ID# : Prompt Text
    with open(prompt_filename) as f: #From export labels in Audacity
        data = f.readlines()
    prompts = [entry[1:-1] for entry in data if entry[0] == "#"]
    # Change the 3 to 1 in the slice if you want the full ID, with letters (eg. sx13)
    # If you do this, the id_list would have to reflect this formatting
    ##ids = [int(entry[3:-1]) for entry in data if entry[0] == "-"]
    ids = [entry[1:-1] for entry in data if entry[0] == "-"]
    id2prompt = dict(zip(ids,prompts))
    id2prompt[0] = "" # If we mark throw-away segments with ID# 0
    return id2prompt

def make_text_files(prompt_file):
    id2prompt = get_dict(prompt_file)
    titles = [file[:-4] for file in os.listdir() if file[-4:] == ".wav"]
    counter = 0
    for tag in titles:
        #tag = re.findall(r'\d+', title) # Ignore ! and letters
        #if len(tag) > 0:
        #    tag = tag[0]
        try:
            prompt = id2prompt[tag]
            with open(tag+".txt", "w") as f:
                f.write(prompt)
            counter += 1
        except:
            print("Skipped", tag, "not found in dictionary")
    print("Saved", counter, "text files.")
    
prompt_file = "PROMPTS.txt"
make_text_files(prompt_file)
