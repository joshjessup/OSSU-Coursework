fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split()
    #print(words)
    #for i in range(len(words)):
    for i in words:
        #print(i)
        if i not in lst:
           lst.append(i)
        else:
            continue

lst.sort()
print(lst)
#print(line.rstrip())
