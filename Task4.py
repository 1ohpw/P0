"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

numbers = {}

for call in calls:
    numbers[call[0]] = True
    if call[3] in numbers:
        numbers[call[3]] = False
    for text in texts:
        if text[0] in numbers:
            numbers[text[0]] = False
        elif text[1] in numbers:
            numbers[text[1]] = False

telemarketers = [k for k,v in numbers.iteritems() if v]

print "These numbers could be telemarketers: "

telemarketers.sort()
for number in telemarketers:
    print number
