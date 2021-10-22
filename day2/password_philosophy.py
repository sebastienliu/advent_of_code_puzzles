import re

inputFileName = "password_policies.txt"
inputFile = open(inputFileName, "r")

passwordEntries = list()
for line in inputFile:
    passwordEntries.append(line)
inputFile.close()

validPassword = 0
for item in passwordEntries:
    item = item.strip()
    template = re.findall("(\d+)-(\d+) (.): (.+)", item)
    low = int(template[0][0])
    high = int(template[0][1])
    letter = template[0][2]
    passcode = template[0][3]

# For day2 part1
    matchLetterCount = 0
    for lett in passcode:
        if lett == letter:
            matchLetterCount += 1

    if matchLetterCount >= low and matchLetterCount <= high:
        validPassword += 1

# For day2 part2
    if passcode[low - 1] == letter and passcode[high - 1] != letter:
        validPassword += 1
    elif passcode[low - 1] != letter and passcode[high - 1] == letter:
        validPassword += 1

print(f"Total amount of valid passwords: {validPassword}")
