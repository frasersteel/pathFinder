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


def haversine(post1, post2):
    post1 = findPostCodeLongLat(post1)
    post2 = findPostCodeLongLat(post2)

    if ((post1.lng or post2.lng or post1.lat or post2.lat) is None):
        return 0

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


listOfPostcodes = ['CW123PN', 'TS251AQ', 'HD34RB', 'TN12 8NA', 'EX24EU', 'SG128TD', 'E981RT',
                   'S21JJ','SS30PS','TA94LB']


class Distance :
    def __init__(self, postcode1, postcode2, distance):
        self.postcode1 = postcode1
        self.postcode2 = postcode2
        self.distance  = distance

def listOfDistances(a):
    distances = []
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            value = haversine(a[i], a[j])
            dis = Distance(a[i],a[j],value)
            distances.append(dis)
    return distances


list = listOfDistances(listOfPostcodes)

newList = sorted(list, key=lambda Distance: Distance.distance)

for x in range(len(list)):
    print(newList[x].postcode1,newList[x].postcode2,newList[x].distance)

