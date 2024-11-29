###
# Makes a copy of a text file
#

# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle.txt'

# read the content of the original file
with open(original_file, "r") as origin:
   with open(target_file, "w") as target:
      for line in origin:
         target.write(line)