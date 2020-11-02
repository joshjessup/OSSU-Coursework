name = input("Enter file: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emailList = dict()

for line in handle:
    if line.startswith('From'):
        words = line.split()
        if len(words) <= 2:
            continue
#        try:
#            if words[2] is None:
#        except:
#            continue

        email = words[1].strip()
        emailList[email] = emailList.get(email,0) + 1
#        print(emailList[email])

bigCount = None
bigEmail = None
for email, count in emailList.items():
    if bigCount is None or count > bigCount:
        bigEmail = email
        bigCount = count

print(bigEmail, bigCount)
