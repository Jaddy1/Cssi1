# x = 100
#
# if x > 500:
#     print "x is really big"
# elif x <= 500 or x > 50:
#     print "x is sort of big"
# elif x < 0:
#     print "x is negative"
# else:
#     print "x is not very interesting"

# groceries = ["Eggs", "Milk", "Butter"]
#
# print groceries[0]
# x = range(100, 1, 1)
# print x

#Add Ten and Divide by Two Lab
# some_numbers = [2, 52, 19, 46, 1000]
# index = 0
#
# for number in some_numbers:
#     number += 10
#     number /= 2
#     print number
#     index +=1

#Reverse Presidents Lab
# presidents = ["George Washington", "John Adadms", "Thomas Jefferson",
#  "James Madison", "James Monroe", "John Quincy Adams"]
# for words in presidents:
#     words = words[::-1]
#     print words

#Bonus Questions for LOOP Q 1
# some_string = raw_input("Type Something: ")

#Bonus Questions for LOOP Q 2
# number_array = [1, 2, 3]
# for words in number_array:
#     numbers = index[::-1]
#     print numbers

#10 Bottles on the wall Lab
bottles = range(10,0,-1)


for numbers in bottles:
    print ("{} bottles of milk on the wall").format(numbers)
    print numbers
