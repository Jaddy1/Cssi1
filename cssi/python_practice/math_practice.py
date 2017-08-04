# import math
# def SquaringFormula(x):
#     return Square(x)
# def CircleArea(r):
#     return 3.14 * Square(x)
# def CircumferenceFormula(z):
#     return 2 * 3.14 * z
# def DistanceFormula(x1,y1,x2,y2):
#     return math.sqrt(Square(x2-x1)-Square(y2-y1))
#     # value_1 = x2 - x1
#     # value_2 = y2 - y1
#     # value_3 = value_1 ** 2 + value_2 ** 2
#     # return math.sqrt(value_3)


# def SwapEnds(some_list):
#     some_list[0] = some_list[-1]
#
# def MessWithList(my_list):
#     SwapEnds(my_list)
#     my_list.append(5)
#
# a_list = [1, 2, 3, 4]
# print a_list
# MessWithList(a_list)
# print a_list

#Parrot Lab
# def BoringParrot():
#     print "I say what you want me to say"
#
# def MathParrot(x, y):
#     print x + y
#
# def FriendlyParrot(name, age):
#     print "Hey {}, I heard you were {} years old".format(name, age)
#
# def FavoritesParrot(favorites):
#     print "Wow! I love {} too".format(favorites)
#
# def reversed(string):
#     string = string[::-1]
#     print string
#
# BoringParrot()
# MathParrot(3, 25)
# FriendlyParrot("Jeffron", 17)
# FavoritesParrot("Ice Cream")
# reversed(BoringParrot())

# sandwich = [["rye", "sourdough", "baguette"],
#             [["ham", "salami", "turkey"],
#              ["swiss", "munster", "cheddar"]],
#             ["mayo", "mustard", "tabasco"]]
# print sandwich[2]
# print sandwich[1][1][2]
# print sandwich[0][1]

city_info = {'new_york' : { 'mayor' : "Bill DeBlasio",
                            'population' : 8406000,
                            'website' : "http://www.nyc.gov"
                            },
             'los_angeles' : { 'mayor' : "Eric Garcetti",
                            'population' : 3884307,
                            'website' : "http://www.lacity.org"
                            },
             'miami' : { 'mayor' : "Tomas Regalado",
                            'population' : 417650,
                            'website' : "http://www.miamigov.com"
                            },
             'chicago' : { 'mayor' : "Rahm Emanuel",
                            'population' : 2719000,
                            'website' : "http://www.cityofchicago.org/"
                            }
        }

print city_info ['new_york']['population']
print city_info ['miami']['website']
print city_info ['los_angeles']['mayor']
print city_info ['chicago']

for city in city_info:
    for info in city_info[city]:
        print "The " + info + " of " + city + " is " + str(city_info[city][info])
