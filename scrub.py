import json
import re
import os
from json.decoder import JSONDecodeError


class Scrubber:
    def scrub(self):
        # open dirty file
        with open(self.data) as f:
            # try to parse
            try:
                result = json.load(f)
            except JSONDecodeError as e: # error happened
                # open the file up again
                with open(self.data) as f:
                    lines = f.readlines() # read each line

                    if re.search("\s}", lines[e.lineno].rstrip()):
                        lines[e.lineno - 2] = lines[e.lineno - 2].rstrip()[:-1] + "\n"
  
                    del lines[e.lineno - 1] # delete the line with the problem
                
                clean_file = open("clean.json", "w+") # open a new json

                for line in lines: # write the file into a clean json
                    clean_file.write(line)

    # default ocnstructor            
    def __init__(self, file_path):
        self.data = file_path
        #self.scrub()
        self.scrub()
if __name__ == "__main__":
    # create object
    data = Scrubber("test_data.json")

