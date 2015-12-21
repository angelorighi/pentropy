import os.path
import sys
import pefile

file_path = sys.argv[1]   

try:
  if os.path.isfile(file_path):
    pe = pefile.PE(file_path,True)

    for section in pe.sections:
      print section.Name, section.get_entropy()

  else:
    print "File '%s' not found!" % file_path     
except pefile.PEFormatError:
  print "Not a PE file!"

