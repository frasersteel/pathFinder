import urllib.request
import json

listOfPostcodes = [' SG6 4BA ', ' CT1 2FY ', ' SY15 6JQ ', ' GL16 7BY ', ' BA14 9QJ ', ' BL4 7DY ', ' W1B 4BZ ',
                   ' CA13 0ZL ', ' SA4 3DQ ', ' S1 2UQ ', ' BS2 9AD ', ' BA14 0NQ ', ' MK46 5DY ', ' ME1 2HG ',
                   ' HD8 8LH ', ' SY4 2HZ ', ' RH10 7RP ', ' SL9 8NR ', ' EX20 3NZ ', ' BD20 5DA ', ' LA12 7HR ',
                   ' WD7 8EE ', ' GU11 3UQ ', ' TD7 5LH ', ' PR4 0LA ', ' WS6 7EY ', ' CF32 0HY ', ' GL20 9SE ',
                   ' RM16 3AT ', ' BH23 5LS ', ' NN5 7BD ', ' RH11 7LP ', ' FY1 2RB ', ' E17 8QY ', ' CR8 5JG ',
                   ' LA14 4EJ ', ' KA12 8AX ', ' B7 4LL ', ' EH11 3NL ', ' SN8 1QU ', ' CA10 1UH ', ' IV51 9PP ',
                   ' AL1 3AZ ', ' DL1 2DZ ', ' DE13 0NT ', ' LN1 2AE ', ' DG4 6HB ', ' DE7 8TB ', ' RG14 1RU ',
                   ' BS5 0AN ', ' SW8 4JZ ', ' OL4 5TA ', ' ME13 7RS ', ' NG5 4AE ', ' SO53 2DE ', ' UB1 2JW ',
                   ' BD23 4RB ', ' YO21 1ET ', ' YO26 7PZ ', ' CA22 2RT ', ' EH14 2PL ', ' B31 2LD ', ' WA14 5AG ',
                   ' PR3 1SB ', ' PO4 8LS ', ' BA2 1NY ', ' CA12 4HD ', ' DN14 5UP ', ' TN26 2QP ', ' B68 9JA ',
                   ' CH62 6AL ', ' BT71 5QJ ', ' TN39 4BB ', ' HP15 6EX ', ' EN2 0AZ ', ' BS10 5AT ', ' BL9 8HD ',
                   ' BA4 5NE ', ' OX29 7LY ', ' W7 1NU ', ' NE25 8JQ ', ' KA5 5JT ', ' DH7 0RL ', ' PL17 7LR ',
                   ' RH13 0ST ', ' HU18 1ER ', ' RH10 7RT ', ' RH17 7NL ', ' CV21 3FH ', ' PO13 8HZ ', ' BS23 3BZ ',
                   ' PO8 0YR ', ' TF6 5DJ ', ' TR15 1PX ', ' CR0 3PH ', ' PL5 4AB ', ' ST9 0EZ ', ' ME7 5DX ',
                   ' SK6 7BN ', ' MK6 3HG ']


def lovelyFormattedListOfPostCodes():
    a = listOfRandomPostcodes()
    lenghtOfDesiredList = 10;
    for x in range(0, lenghtOfDesiredList*2):
        if (hasattr(a[x], "name")):
            print("'", a[x].name, "'", end='')
        else:
            print(a[x], end=" ")


def listOfRandomPostcodes():
    a = []
    numOfPostcodes = 100
    for x in range(0, numOfPostcodes):
        post = findRandomPostcode()
        a.append(post)
        a.append(",");
    return a


def findRandomPostcode():
    res = urllib.request.urlopen("http://api.postcodes.io/random/postcodes").read()
    data = json.loads(res.decode())
    post = PostCode(data["result"]["longitude"], data["result"]["latitude"], data["result"]["postcode"])
    return post;


class PostCode:
    def __init__(self, lng, lat, name):
        self.lat = lat
        self.lng = lng
        self.name = name


lovelyFormattedListOfPostCodes();
