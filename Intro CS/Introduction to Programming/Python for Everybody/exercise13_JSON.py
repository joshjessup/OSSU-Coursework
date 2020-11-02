import urllib.request, urllib.parse, urllib.error
import json
import ssl

count = 0
sumVal = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter data location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

print('Retrieved', len(data), 'characters')
info = json.loads(data)
print('User count:', len(info['comments']))
#print(info)

for item in info['comments']:
    if item['count'] is not None:
        count += 1
        sumVal += item['count']


##LIST COMP######################################################
#sumVal = sum(item['count'] for item in info['comments'])
#################################################################

print('Count:', count)
print('Sum:', sumVal)
