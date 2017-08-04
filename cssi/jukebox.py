SONGS = ["uptown funk", "thinking out loud" , "blank space" , "take me to church" , "shake it off"]
def List():
    for song in SONGS:
        print song

def Play():
    print "Your choices are "
    List()
    song_number = input("Type song number : ")
    print "Now Playing " + SONGS[song_number - 1]

def Search():
    query = raw_input("Search Songs: ")
    found = False
    for song in SONGS:
        if query in song:
            print song
            found = True
    if not found:
        print "No songs match your search."
        print "Try again"
        Search()

def Quit():
    print "GoodBye"

def Jukebox():
    command = ' '
    while command != 'quit':
        command = raw_input("What do you want to do? list, play, search or quit")
        if command == 'list':
            List()
        if command == 'play':
            Play()
        if command == 'search':
            Search()
        if command == 'quit':
            Quit()
            return

        Jukebox()
