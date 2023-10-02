import re

# Define the regular expression pattern
pattern = "New Revision: (\\d+)"

new = []

fhand = open("mbox.txt")
for line in fhand:
    if re.search(pattern, line):
        new.append(line.split(" ")[2].strip('\n'))

nums = list(map(int, new))

sigma = 0

for num in nums:
    sigma += num

print(sigma / len(nums))