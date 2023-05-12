import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter Location: ')
    # get out of loop on enter
    if len(address) < 1: break
    
    params = dict()
    params['address'] = address
    if api_key is not False: params['key'] = api_key

    # concatonate to make full string for API call
    url = serviceurl + urllib.parse.urlencode(params)

    print('Retrieving', url)
    urlHandle = urllib.request.urlopen(url, context=ctx)
    data = urlHandle.read().decode()
    print('Retrieved', len(data), 'characters')

    # set resusts to json except when none
    try:
        js = json.loads(data)
    except:
        js = None

    # if no object returned, or lacks status, or status is not ok
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    
    # pretty print with indenting
    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat:', lat, 'lng:', lng)
    location = js['results'][0]['formatted_address']
    print(location)

    # Google API SAYS NO!