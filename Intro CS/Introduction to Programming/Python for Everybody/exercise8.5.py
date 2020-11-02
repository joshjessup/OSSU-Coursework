#filename: mbox-short.txt
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith('From'):
        words = line.split()
        if len(words) <= 2:
            continue
#        try:
#            if words[2] is None:
#        except:
#            continue
        email = words[1].strip()
        print(email)
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
