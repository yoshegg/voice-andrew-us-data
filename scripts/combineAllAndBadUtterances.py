#!/usr/bin/env python

__author__      = "Christophe Biwer, cbiwer@coli.uni-saarland.de"

with open("list_of_all_utterances.txt", "r") as alle:
  with open ("list_of_bad_utterances.txt", "r") as bad:
    next_list = False
    first_all_list = set()
    second_all_list = set()
    for x in alle:
      if x == "\n":
        next_list = True
        continue
      x = int(x)
      if not next_list:
        first_all_list.add(x)
      else:
        second_all_list.add(x)

    first_bad_list = set()
    second_bad_list = set()
    next_list = False
    for x in bad:
      if x == "\n":
        next_list = True
        continue
      x = int(x)
      if not next_list:
        first_bad_list.add(x)
      else:
        second_bad_list.add(x)
        
    final_first = first_all_list.difference(first_bad_list)
    final_second = second_all_list.difference(second_bad_list)
    
    with open ("list_of_good_utterances.txt", "w") as good:
    for x in sorted(final_first):
      good.write(x) 
    for x in sorted(final_second):
      good.write(x) 
