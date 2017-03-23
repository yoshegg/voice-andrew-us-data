with open("../prompts/ourCorpus.txt", "r") as c:
  corpus = dict()
  for line in c:
    splitted = line.split(" (")
    corpus[splitted[1][2:-2]] = splitted[0]

with open("../numericalListsOfUtterances/list_of_all_good_utterances.txt", "r") as t:
  speech_replacer = list()  
  for line in t:
    speech_replacer.append(line[:-1])

with open ("../textgrids/complete.TextGrid", "r") as t:
  with open("../textgrids/finalAnnotated.TextGrid", "w") as f:
    for line in t:
      if "Speech" in line:
        index = speech_replacer.pop(0)
        string = "\"" + corpus[index] + " (" + index + ")" + "\"\n"
        f.write(string)
      else:
        f.write(line)
