import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

sumVal = 0
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
#    print(data.decode())
    tree = ET.fromstring(data)

#################################################################
###Using tree.findall('.//count') to create list of count XML####
    counts = tree.findall('.//count')
    for count in counts:
        count = int(count.text)
        sumVal = sumVal + count
#################################################################
#################################################################


#################################################################
###Workng from top of XML down to comments node and then loop
###through the child nodes of the comments node.
#    for comments in tree.findall('comments'):
#        for comment in comments.findall('comment'):
#            sumVal += int(comment.find('count').text)
#################################################################
#################################################################


#################################################################
###Same as above, but using a list comprehension and sum()
#    sumVal = sum([int(count.text) for count in tree.findall('comments/comment/count')])
#################################################################
#################################################################

    print('Count:', len(counts))
    print('Sum:', sumVal)

#    lat = results[0].find('geometry').find('location').find('lat').text
#    lng = results[0].find('geometry').find('location').find('lng').text
#    location = results[0].find('formatted_address').text

#    print('lat', lat, 'lng', lng)
#    print(location)
