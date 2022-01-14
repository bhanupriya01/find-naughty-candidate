# Write a program that can tell the principal both the least and the most naughty candidate in the list.

# Input
#   1. N – number of entries in the list
#   2. For each I in N
#       a. Name of the candidate
# Output
#   1. Most Naughty candidate’s name
#   2. Least Naughty candidate’s name

# taking list length
listLen = input("N –")

# taking name list
nameList = list()
for i in range(0, int(listLen)):
    nameList.append(input())
    
# counting occurance
occuranceList = list()
for name in nameList:
    occuranceList.append(nameList.count(name))

# candidate name and occurance pairing
nameDict = {}
for i in range(0, int(listLen)):
    nameDict[nameList[i]] = occuranceList[i]

# duplicate key removed
values = list(nameDict.values())
keys = list(nameDict.keys())

# getting min and max occurance
minval = min(values)
maxval = max(values)

# listing most naught student and least naught student
most = list()
least = list()
for key in keys:
    if nameDict[key] == minval:
        least.append(key)
    elif nameDict[key] == maxval:
        most.append(key)
        
# preparing for output
mostNaught = ''
for name in most:
    if most.index(name) == 0:
        mostNaught = name
    else:
        mostNaught += ", " + name

leastNaught = ''
for name in least:
    if least.index(name) == 0:
        leastNaught = name
    else:
        leastNaught += ", " + name

# Output
print("Most naughty – " + mostNaught)
print("Least naughty – " + leastNaught)