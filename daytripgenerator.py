#1. As a developer, I want to make at least three commits with descriptive messages
#2. Store destinations, restaurants, transportation, and entertainment in separate lists
#3. Randomly select destination
#4. Randomly select transportation
#5. Randomly select entertainment
#6. Randomly select restaurant
#7. Enable user to reselect choices
#8. Enable user to confirm trip
#9. Display trip plans in the consol3
import random

greeting = "Hello, welcome to the Day Trip Generator! We can help you plan your next adventure!"
user_steps = "Here you can select your choice for your destination, transportation, entertainment, and dining options."
next_step = "Let's get started!"

destinations = ['Washington D.C.', 'Seattle', 'New Orleans', 'San Diego']
transportation = ['plane', 'trolley', 'rental car', 'Uber']

entertainment = ['entertainment_DC', 'entertainment_Seattle', 'entertainment_NOLA', 'entertainment_SD']
entertainment_DC = ['touring the National Mall', 'visiting the Smithsonian', 'the White House tour', 'The Changing of the Guard at Arlington National Cemetery']
entertainment_Seattle = ['Pikes Place Market', 'The Beneath the Streets, Underground History Tour', 'the Seattle Harbor Cruise', 'seeing Bruce Lees Grave']
entertainment_NOLA = ['the Oak Alley Plantation Tour', 'spending the day on Bourbon St.', 'the Haunted New Orleans tour', 'touring the Cemeteries and Voodoo Shops']
entertainment_SD = ['going on a La Jolla Sea Caves Kayak Tour', 'the USS Midway tour', 'going on a Whale Watching Cruise', 'having a Day at the Beach']

restaurants = ['restaurant_DC', 'restaurant_Seattle', 'restaurant_NOLA', 'restaurant_SD']
restaurant_DC = ['1789 Restaurant', 'The Dabney', 'Old Ebbitt Grill', 'Martins Tavern']
restaurant_Seattle = ['Ivars', 'The Pink Door', 'The Walrus and the Carpenter', 'Umi Sake House']
restaurant_NOLA = ['Olde Nola Cookery', 'Mais Arepas', 'Atchafalaya', 'Criollo Restaurant']
restaurant_SD = ['Harney Sushi', 'The Mission - East Village', 'Oceana Coastal Kitchen', 'Hash House A Go Go']


def dest_options(destinations):
    proceed = False
    while proceed == False:
        choose_place = random.choice(destinations)
        print(f'Would you like to go to {choose_place}?')
        response = input("enter yes or no: ")
        if response == "yes":
            proceed = True
            print(f'That will be so fun! Enjoy {choose_place}!')
            return choose_place 
            

def trans_options(transportaion):
    proceed = False
    while proceed == False:
        choose_trans = random.choice(transportaion)
        print(f'Would you like to travel by {choose_trans}?')
        response = input("enter yes or no: ")
        if response == "yes":
            proceed = True
            print(f'Ok, you will travel buy {choose_trans}!')
            return choose_trans


def ent_options(current_destination):
    proceed = False
    while proceed == False:
        if current_destination == destinations[0]:
            choose_ent = random.choice(entertainment_DC)
            print(f'Options for activites include: {choose_ent}')
            response = input("Does this sound fun? enter yes or no: ")
            if response == "yes":
                proceed = True
                print(f'What a great way to learn about this city, enjoy {choose_ent}. ')
                return choose_ent
        if current_destination == destinations[1]:
            choose_ent = random.choice(entertainment_Seattle)
            print(f'Options for activites include: {choose_ent}')
            response = input("Does this sound fun? enter yes or no: ")
            if response == "yes":
                proceed = True
                print(f'What a great way to learn about this city, enjoy {choose_ent}. ')
                return choose_ent
        if current_destination == destinations[2]:
            choose_ent = random.choice(entertainment_NOLA)
            print(f'Options for activities include: {choose_ent}')
            response = input("Does this sound fun? enter yes or no: ")
            if response == "yes":
                proceed = True
                print(f'What a great way to learn about this city, enjoy {choose_ent}. ')
                return choose_ent
        if current_destination == destinations[3]:
            choose_ent = random.choice(entertainment_SD)
            print(f'Options for activities include: {choose_ent}')
            response = input("Does this sound fun? enter yes or no: ")
            if response == "yes":
                proceed = True
                print(f'What a great way to learn about this city, enjoy {choose_ent}. ')
                return choose_ent
                

def rest_options(current_destination):
    proceed = False
    while proceed == False:
        if current_destination == destinations[0]:
            choose_rest = random.choice(restaurant_DC)
            print(f'Dinner options include: {choose_rest}')
            response = input("Would you like to go here for dinner? enter yes or no: ")
            if response == "yes":
                proceed = True
                print(f'This place has great reviews, I hope you like {choose_rest}')
                return choose_rest
        if current_destination == destinations[1]:
            choose_rest = random.choice(restaurant_Seattle)
            print(f'Dinner options include: {choose_rest}')
            response = input("Would you like to go here for dinner? enter yes or no: ")
            if response == "yes":
                proceed = True
                print(f'This place has great reviews, I hope you like {choose_rest}')
                return choose_rest
        if current_destination == destinations[2]:
            choose_rest = random.choice(restaurant_NOLA)
            print(f'Dinner options include: {choose_rest}')
            response = input("Would you like to go here for dinner? enter yes or no: ")
            if response == "yes":
                proceed = True
                print(f'This place has great reviews, I hope you like {choose_rest}')
                return choose_rest
        if current_destination == destinations[3]:
            choose_rest = random.choice(restaurant_SD)
            print(f'Dinner options include: {choose_rest}')
            response = input("Would you like to go here for dinner? enter yes or no: ")
            if response == "yes":
                proceed = True
                print(f'This place has great reviews, I hope you like {choose_rest}')
                return choose_rest


def entry_message():
    print(greeting)
    print(user_steps)
    print(next_step)


def run_daytrip_generator():
    entry_message()
    chosen_destination = dest_options(destinations) 
    chosen_transportation = trans_options(transportation)
    chosen_entertainment = ent_options(chosen_destination)
    chosen_restaurant = rest_options(chosen_destination)  
    print(f'Ok, you have chosen to go to {chosen_destination} and you will travel by {chosen_transportation}.  While you are there, you will be/do {chosen_entertainment} and finish your day with a fantastic meal at {chosen_restaurant}')
    final_confirmation()


def final_confirmation():
    confirmation = input("Are you happy with these selections? (yes or no)")
    if confirmation == "yes":
        print("Awesome! Hope you have a great time on your trip! Thank you for using the Day Trip Generator, come again soon :) ")
    elif confirmation == "no":
        run_daytrip_generator()
        
run_daytrip_generator()


