#Just importing some modules and added a variable called t_score to be 
#able to track the user's score on wether he wins or loses.

import random 
import time 
import sys 
t_score = 0 
name = ["Adam", "Lando", "Muhammad", "RandomGuyOnTheStreet"]
result = random.choice(name)

#Print and pause function to make it easier for the reader to read and 
#instead of having to write time.sleep every time I write a code

def print_pause(text, seconds=2):
    print(text)
    time.sleep(seconds)

#This is where the true story starts, The first decision.

def story():
    options = {
        '1': forest,
        '2': house1,
    }
    print("1 - Explore the forest")
    print("2 - Find your way back")
    choice = input("Please enter a number 1 or 2: ")
    while choice not in options:
        print('Invalid input, Please try again')
        story()
    options[choice]()
    

#This is the first House, if the user chose this they win automatically.
#Most users are dumb though, they wouldn't go back they want to explore.

def house1():
    t_score = 2
    print("You chose to go back to your house!")
    print_pause("Honestly, you are quite a boring person."
                " You survived the night though.")
    print("Your score is:", t_score)
    if t_score > 0:
     print("Congratulations! You won!")
    elif t_score <0:
     print("You lost.")
    win_lose()

#Deep dark forest, just another function that tells the story of what happens
#If they chose the forest, which statistically users will choose this more than
#Than the house.

def forest():
    print("You choose to explore the forest, you've got some guts.")
    print_pause("You head down to the forest, "
                "you walk for miles and miles, it doesn't seem to end though...")
    print_pause("You think to yourself, 'Am I seriously lost?'"
                ",you suddenly remember that you have a map and in your right pocket "
                "and a compass on your phone.")
    side()

# After winning or losing this function determines if they want to play again

def win_lose():
    options = {
        'y': main,
        'n': end_game
    }
    choice = input("Do you want to play again, y/n? ")
    if choice in options:
        options[choice]()
    else:
        print("Invalid Response. Try Again!")
        win_lose()
                
# function to store what will happen in the house the second time.

def house():
    house1()
    win_lose()

#function for the map that saves the user

def Map():
  t_score = 1
  print_pause("You open the map")
  print_pause("You find out your exact location"
        " and you are able to get out of the forest")
  print("Your score is:", t_score)
  if t_score > 0:
    print("Congratulations! You won!")
  elif t_score <0:
    print("You lost.") 

  win_lose()

#Function if the user chooses explore (this is the only one that makes him die)
#Between the three choices

def explore():
    t_score = -1
    print_pause("For some reason you are so dumb to think of exploring,"
        " you are acting like one of those dumb characters")
    print_pause("The character that would choose the darkest pit of hell"
        " instead of the gates to heaven")
    print("You die, Slender Man catches you lacking.")
    print("Your score is:", t_score)
    print_pause("You lose, you are a defect to humanity.")
    win_lose()

#function for the MAIN game, the start of the story.

def game():
    print("Hey", result)
    print_pause("You are in a forest, a huge forest, at night,"
         " it's like one of those horror movies forests.")
    print_pause("Rumour has it that there have been some "
        'sightings' " of a white tall man," 
        " approximately 6-7 feet tall he has no hair,"
        " and generally has normal-looking bare hands,"
        " he basically just wonders around.")
    print_pause("They say he might have been the cause to some murders,"
        " but there isn't really any evidence to back that up.")
    print_pause("Hey, you shouldn't worry though.")
    print_pause("It's probably not a big deal, probably even a myth,"
        " you know? So what do you plan on doing?")

# just a side function to use, so i don't get confused with other functions
# This can be used in the forest later on.

def side():
  while True:
    print("1 - Open the Map")
    print("2 - Open the compass on your phone")
    choice2 = input("Please enter 1 or 2: ")
    if choice2 == "1":
        Map()
        break
    elif choice2 == "2":
        story_Phone()
        break
    else: 
     print("Invalid input, Please try again.")


#Just a function that gives the user three more choices since the "phone"
#isn't working

def Phone():
   options3 = {
      "1": house,
      "2": Map,
      "3": explore,
   }
   choice90 = input("Enter a number 1, 2 or 3: ")
   if choice90 in options3:
      options3[choice90]()
   else:
      print("Invalid response, Try again!")
      Phone()

# Just a function that holds the story that is supposed to be within the phone.      

def story_Phone():
         print_pause("You try to open your phone and you come to realize,"
            " it's already dead.")
         print_pause("You still have a couple of choices though.")
         print("1 - Go back home")
         print("2 - Open the map")
         print("3 - Keep on exploring like a champ!")

         Phone() 

# Just functions that hold other functions

def main():
    game()
    story()
# End of the game function 

def end_game():
    print("Thank you for playing,"
          " 'The Slender Man Story Game.'")
    exit()

main()