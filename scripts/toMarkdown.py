__author__ = 'Christophe Biwer, cbiwer@coli.uni-saarland.de"

import re

with open("PROMPTS.TXT", "r") as source:
    for line in source:
        if line[0] == ";":
            continue
        temp = re.search("\(.*?\)$", line)
        name = temp.group(0)[1:-1]
        print(name)
        to_replace = " (" + name + ")"
        sentence = line.replace(to_replace, "")[:-1]
        print(sentence)
