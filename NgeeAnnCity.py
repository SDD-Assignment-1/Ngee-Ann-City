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
            "name":'',
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
    
def is_adjacent_to_residence(buildplace, vert_pos):
    orthoTiles = getOrthoTiles(int(buildplace[1:])-1, vert_pos)
    return ' R' in orthoTiles

def place_building(game_data, buildplace, field):
    vert_pos = t.index(buildplace[0].capitalize())
    if game_data['turn'] == 1:
        if field[int(vert_pos)][int(buildplace[1:])-1] == '':
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1
            orthoTiles = ['', '', '', '']
            adjacentTiles = ['', '', '', '']
            connectedTiles = ['', '', '', '']
            add_point(game_data, adjacentTiles, connectedTiles, buildplace, vert_pos)
        else:
            print("Another unit is in position")
    else:
        orthoTiles = getOrthoTiles(int(buildplace[1:])-1, vert_pos)

        if field[int(vert_pos)][int(buildplace[1:])-1] == '' and (orthoTiles[0] != "" or orthoTiles[1] != "" or orthoTiles[2] !="" or orthoTiles[3] !=""):
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1

            adjacentTiles = getAdjacentTiles(int(buildplace[1:])-1, vert_pos)
            connectedTiles = getConnectedTiles(field, vert_pos, int(buildplace[1:])-1)
            add_point(game_data, adjacentTiles, orthoTiles, connectedTiles, buildplace, vert_pos)
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

def getConnectedTiles(field, vert_pos, buildplace):
    connectedTiles = []

    # Check the tile to the left
    if vert_pos > 0 and field[vert_pos - 1][int(buildplace) - 1] != '':
        connectedTiles.append(field[vert_pos - 1][int(buildplace) - 1])

    # Check the tile to the right
    if vert_pos < len(field) - 1 and field[vert_pos + 1][int(buildplace) - 1] != '':
        connectedTiles.append(field[vert_pos + 1][int(buildplace) - 1])

    while len(connectedTiles) < 2:
        connectedTiles.append("")

    return connectedTiles

def getNextTo(buildplace, vert_pos):
    nextTiles = []
    
    #Check the tile to the left
    if vert_pos > 0:
        nextTiles.append(field[int(vert_pos -1)][buildplace])
    
    #Check the tile to the right
    if vert_pos < len(field[0]) - 1:
        nextTiles.append(field[int(vert_pos +1)][buildplace])

    #Check the tile to 
    while len(nextTiles) < 2:
        nextTiles.append("")


    return nextTiles

# Modify this function to generate gold for residences adjacent to commercial buildings
def add_point(game_data, adjacentTiles, connectedTiles, buildplace, vert_pos):
    if game_data["building"] == "Industry":
        numberOfPoints = 0
        count = 0
        numberOfCoins = 0
        game_data["points"] += 1
        numberOfPoints += 1

        print("You Have Received {} Point(s)!".format(numberOfPoints))

        # foreach R tile adjacent, add one coin.
        for i in adjacentTiles:
            if adjacentTiles[count] == ' R':
                game_data["coins"] += 1
                numberOfCoins += 1

            count += 1
        if numberOfCoins != 0:
            print("You Have Received {} Coin(s)!".format(numberOfCoins))
    # foreach R, C, or O adjacent, add points.
   
        
    elif game_data["building"] == "Residential":
        nextTiles = []
        nextTiles = getNextTo(int(buildplace[1:]), vert_pos)
        count = 0
        numberOfPoints = 0
        # foreach R tile adjacent, add one point.
        for i in adjacentTiles:
            if adjacentTiles[count] == ' R' or (adjacentTiles[count] == ' C' and is_adjacent_to_residence(buildplace, vert_pos)):
                game_data["points"] += 1
                numberOfPoints += 1

            elif adjacentTiles[count] == ' O':
                game_data["points"] += 2
                numberOfPoints += 2
            count += 1
        count1 = 0
        for i in nextTiles:
            if nextTiles[count1] == ' I':
                game_data["points"] += 1
                numberOfPoints += 1
                if numberOfPoints > 0 or numberOfPoints < 1:
                    break
            count1 += 1
        if numberOfPoints != 0:
            print("You Have Received {} Point(s)!".format(numberOfPoints))

    elif game_data["building"] == "Commercial":
        numberOfCoins = 0
        # Generate gold for each adjacent residence
        for i in adjacentTiles:
            if i == ' R':
                game_data["coins"] += 1
                print("1 gold generated for residence")
        

    elif game_data["building"] == "Park":
        # Scores 1 point for each adjacent building.
        numberOfPoints = 0
        for tile in adjacentTiles:
            if tile in [' R', ' C', ' I']:
                game_data["points"] += 1
            if numberOfPoints != 0:
                print("You Have Received {} Point(s)!".format(numberOfPoints))

    elif game_data["building"] == "Road":
        numberOfPoints = connectedTiles.count(' *')
        game_data["points"] += numberOfPoints
        if numberOfPoints != 0:
            print("You Have Received {} Point(s)!".format(numberOfPoints))

# randomise building choices
recentChoices = [building_list[random.randint(0,2)], building_list[random.randint(2,5)]]
def random_building():
    global recentChoices
    choice1 = building_list[random.randint(0,4)]
    choice2 = building_list[random.randint(0,4)]
    # ensure the choices dont repeat.
    while choice2 == choice1:
        choice2 = building_list[random.randint(0,4)]
    recentChoices = [choice1, choice2]

def choose_building(game_data, validity):
    if validity == True:
        random_building()
    print()
    print("Turn: {}          Coins: {}".format(game_data['turn'], game_data['coins']))
    print("Name: {}           Points: {}".format(game_data['name'], game_data['points']))
    buildoption = input("You have been given 2 buildings! Please select a building to place.\n 1. {} \n 2. {}\n ------ OR ------ \n 3. Stop playing \n Your choices are: ".format(recentChoices[0], recentChoices[1]))
    if buildoption == '1':
        buy_building(game_data, recentChoices[0])
        buildplace = input("Please select where to place building: ")
        while not is_valid_position(buildplace):
            print("Invalid position. Please enter a valid position within the 20x20 grid.")
            buildplace = input("Please select where to place building: ")
        # placing the building
        place_building(game_data, buildplace, field)
        validity = True

    elif buildoption == '2':
        buy_building(game_data, recentChoices[1])
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

# save high scores
def save_high_scores():
    # Save high scores to a text file
    name = game_data['name']
    points = game_data['points']

    with open("high_scores.txt", "w") as save:
        save.write("Top 10 High Scores:\n")
        save.write("Rank 1: {} - Points: {}\n".format(game_data['name'], game_data['points']))

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
        if game_data["coins"] !=0:
            validity = choose_building(game_data, validity)
        else:
            print("--------------------------------------------")
            print("|   You Have Run Out Of Coins, Game Over!  |")
            print("--------------------------------------------")
            print("Turn: {}          ".format(game_data['turn']))
            print("Name: {}           Final score: {}".format(game_data['name'], game_data['points']))
            print()
            exit()

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
        print("Hello!")
        game_data['name'] = input("What's your name? ")
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
    
