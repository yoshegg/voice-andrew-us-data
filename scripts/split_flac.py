import sys
import yaml
import os


ymlGrid_file   = sys.argv[1]
flac_file = sys.argv[2]

with open(ymlGrid_file, 'r') as ymlGrid:
    try:
        library = (yaml.load(ymlGrid))
    except yaml.YAMLError as exc:
        print(exc)

os.system("rm -rf target/")
os.system("mkdir target/")

for x in library.items():
  target = "target/"
  filename = x[0] + ".wav"
  sta = str(x[1]["sta"])
  end = " =" + str(x[1]["end"])
  command = "sox " +  flac_file + " " +  target + filename + " trim " + sta + end + " rate 16000"
  print("execute: " + command)
  os.system(command)
  print(" > saved " + filename + "\n")


