import os
import json

folder=r'files'

# This lists all the files, so far you were correct
for each_file in os.listdir(folder):
    print(each_file)

#
all_dicts = []

# Next -- you had the right idea using os.path.join
for each_file in os.listdir(folder):
    print(each_file)
    filepath = os.path.join(folder,each_file)

    # This is basically what we had on test2.py
    myDict = {}
    rest = []

    with open (filepath, 'r') as f:
        for line in f:
            if ':' in line:
                line = line.strip()
                parts = line.split(':')
                if parts[0].isupper():
                    key = parts[0]
                    value = parts[1]
                    myDict[key] = value
                else:
                    rest.append(line)
            else:
                rest.append(line)

    myDict['text'] = ''.join(rest)
    # End of test2.py

    # Now I'm saving this on a temporary list variable
    all_dicts.append(myDict)

# Now we save the all_dicts to file and we are done.
print('Saved to new file')
with open('dict.json', 'a') as f2:
    json.dump(all_dicts, f2, indent = 2)
