import urllib.request
import json
from math import radians, cos, sin, asin, sqrt


class PostCode:
    def __init__(self, lng, lat, name):
        self.lat = lat
        self.lng = lng
        self.name = name


def findPostCodeLongLat(postcode):
    res = urllib.request.urlopen("http://api.postcodes.io/postcodes/" + postcode).read()
    data = json.loads(res.decode())
    post = PostCode(data["result"]["longitude"], data["result"]["latitude"], postcode)
    return post;


def findRandomPostcode():
    res = urllib.request.urlopen("http://api.postcodes.io/random/postcodes").read()
    data = json.loads(res.decode())
    post = PostCode(data["result"]["longitude"], data["result"]["latitude"], data["result"]["postcode"])
    return post;


def listOfRandomPostcodes():
    a = []
    numOfPostcodes = 100
    for x in range(0, numOfPostcodes):
        post = findRandomPostcode()
        a.append(post)
        a.append(",");
    return a


def haversine(post1, post2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    lon1 = post1.lng
    lat1 = post1.lat
    lon2 = post2.lng
    lat2 = post2.lat
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6373.0  # Radius of earth in kilometers. Use 3956 for miles
    return c * r




listOfPostcodes = [' W4 1RT ', ' L23 0TX ', ' N7 6DS ', ' S44 6EJ ', ' NN13 7FD ', ' CT1 3ZD ', ' RG20 9PU ',
                   ' WF9 4BL ', ' ML8 4FF ', ' LL40 2NT ', ' SY21 8NX ', ' G42 7LW ', ' TS14 6NY ', ' KT10 0AU ',
                   ' M33 2GG ', ' AB54 7LE ', ' SY3 9NZ ', ' NE10 9DT ', ' BT62 2AY ', ' SA65 9HJ ', ' TS19 0NJ ',
                   ' MK11 1AF ', ' BT32 3YD ', ' IV2 3XJ ', ' SA3 5DJ ', ' AL10 9LF ', ' RG4 5AE ', ' GU29 0AQ ',
                   ' GU29 0LD ', ' M24 4LU ', ' TN14 5GD ', ' SA72 4UP ', ' SG8 5UP ', ' SY15 6HL ', ' ML6 8QZ ',
                   ' L3 6AL ', ' DL13 2WX ', ' S3 9LF ', ' NW7 2EZ ', ' B19 1HB ', ' IM2 3BY ', ' SY3 7QP ',
                   ' WF11 9HN ', ' LE12 8GY ', ' TA23 0HR ', ' BD16 2QA ', ' NW7 4LH ', ' SW16 4UD ', ' LS12 1YN ',
                   ' WV12 4LY ', ' DN34 4PN ', ' WR2 6QR ', ' SA31 3NA ', ' EH4 1JD ', ' FK10 2HX ', ' WN2 4NY ',
                   ' CO5 0AE ', ' LS4 2NQ ', ' HU13 0LA ', ' ME19 6SR ', ' SL5 7PR ', ' HP18 0DU ', ' JE2 6LL ',
                   ' GY1 1FR ', ' SP8 4NW ', ' FY4 1SX ', ' LU5 5ZX ', ' HD1 4TR ', ' RH13 6AG ', ' TS19 0BG ',
                   ' TN3 0BS ', ' BT53 8NE ', ' MK45 1JF ', ' HU19 2LU ', ' WA11 0HL ', ' OX25 5QA ', ' CF15 8DH ',
                   ' CF82 8HA ', ' IP6 0BA ', ' PH33 7BD ', ' BT93 5ES ', ' BT80 8WU ', ' PE22 7RE ', ' L5 9RX ',
                   ' SE17 1BP ', ' BT1 4DR ', ' WN5 7HD ', ' LU2 0EB ', ' SN14 8BX ', ' DN22 0AR ', ' LS10 3TJ ',
                   ' NG15 6TE ', ' EX1 1BE ', ' LE67 6JD ', ' IV31 6BZ ', ' BA1 1SR ', ' CW9 7XU ', ' YO42 1QY ',
                   ' WV6 9NR ', ' DH1 3EW ']


def listOfDistances(a):
    distances = []
    for x in range(0,(len(a))-1):
        distances[x] = haversine(findPostCodeLongLat(a[x]), findPostCodeLongLat(a[x-1]))
    return distances


list = listOfDistances(listOfPostcodes)

print(len(list))