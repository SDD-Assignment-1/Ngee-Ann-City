import pickle
import random
 
building_list = ['Residential', 'Commercial', 'Industry', 'Park', 'Road']

buildings =  {'Residential' : {
            'shortform': 'R'
            },
            'Commercial' : {
            'shortform': 'C'
            },
            'Industry' : {
            'shortform': 'I'
            },
            'Park' : {
            'shortform': 'O'
            },
            'Road' : {
            'shortform': '*'
            }
            }
 
# Initialize game data
game_data = {
            "coins":16,
            "points":0,
             "turn": 1,
             "building": ''}
 
t = ["A", "B", "C", 'D', "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
 
field = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],  #To print out all the units' name
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ]
    
         
         ]
health = [['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],  #To print out all the units' name
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ],
    ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '' ]]
 
def save_game():
    with open('save_map.txt','wb') as save:
        pickle.dump([field,health,game_data], save)
    save.close()
    print("Game saved.")


def load_game():
    global field, game_data, health
    with open('save_map.txt','rb') as save:     #Load the Game Variable 
        field, health, game_data = pickle.load(save)
    save.close()

    return
 
 
def draw_field():
    print("   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20")
    num_row = len(field)
    num_column = len(field[0])
    print(" ", end="")
    for i in range(num_column):
        print("+---", end="")
    print('+')
    for row in range(num_row):
        print(t[row], end="")
        for column in field[row]:
            print("|{:3}".format(column), end="")
        print("|")
        print(" ", end='')
        
        for i in range(num_column):
            print("+---", end="")
        print("+")

def buy_building(game_data, choice):

    game_data["building"] = choice
def place_building(game_data, buildplace,field):
    
    vert_pos = t.index(buildplace[0].capitalize())
    if game_data['turn'] == 1:
        if field[int(vert_pos)][int(buildplace[1:])-1] == '':
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1
            add_point(game_data, buildplace, vert_pos)
        else:
            print("Another unit is in position")
    else:
        if field[int(vert_pos)][int(buildplace[1:])-1] == '':
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1
            add_point(game_data, buildplace, vert_pos)
        else:
            print("Invalid position")



def add_point(game_data, buildplace, vert_pos):
    if game_data["building"] == "Industry":
        game_data["points"]+=1
        if field[int(vert_pos)][int(buildplace[1:]) - 1] == " R":
            game_data["coins"]+=1
        
    elif game_data["building"] == "Residential":
        game_data["points"]+=1

    elif game_data["building"] == "Commercial":
        game_data["points"]+=1

    elif game_data["building"] == "Park":
        game_data["points"]+=1

    elif game_data["building"] == "Road":
        game_data["points"]+=1
    
    #building_list = ['Residential', 'Commercial', 'Industry', 'Park', 'Road']

# randomise building choices
def choose_building(game_data):

    
    choice1 = building_list[random.randint(0,4)]
    choice2 = building_list[random.randint(0,4)]
    # ensure the choices dont repeat.
    while choice2 == choice1:
        choice2 = building_list[random.randint(0,4)]
    print()
    print("Turn: {}          Coins: {}".format(game_data['turn'],game_data['coins']))
    print("Name:            Points: {}".format(game_data['points']))
    buildoption = input("You have been given 2 buildings! Please select a building to place.\n 1. {} \n 2. {}\n ------ OR ------ \n 3. Stop Playing \n Your choices are: ".format (choice1, choice2))
    if buildoption == '1':
        buy_building(game_data, choice1)
        buildplace = input("Please select where to place building: ")
        # placing the building
        place_building(game_data, buildplace, field)

    elif buildoption == '2':
        buy_building(game_data, choice2)
        buildplace = input("Please select where to place building: ")
        # placing the building
        place_building(game_data, buildplace, field)

    elif buildoption == '3':
        # Save the game before stopping
        save_high_scores()
        save_game()
        print("Game saved. Thank you for playing Ngee Ann City. Goodbye!")
        exit()  # Exit the program after saving
 
 
    else:
        print("Invalid option. Please enter a valid choice.")

# save high scores
def save_high_scores():
    # Save high scores to a text file
    #player_name = game_data['name']
    points = game_data['points']

    with open("high_scores.txt", "w") as save:
        save.write("Top 10 High Scores:\n")
        save.write(f"Rank 1: User - Points: {points}\n")

    print("High scores saved successfully.")

    

def display_high_scores():
    try:
        with open("high_scores.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("Unable to load file or no high scores available.")

def game_start():
    while True:
        draw_field()
        choose_building(game_data)

def show_main_menu():
    print()
    print("----------------")
    print("| Ngee Ann City |")
    print("----------------")
    print("Build a prosperous city!")
    print()

    print("Please select an option:\n\
    1. Start New Game\n\
    2. Load Saved Game\n\
    3. Display High Scores\n\
    4. Save and exit Game")
    
    option = input("Enter your choice: ")

    if option == '1':
        game_start()

    elif option == '2':
        try:
            load_game()
            print("Game loaded successfully.")
            game_start()
        except FileNotFoundError:
            print("No saved game found. Starting a new game.")
            game_start()

    elif option == '3':
        display_high_scores()

    elif option == '4':
        # Save high scores and the game before exiting
        save_high_scores()
        save_game()
        print("Game saved. Thank you for playing Ngee Ann City. Goodbye!")
        

    else:
        print("Invalid option. Please enter a valid choice.")



# main game
i=0
while True:
    if i == 0:
        show_main_menu()
        i +=1
    
