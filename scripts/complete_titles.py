import sys

textGrid_file = sys.argv[1]

with open("newTG.textGrid", "w") as ntg:
  with open(textGrid_file, "r") as tG:
    for x in tG:
      if "(" and ")" in x and "!)" not in x:
        splitted = x.split(" (")
        end = splitted[1][:-3]

        try:
          if int(end) < 3:
            new_number = "sa" + end
          elif int(end) < 450:
            new_number = "sx" + end
          else:
            new_number = "si" + end
        except ValueError:
          pass
      else:
        ntg.write(x)
        continue
      ntg.write(splitted[0] + " (" + new_number + ")\"\n")
