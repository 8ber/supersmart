import sys

args           = sys.argv
fullname       = args[len(args)-1]
temp           = fullname.split(".")
missing_suffix = ".".join(temp[:-1])

with open(fullname, "w") as file:
  file.write(missing_suffix)

