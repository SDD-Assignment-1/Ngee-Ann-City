import pickle
import random
building_list = ['Residential', 'Commercial', 'Industry', 'Park', 'Road']
validity = False
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

def is_valid_position(buildplace):
    # Check if the input position is within the valid range
    if len(buildplace) == 2 and buildplace[0].capitalize() in t and 1 <= int(buildplace[1:]) <= 20:
        return True
    else:
        return False

def place_building(game_data, buildplace,field):
    
    vert_pos = t.index(buildplace[0].capitalize())
    if game_data['turn'] == 1:
        if field[int(vert_pos)][int(buildplace[1:])-1] == '':
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1
            orthoTiles = ['', '','','']
            adjacentTiles = ['','','','']
            add_point(game_data, adjacentTiles, orthoTiles)
        else:
            print("Another unit is in position")
    else:
        orthoTiles = getOrthoTiles(int(buildplace[1:])-1, vert_pos)
     
        if field[int(vert_pos)][int(buildplace[1:])-1] == '' and (orthoTiles[0] != "" or orthoTiles[1] != "" or orthoTiles[2] !="" or orthoTiles[3] !=""):
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1
           
            adjacentTiles = getAdjacentTiles(int(buildplace[1:])-1, vert_pos)
            add_point(game_data, adjacentTiles, orthoTiles)
        
        else:
                print("-------------------")
                print("| INVALID POSITION |")
                print("-------------------")


def getOrthoTiles(buildplace, vert_pos):
    orthoTiles = []

    # Check the tile above
    if buildplace > 0:
        orthoTiles.append(field[vert_pos][int(buildplace -1)])
        

    #Check the tile below
    if buildplace < len(field) - 1:
        orthoTiles.append(field[vert_pos][int(buildplace +1)])
    
    #Check the tile to the left
    if vert_pos > 0:
        orthoTiles.append(field[int(vert_pos -1)][buildplace])
    
    #Check the tile to the right
    if vert_pos < len(field[0]) - 1:
        orthoTiles.append(field[int(vert_pos +1)][buildplace])

    #Check the tile to 
    while len(orthoTiles) < 4:
        orthoTiles.append("")


    return orthoTiles

# game over
# def gameOver():
    
# get value of adjacent tiles
def getAdjacentTiles(buildplace, vert_pos):
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

    #Check the tile to top left
    if buildplace > 0 and vert_pos > 0:
        adjacentTiles.append(field[vert_pos-1][int(buildplace -1)])
        
    #Check the tile to top-right
    if buildplace > 0 and vert_pos < len(field[0]) - 1:
       adjacentTiles.append(field[int(vert_pos +1)][buildplace -1])

    # Check the tile to bottom-left
    if buildplace < (len(field[0]) - 1) and vert_pos > 0:
        adjacentTiles.append(field[vert_pos-1][int(buildplace +1)])

    # Check the tile to bottom-right
    if buildplace < (len(field[0]) - 1) and vert_pos < (len(field[0]) - 1):
        adjacentTiles.append(field[vert_pos+1][int(buildplace +1)])

    # if len(list) less than 4, must add 
    while len(adjacentTiles) < 7:
        adjacentTiles.append("")

    
    
    return adjacentTiles


# add points for each specific building   
def add_point(game_data, adjacentTiles, orthoTiles):
    if game_data["building"] == "Industry":
        game_data["points"]+=1
        
       
        count = 0
        # foreach R tile adjacent, add one coin.
        for i in adjacentTiles:       
            if adjacentTiles[count] == ' R':
                game_data["coins"]+=1
            count+=1

    # foreach R, C, or O adjacent, add points.   
    elif game_data["building"] == "Residential":
        count = 0
        # foreach R tile adjacent, add one point.
        for i in adjacentTiles:       
            if adjacentTiles[count] == ' R' or adjacentTiles[count] == ' C':
                game_data["points"]+=1

            elif adjacentTiles[count] == ' O':
                game_data["points"]+=2
            count+=1
        count1 = 0
        for i in orthoTiles:       
            if orthoTiles[count1] == ' I':
                game_data["points"]+=1
            count1+=1

    #elif game_data["building"] == "Commercial":
        #Input your code here (Nithish)
    #elif game_data["building"] == "Park":
        #Input your code here (Xin Yang)

    #elif game_data["building"] == "Road":
        #Input your code here (Shawn)
    

# randomise building choices
def random_building():
        choice1 = building_list[random.randint(0,4)]
        choice2 = building_list[random.randint(0,4)]
        # ensure the choices dont repeat.
        while choice2 == choice1:
            choice2 = building_list[random.randint(0,4)]
        choices = [choice1, choice2]

        return choices
    
    
choices = random_building()
def choose_building(game_data, choices, validity):
    
    if validity == True:
        choices = random_building()
    print()
    print("Turn: {}          Coins: {}".format(game_data['turn'], game_data['coins']))
    print("Name:            Points: {}".format(game_data['points']))
    buildoption = input("You have been given 2 buildings! Please select a building to place.\n 1. {} \n 2. {}\n ------ OR ------ \n 3. Stop playing \n Your choices are: ".format(choices[0], choices[1]))
    if buildoption == '1':
        buy_building(game_data, choices[0])
        buildplace = input("Please select where to place building: ")
        while not is_valid_position(buildplace):
            print("Invalid position. Please enter a valid position within the 20x20 grid.")
            buildplace = input("Please select where to place building: ")
        # placing the building
        place_building(game_data, buildplace, field)
        validity = True

    elif buildoption == '2':
        buy_building(game_data, choices[1])
        buildplace = input("Please select where to place building: ")
        while not is_valid_position(buildplace):
            print("Invalid position. Please enter a valid position within the 20x20 grid.")
            buildplace = input("Please select where to place building: ")
        # placing the building
        place_building(game_data, buildplace, field)
        validity = True

    elif buildoption == '3':
        show_main_menu()
    else:
        print("Invalid option. Please enter a valid choice.")
        validity = False
    return validity
# Function to calculate Park score based on adjacent parks
def calculate_park_score(board, row, col):
    adjacent_parks = count_adjacent_buildings(board, row, col, "Park")
    return adjacent_parks * 1  # Park score is 1 point per adjacent park

# Function to count adjacent buildings of a specific type
def count_adjacent_buildings(board, row, col, building_type):
    count = 0
    for i in range(max(0, row - 1), min(len(board), row + 2)):
        for j in range(max(0, col - 1), min(len(board[0]), col + 2)):
            if i != row or j != col:  # Exclude the current position
                if board[i][j].endswith(building_type):
                    count += 1
    return count


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
    validity = False
    
    while True:
        draw_field()
        # this might be the problem ?????
        validity = choose_building(game_data,choices, validity)

def show_main_menu():
    print()
    print("----------------")
    print("| Ngee Ann City |")
    print("----------------")
    print("Build a prosperous city!")
    print()
    print("  /◥████◣")
    print("  │田│▓ ∩ │◥███◣")
    print("  /◥◣ ◥████◣田∩田")
    print("  │╱◥█◣║∩∩∩ ║◥███◣")
    print("  │∩│ ▓ ║∩田│║ ▓田▓")

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
        show_main_menu()


    elif option == '4':
        # Save high scores and the game before exiting
        save_high_scores()
        save_game()
        print("Game saved. Thank you for playing Ngee Ann City. Goodbye!")
        raise SystemExit
        

    else:
        print("Invalid option. Please enter a valid choice.")
        show_main_menu()



# main game
i=0
while True:
    if i == 0:
        show_main_menu()
        i +=1
    
