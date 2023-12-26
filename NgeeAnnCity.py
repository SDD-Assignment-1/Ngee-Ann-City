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
 
def save_game(field, health, file_path):
    game_data['field'] = field
    game_data['health'] = health
    with open(file_path, 'wb') as file:
        pickle.dump(game_data, file)
def save_to_textfile(field, health, file_path):
    with open(file_path, 'w') as file:
        file.write("Field:\n")
        for row in field:
            file.write(' '.join(map(str, row)) + '\n')
        file.write("\nHealth:\n")
        for row in health:
            file.write(' '.join(map(str, row)) + '\n')
    print("Map saved to text file successfully!")
def load_from_textfile(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
 
    try:
        field_start = lines.index("Field:\n") + 1
        field_end = lines.index("\nHealth:\n")
        health_start = field_end + 1
 
        for row_idx in range(field_start, field_end):
            field[row_idx - field_start] = lines[row_idx].split()
 
        for row_idx in range(health_start, len(lines)):
            health[row_idx - health_start] = lines[row_idx].split()
 
        print("Map loaded from text file successfully!")
    except ValueError:
        print("Error loading map from text file.")
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
        adjacentTiles = getAdjacentiles(int(buildplace[1:])-1, vert_pos)
        print(adjacentTiles)
        if field[int(vert_pos)][int(buildplace[1:])-1] == '' and (adjacentTiles[0] != "" or adjacentTiles[1] != "" or adjacentTiles[2] !="" or adjacentTiles[3] !=""):
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1
            add_point(game_data, buildplace, vert_pos)
        
        else:
            print("Invalid position")


def getAdjacentiles(buildplace, vert_pos):
    adjacentTiles = []

    # Check the tile above
    if buildplace > 0:
    
        adjacentTiles.append(field[vert_pos][int(buildplace -1)])
        

    #Check the tile below
    if buildplace < len(field) - 1:
        
        adjacentTiles.append(field[vert_pos][int(buildplace +1)])
    
    #Check the tile to the left
    if vert_pos > 0:
        adjacentTiles.append(field[int(vert_pos -1)][buildplace])
    
    #Check the tile to the right
    if vert_pos < len(field[0]) - 1:
        adjacentTiles.append(field[int(vert_pos +1)][buildplace])

    if len(adjacentTiles) < 4:
        adjacentTiles.append("")

    return adjacentTiles

    
def add_point(game_data, buildplace, vert_pos):
    if game_data["building"] == "Industry":
        game_data["points"]+=1
        if field[int(vert_pos)][int(buildplace[1:])-1] == ' R': 
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
        text_file_path = 'saved_map.txt'
        save_to_textfile(field, health, text_file_path)
        print("Game saved. Thank you for playing Ngee Ann City. Goodbye!")
        exit()  # Exit the program after saving
 
    else:
        print("Invalid option. Please enter a valid choice.")

# save high scores
def save_high_scores():
    # Save high scores to a text file
    savefile = open("high_scores.txt", "w")

    player_name = game_data['name']
    points = game_data['points']

    savefile.write("Top 10 High Scores:\n")
    savefile.write(f"Rank 1: {player_name} - Points: {points}\n")

    savefile.close()
    

def display_high_scores():
    # Display the top 10 high scores from high_scores.txt
    savefile = open("high_scores.txt", "w")
    try:
        with open(savefile, "r") as file:
            print(savefile.read())
    except FileNotFoundError:
        print("Unable to load file.")


def show_main_menu():
    print()
    print("----------------")
    print("| Ngee Ann City |")
    print("----------------")
    print("Build a prosperous city!")
    print()

    print("Please select an option \n\
    1. Start New Game\n\
    2. Load Saved Game\n\
    3. Display High Scores\n\
    4. Save and exit Game")
    option = input("Enter your choice: ")
    while True:
        if option == '1':
            
            draw_field()
            choose_building(game_data)

        elif option == '2':
            '''# Replace 'file_path' with the actual path from where you want to load the text file
            text_file_path = 'saved_map.txt'
            load_from_textfile(text_file_path)
            print("Map loaded from text file successfully!")
            # Continue with the loaded game
            draw_field()
            choose_building(game_data)'''
            print("This feature will be available in the next update.")
                        
        elif option == '3':
            display_high_scores()

        elif option == '4':
            # Replace 'file_path' with the actual path where you want to save the text file
            text_file_path = 'saved_map.txt'
            save_high_scores()
            save_to_textfile(field, health, text_file_path)
            break

        else:
            print("Invalid option. Please enter a valid choice.")
            break

 

 
# main game
i=0
while True:
    if i == 0:
        show_main_menu()
        i +=1
    
