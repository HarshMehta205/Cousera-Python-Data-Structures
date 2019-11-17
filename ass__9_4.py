
#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

d = dict()
maximum = 0

for l in handle:
	l = l.rstrip()
	words = l.split()
	if not l.startswith("From "): continue
	d[words[1]] = d.get(words[1], 0) + 1

for k in d:
	if d[k] > maximum:
		maximum = d[k]
		KEY = k

print (KEY, maximum)
