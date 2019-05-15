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
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""
phoneNumbers = {}

for text in texts:
    if text[0] not in phoneNumbers:
        phoneNumbers[text[0]] = None
    if text[1] not in phoneNumbers:
        phoneNumbers[text[1]] = None

for call in calls:
    if call[0] not in phoneNumbers:
        phoneNumbers[call[0]] = None
    if call[1] not in phoneNumbers:
        phoneNumbers[call[1]] = None

print "There are " + str(len(phoneNumbers)) + " different telephone numbers in the records."
