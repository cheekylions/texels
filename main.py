import Universe

player_name = ""

while 1:
    print("Welcome to Texels!")
    
    while player_name == "":
        player_name = input("What is your name? ")
    
        if type(player_name) is not str:
            print("That's not a name!")
            player_name = ""
            player_name = input("What is your name?")