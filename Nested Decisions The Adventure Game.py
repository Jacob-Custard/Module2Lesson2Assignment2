#Task 1 Code Correction: You are provided with a Python script that is supposed to guide a user through and adventure game. but it has some errors. Identify and fix them.
#Buggy Code
#place = input("Choos a place: forest or cave?")
#if place = "forest":
#    action = input("Climb a tree or cross a river?")
#    if action = "climb a tree":
#        print("You found a bird's nest!")
#    else action = "cross a river":
#        print("You found a boat!")
#elif place = "cave":
#    print("You find a hidden treasure!")  

#solution
place = input("Choos a place: forest or cave?")
if place == "forest":                                  #fixed a syntax error. Needed the == to show that we were checkig to see if "place" was forest, we werent designating a variable.
    action = input("Climb a tree or cross a river?")
    if action == "climb a tree":                       #same syntax error as before needed == instead of =
        print("You found a bird's nest!")
    elif action == "cross a river":                    #changed else to elif because there is a condition associated with it, and you probably wouldnt "find a boat" if your action was "climb a hill" or "swing from tree" which with the else statement is what it would have printed out, also fixed the same syntax error as the previous 2.
        print("You found a boat!")
elif place == "cave":                                  #again the same syntax error needed == instead of =. I thought about using an else statement but this way more options for places can be added later if needed. And although the else statment could be changed later this rules out the possibilty of accidentally forgetting or missing the fact that there's an else statement in there that could cause problems down the road
    print("You find a hidden treasure!")                     

#Task 2 Setting the Scene: Based on your corrected code from Task 1, expand the game. If the user chooses "cave" ask them if they want to "light a torch" or "proceed in the dark"
#and provide outcomes for each decision.
place = input("Choos a place: forest or cave?")
if place == "forest":                                  
    action = input("Climb a tree or cross a river?")
    if action == "climb a tree":                       
         print("You found a bird's nest!")
    elif action == "cross a river":                    
        print("You found a boat!")
elif place == "cave":                                  
    action = input("light a torch or proceed in the dark?")                                         #added in an input to for people to choose between lighting a torch or not once theyve entered the cave
    if action == "light a torch":
        print("A sprawling cave network lights up before you, with many paths to choose from.")     #what happends if you light the torch
    elif action == "proceed in darkness":
        print("As a season adventurer, you move through the darkness with no hesitation.")          #what happens if you stay in the dark    

#Task 3 Default Path: If the user makes an invalid choice at any point, incorporte a pass statement to handle it.        
place = input("Choos a place: forest or cave?")
if place == "forest":                                  
    action = input("Climb a tree or cross a river?")
    if action == "climb a tree":                       
         print("You found a bird's nest!")
    elif action == "cross a river":                    
        print("You found a boat!")
    else:                                                              #added an else statement that will tell the user they left the forest if they dont select one of the two available actions
        print("You turn and leave the forest.")
elif place == "cave":                                  
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("A sprawling cave network lights up before you, with many paths to choose from.")
    elif action == "proceed in darkness":
        print("As a season adventurer, you move through the darkness with no hesitation.")
    else:
        print("You turn and leave the cave.")                        #again added an else statement that has the user leave if they dont select one of the 2 available actions
elif place == "town":                                                #my code doesn't break when somebody enters a wrong thing, it just returns nothing, so i'm not 100% certain what the task is asking for,
    pass                                                             #however i added this new elif and pass statement to show/simulate being in the middle of wanting to add a 3rd place, town, but not having fleshed in out yet, so if somebody enters "town" it'll just skip over it
