azLots = [
    {"address": "5905 Red Moon Trl",
     "city": "Williams",
     "state": "AZ",
     "zipcode": "86049",
     "asking price": "$19947",
     "acreage": "42.14"
     },
    {"address": "9460 Quarter Master Trl",
     "city": "Snowflake",
     "state": "AZ",
     "zipcode": "85937",
     "asking price": "11987",
     "acreage": "40"
     },
    {"address": "0 S Jesse James Rd",
     "city": "Yucca",
     "state": "AZ",
     "zipcode": "86438",
     "asking price": "$9990",
     "acreage": "20"
     },
    {"address": "6900 Pffj Rd",
     "city": "Snowflake",
     "state": "AZ",
     "zipcode": "85937",
     "asking price": "$8947",
     "acreage": "38.03"
     },
    {"address": "0 County Road 6114",
     "city": "Saint Johns",
     "state": "AZ",
     "zipcode": "85936",
     "asking price": "$12900",
     "acreage": "40"
     },
    {"address": "Owens Whitney Elemental District",
     "city": "Wikieup",
     "state": "AZ",
     "zipcode": "85360",
     "asking price": "$8900",
     "acreage": "20"
     },
    {"address": "Lot 1273 Sandy Faye Way",
     "city": "Seligman",
     "state": "AZ",
     "zipcode": "86337",
     "asking price": "$17995",
     "acreage": "37.39"
     },
    {"address": "S Marauder Lot Wikieup",
     "city": "Wikieup",
     "state": "AZ",
     "zipcode": "85360",
     "asking price": "$14450",
     "acreage": "38.37"
     },
    {"address": "826 Tower Rd",
     "city": "Peach Springs",
     "state": "AZ",
     "zipcode": "86434",
     "asking price": "$19947",
     "acreage": "43.19"
     },
    {"address": "2045 E Calle Copala",
     "city": "Kingman",
     "state": "AZ",
     "zipcode": "86409",
     "asking price": "$19900",
     "acreage": "40"
     },
    {"address": "5939 Mesa View Dr",
     "city": "Winslow",
     "state": "AZ",
     "zipcode": "86047",
     "asking price": "$19995",
     "acreage": "40.34"
     },
]
sortedListByAcres = sorted(azLots, key=lambda item: item['acreage'], reverse=True)

# Via Mike's recommendation the sorted lists have been dropped into variables
#
#
# makes it easier to use the for loop for the list with variables
for item in sortedListByAcres:
    print(item)


print(sortedListByAcres)

# todo: Determine avg price per acre
# Todo: To calculate the price per acre, create custom function
# Todo: Utilize int() /float() in custom function
# Todo: Dictionary that contains price per acre
# testing function for acreage in azLots:
#     print(int('acreage')) in console
# Result: got whole list instead of the actual acreage BOTTOM LINE: Failed
# going to try azLots(int('asking price') / float('acreage') in console
# result: Typeerror: List object is not callable, tried different variations
# Testing for asking in azLots:
# ...     print() in different variations: feels like im getting closer. (semantic errors right? lol been reading a lil)
# after watchin lesson 5 videos for the 1000th time finally was able to come up with this :
#     def price_per_acre(asking_price, acreage):
#     """
#
#     :type acreage: float
#     """
#     int(asking_price)
#     "/"
#     = price_per_acre
#     Ima retreat for now but feels like i made some progress
# to create a custom function that would get the price per acre, i'd have to divide the asking price by the acres.
# from the list itself. azLots('asking price'/ 'acreage') = Typeerror: unsupported operand type for /: 'str' and
# 'str'. now how do i turn the string to a numeral??

