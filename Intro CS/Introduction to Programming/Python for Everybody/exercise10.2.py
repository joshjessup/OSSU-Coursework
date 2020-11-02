name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

hourCount = dict()

for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) <= 2:
            continue
#        try:
#            if words[2] is None:
#        except:
#            continue

        timeDist = words[-2].strip()
        timeDist = timeDist.split(':')
        hr = timeDist[0]

        hourCount[hr] = hourCount.get(hr,0) + 1

hourCount = sorted(hourCount.items())

for (k,v) in hourCount:
    print(k,v)
#tmp = list()
#for k,v in hourCount.items():
#    tmp.append((v,k))
#tmp = sorted(tmp, reverse=True)
