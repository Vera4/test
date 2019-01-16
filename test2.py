import json

myDict = {}
rest = []

with open ('files/file_100.txt', 'r') as f:
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
print('Final dictionary: ')
print(json.dumps(myDict, indent=2))
