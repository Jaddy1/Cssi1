# # # VOWELS = ["A", "E", "I", "O", "U"]
# # #
# # # def LongShout(word, multiplier):
# # #     word = word.upper()
# # #     count = 1
# # #     for vowel in VOWELS:
# # #         long_vowels = vowel * multiplier*count
# # #         word = word.replace(vowel, long_vowels)
# # #         count += 1
# # #
# # #     return word
# # #
# # # print LongShout("Jessie Douglas", 5)
# # # print LongShout("AEIOU", 1)
# #
# # # groceries = {"eggs": 5, "butter": 4, "chocolate": 2}
# # # for item in groceries:
# # #     price = groceries(item)
# # #     print item + ": $ " + str(price)
# # #
# # # def speak_to_Wallke
# #
# # class Musician:
# #     def __init__(self, name, instrument, song, recording):
# #         self.name = name
# #         self.instrument = instrument
# #         self.song = song
# #         self.recording = recording
# #
# #     def description(self):
# #         return "Hey my name is {0}, I play {1}, and my favorite song is {2}".format(self.name, self.instrument, self.song)
# #
# #     def is_recording(self):
# #         if self.recording:
# #             return "Woohoo I'm recording"
# #         else:
# #             return "nah maybe later, I'm napping"
# #
# # kanye = Musician('kanye', 'vocals', 'famous', True)
# # chance = Musician('chance', 'rapper', 'no problem', False)
# #
# # print kanye.description()
# # print chance.description()
# # print kanye.is_recording()
# # print chance.is_recording()
#
# from random import randint
#
# roll1 = randint(1, 6)
# roll2 = randint(1, 6)
#
# def RollDice():
#     score_sum = roll1 + roll2
#     if roll1 == roll2:
#         print "Doubles! Move {} spaces and roll again.".format(str(score_sum))
#     else:
#         print "Move {} spaces. Next player's turn!".format(str(score_sum))
#
# RollDice()
#
# def RollDungeonsAndDragonsDie(number_of_sides, modifier):
#     modifier = number_of_sides + 2
#
# def RollManyDungeonsAndDragonsDie(sides):
#     total = 0
#     for side in sides:
#         roll = randint(1, number_of_sides)
#         total += roll
#     print "You may move " + str(total) + " spaces!"





# #Roling Dice Lab
# import random
#
# # i = 0
# die1 = random.randint(1, 6)
#
# die2 = random.randint(1, 6)
#
# rolls = 0
# while die1 + die2 != 12:
#     rolls += 1
#     die1 = random.randint(1, 6)
#
#     die2 = random.randint(1, 6)
#     if die1 + die2 == 2:
#         print "Got snake eyes!"
#     elif die1 == 6 and die2 == 6:
#         print "Got double sixes!"
#     print "Rolls: {0} {1}".format(die1, die2)
#     print "Rolled the dice {} times".format(rolls)



#JukeBox Lab
songs = ["uptown funk", "thinking out loud" , "blank space" , "take me to church" , "shake it off"]
def JukeBox():
    # for song in songs:
    # user_option = raw_input("What would you like to do? Play a song, List, Search for a song, or Quit?")
    # if user_option == "Play":
    #     raw_input("What song would you like to play? {}, {}, {}, or {}?".format(songs[0], songs[1], songs[2], songs[3], songs[4]))
    # elif user_option == "List":
    #     print "Your song options are: {}, {}, {}, {}, and {}".format(songs[0], songs[1], songs[2], songs[3], songs[4])
    # elif user_option == "Search":
    #     raw_input("What would you like to search?")
    # elif user_option == "Quit":
    #     quit()
    # for song in songs:
    #     song = raw_input("What would you like to do? Play a song, List, Search for a song, or Quit?")
    #     if user_option == "Play":
    #         raw_input("What song would you like to play? {}, {}, {}, or {}?".format(songs[0], songs[1], songs[2], songs[3], songs[4]))
    #     elif user_option == "List":
    #         print "Your song options are: {}, {}, {}, {}, and {}".format(songs[0], songs[1], songs[2], songs[3], songs[4])
    #     elif user_option == "Search":
    #         raw_input("What would you like to search?")
    #     elif user_option == "Quit":
    #         quit()
    #
    #     print song
    # print song
    for song in songs:
        print song

JukeBox()
