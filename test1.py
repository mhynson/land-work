# Client wants a list of 10 plots in the Arizona area That include street address, city, state, zipcode asking
#  price and the number of acres
# Sort the list in 2 dif ways: Largest to smallest plot, cheapest to most expensive
# todo: Determine avg price per acre
# Represent lis of plots as list_of_dictionaries // Used azLots
# Todo: To calculate the price per acre, create custom function
# Print sorted lists to the console, DONE
# Todo: Dictionary that contains price per acre


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
print(sorted(azLots, key=lambda item: item['acreage'], reverse=True)) # Its smallest to largest, tried to get the reverse=true but
# it wasnt working for me.
#
# I didn't captialize the T in True. smh thanks for that: learned something
#
#
# Also how do I get them i true list format, like in columns instead of rows??? comment here
# to lemme know //azLots.sort(reverse=true) ... print(azLots) gave me a nameerror // is it because i put a dict in a
# list?? comment here to put me on. https://www.w3schools.com/python/trypython.asp?filename=demo_ref_list_sort5
#
#
#
#Tried this print("column format : " + xAddress + xCity + xZipcode + float(xAsking) + float(xAcreage)) but gotta type error.
# right side of console got the variables as a dict.

print(sorted(azLots, key=lambda item: item['asking price']))

# to create a custom function that would get the price per acre, i'd have to divide the asking price by the acres.
# from the list itself. azLots('asking price'/ 'acreage') = Typeerror: unsupported operand type for /: 'str' and
# 'str'. now how do i turn the string to a numeral??

