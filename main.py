import Universe as Universe
import Parser as Parser

player_name = ""

print("Welcome to Texels!")
    
while player_name == "":
    player_name = input("What is your name? ")
    
    print("Hey, " + player_name + ".")
    print("--------")
    print(Universe.introduction)

while True:  
    task = input("What would you like to do?")
    task = Parser.parse(task)
    
    if task is None:
        print("I don't understand that command.")
    
    if task == "exit":
        break
