'''
Project 3 - Hotel Reservation System (Part 3) - Spring 2026  
Author: Brooks Morgan and brooksm07 

My program simulates a basic hotel reservation system. Users can create, view, edit, delete, save, and load reservations. Each reservation has a unique ID and is stored in a dictionary.

I have neither given or received unauthorized assistance on this assignment.
Signed:  Brooks Morgan
'''

import random



def calculate_discounted_rate(standard_rate, age):
    '''
    Returns the nightly rate after applying age discounts.
    
    Parameters:
    standard_rate (float): base nightly rate
    age (int): guest age
    
    Returns:
    float: discounted rate
    '''
    if age < 22:
        return standard_rate * 0.90
    elif age > 64:
        return standard_rate * 0.85
    else:
        return standard_rate
    
def determine_standard_rate(room_type):
    '''
    Returns the standard nightly rate based on the room type.
    
    Parameters:
    room_type (str)
    
    Returns:
    float
    '''
    room_rates = {
        'single': 100.00,
        'double': 125.00,
        'king': 150.00,
        'suite': 200.00
        }
    return room_rates[room_type]


def calculate_reservation_total(room_type, nights, age):
    '''
    Finds the total cost of the stay based on the number of nights, the nightly rate, and the taxes.
    
    Returns:
    float
    '''
    standard_rate = determine_standard_rate(room_type)
    nightly_rate = calculate_discounted_rate(standard_rate, age)
    subtotal = nights * nightly_rate
    total = subtotal * 1.06
    return total

def get_new_reservation_id(all_reservations):
    '''
    Generates a unique reservation ID.
    '''
    while True:
        number = random.randint(100, 999)
        new_id = "PHS-734-" + str(number)
        if new_id not in all_reservations:
            return new_id
    
    

def create_reservation(all_reservations):
    '''
    Asks the user for their information and prints the cost of the reservation.
    '''
    
    print("Creating new reservation...")
    
    first = input("What is the guest's first name? ")
    last = input("What is the guest's last name? ")
    room = input("What type of room (single, double, king, suite)? ")
    while room not in ['single', 'double', 'king', 'suite']:
        room = input("Invalid room type. Please reenter: ")
    nights = int(input("How many nights? "))
    age = int(input("What is the age of the primary guest? "))
    
    total = calculate_reservation_total(room, nights, age)
    
    print(f"The cost of this reservation for {first} {last} is ${total:.2f}.")
    
    reservation_id =  get_new_reservation_id(all_reservations)
    print(f"The reservation ID is {reservation_id}")
    
    all_reservations[reservation_id] = [first, last, room, nights, age]
    return all_reservations

def print_menu():
    '''
    Prints the menu options
    '''
    print("Select an option from the following menu:")
    print("1. Create a reservation")
    print("2. View reservations")
    print("3. Edit reservation")
    print("4. Delete reservation")
    print("5. Save reservations")
    print("6. Load reservations")
    print("7. Exit the program")
    
def view_reservations(all_reservations):
    '''
    Displays all reservations
    '''
    if len(all_reservations) == 0:
        print("No reservations found.")
        return
    
    print("Current reservations:\n")
    
    for res_id in all_reservations:
        first, last, room, nights, age = all_reservations[res_id]
        
        print(f"Reservation ID: {res_id}")
        print(f"Guest: {first} {last} (age {age})")
        print(f"Room type: {room}")
        print(f"Number of nights: {nights}")
        print()
        
def edit_reservation(all_reservations):
    '''
    Edits an existing reservation.
    '''
    res_id = input("Enter the reservation ID you wish to edit: ")

    if res_id not in all_reservations:
        print("That reservation ID does not exist.")
        return all_reservations

    room = input("What type of room (single, double, king, suite)? ")
    while room not in ['single', 'double', 'king', 'suite']:
        room = input("Invalid room type. Please reenter: ")
        
    nights = int(input("How many nights? "))
    first, last, _, _, age = all_reservations[res_id]
    total = calculate_reservation_total(room, nights, age)
    print(f"The updated cost of this reservation is ${total:.2f}.")
    all_reservations[res_id] = [first, last, room, nights, age]

    return all_reservations

def delete_reservation(all_reservations):
    res_id = input("Enter the reservation ID to delete: ")

    if res_id not in all_reservations:
        print("That reservation ID does not exist.")
        return all_reservations

    del all_reservations[res_id]
    print("That reservation has been deleted.")

    return all_reservations

            
def save_reservations(all_reservations):
    '''
    Saves reservations to a file.
    '''
    try:
        file = open("reservations.txt", "w")

        for res_id in all_reservations:
            first, last, room, nights, age = all_reservations[res_id]
            file.write(f"{res_id} {first} {last} {room} {nights} {age}\n")

        file.close()
        print("Data saved successfully.")
    except:
        print("There was an error saving the data.")


def load_reservations():
    '''
    Loads reservations from a file.

    Returns:
    dict
    '''
    try:
        file = open("reservations.txt", "r")

        data = {}

        for line in file:
            parts = line.strip().split()

            res_id = parts[0]
            first = parts[1]
            last = parts[2]
            room = parts[3]
            nights = int(parts[4])
            age = int(parts[5])

            data[res_id] = [first, last, room, nights, age]

        file.close()
        print("Data loaded successfully.")
        return data

    except:
        print("There was an error loading the data.")
        return {}

def main():
    '''
    Runs the main program. Shows the menu, gets the user's choice, and runs the correct option until the user leaves.
    '''
    
    print("Welcome to the Python hotel reservation system!\n")
    
    all_reservations = {}
    while True:
   
        print_menu()
        choice = int(input("What is your selection? "))
        
        if choice == 1:
            all_reservations =  create_reservation(all_reservations)
            
        elif choice == 2:
            view_reservations(all_reservations)
            
        elif choice == 3:
            all_reservations = edit_reservation(all_reservations)
            
        elif choice == 4:
            all_reservations = delete_reservation(all_reservations)
            
        elif choice == 5:
            save_reservations(all_reservations)
            
        elif choice == 6:
            all_reservations = load_reservations()
            
        elif choice == 7:
            print('Now exiting program. Thanks for visiting!')
            break
        else:
            print('Invalid choice. Please try again.')
            print()
        

        



if __name__ == '__main__':
    main()
