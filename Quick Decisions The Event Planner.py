#Task 1 Code Correction: You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.
#Buggy code:
#attendees = input("Enter number of ateendees:")
#venue = "large hall" if attendees > 100 else "confrence room"
#print(venue)

#solution
attendees = int(input("Enter number of ateendees:"))          #our input either needs to be a float or int, since we're representing the number of people i chose int.
venue = "large hall" if attendees > 100 else "confrence room"
print(venue)

#Task 2 Venue Selection: Based on the corrected code from task 1, futher enhance your code to recommend additional things like "audio system"
# or "projector" based on the number of attendees.
attendees = int(input("Enter number of ateendees:"))
venue = "large hall" if attendees > 100 else "confrence room"
gear = "microphone, podium and a speaker" if attendees < 50 else "microphone, podium, and full sound system"      #added a gear variable and a shorthand if statement to give the user some recommednations for what gear to use based off how many attendees.
print("Based on the number of attendes we would recommend you set up in the", venue, "with a", gear)              #changed the final print statement to show the new gear variable

#Task 3 Catering Choices: Ask the user if they want "vegetrian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers"
attendees = int(input("Enter number of ateendees:"))
venue = "large hall" if attendees > 100 else "confrence room"
gear = "microphone, podium and a speaker" if attendees < 50 else "microphone, podium, and full sound system"     
food_choice = input("Do you want vegetarian food? (Yes/No):") 
caterer = "Veggie Delight Caterers" if food_choice == "Yes" else "Gourmet Meal Caterers"
print("Based on the number of attendes we would recommend you set up in the", venue, "with a", gear,". We would also recommend", caterer, "to cater the event.")


