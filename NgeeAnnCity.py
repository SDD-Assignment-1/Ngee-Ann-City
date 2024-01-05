import pickle
import random
import re
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

def place_building(game_data, buildplace,field):  
    vert_pos = t.index(buildplace[0].capitalize())
    if game_data['turn'] == 1:
        if field[int(vert_pos)][int(buildplace[1:])-1] == '':
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1
            orthoTiles = ['', '','','']
            adjacentTiles = ['','','','']
            connectedTiles = ['','','','']
            add_point(game_data, adjacentTiles, orthoTiles, connectedTiles)
        else:
            print("Another unit is in position")
    else:
        orthoTiles = getOrthoTiles(int(buildplace[1:])-1, vert_pos)
     
        if field[int(vert_pos)][int(buildplace[1:])-1] == '' and (orthoTiles[0] != "" or orthoTiles[1] != "" or orthoTiles[2] !="" or orthoTiles[3] !=""):
            field[int(vert_pos)][int(buildplace[1:]) - 1] = " " + buildings[game_data["building"]]["shortform"]
            game_data["coins"] -= 1
            game_data["turn"] += 1
           
            adjacentTiles = getAdjacentTiles(int(buildplace[1:])-1, vert_pos)
            connectedTiles = getAdjacentTiles(int(buildplace[1:])-1, vert_pos)
            add_point(game_data, adjacentTiles, orthoTiles, connectedTiles)
        
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


# add points for each specific building   
def add_point(game_data, adjacentTiles, orthoTiles, connectedTiles):
    if game_data["building"] == "Industry":
        numberOfPoints = 0
        count = 0
        numberOfCoins = 0
        game_data["points"]+=1
        numberOfPoints += 1
        
        print("You Have Received {} Point(s)!".format(numberOfPoints))

        # foreach R tile adjacent, add one coin.
        for i in adjacentTiles:       
            if adjacentTiles[count] == ' R':
                game_data["coins"]+=1
                numberOfCoins +=1
           
            count+=1
        if numberOfCoins !=0:
            print("You Have Received {} Coin(s)!".format(numberOfCoins))
    # foreach R, C, or O adjacent, add points.   
    elif game_data["building"] == "Residential":
        count = 0
        numberOfPoints = 0
        # foreach R tile adjacent, add one point.
        for i in adjacentTiles:       
            if adjacentTiles[count] == ' R' or adjacentTiles[count] == ' C':
                game_data["points"]+=1
                numberOfPoints += 1

            elif adjacentTiles[count] == ' O':
                game_data["points"]+= 2
                numberOfPoints +=2
            count+=1
        count1 = 0
        for i in orthoTiles:       
            if orthoTiles[count1] == ' I':
                game_data["points"]+=1
                numberOfPoints +=1
            count1+=1
        if numberOfPoints !=0:
            print("You Have Received {} Point(s)!".format(numberOfPoints))

    elif game_data["building"] == "Commercial":
        # Generate gold for each adjacent residence
        for i in adjacentTiles:
            if i == ' R':
                game_data["coins"] += 1
                print("1 Gold generated for Residence")
            elif i == ' C':
                game_data["points"] += 1  # Commercial building adjacent to another commercial building generates 1 point

    elif game_data["building"] == "Park":
    # Scores 1 point for each adjacent park.
     for tile in adjacentTiles:
        if tile == ' O':
            game_data["points"] += 1
            print("1 point for park")

    elif game_data["building"] == "Road":
        numberOfPoints = connectedTiles.count(' *')
        game_data["points"] += numberOfPoints
        if numberOfPoints != 0:
            print("You Have Received {} Point(s)!".format(numberOfPoints))
    

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
    print("Name: {}           Points: {}".format(game_data['name'], game_data['points']))
    buildoption = input("You have been given 2 buildings! Please select a building to place.\n 1. {} \n 2. {}\n ------ OR ------ \n 3. Stop playing \n Your choices are: ".format(choices[0], choices[1]))

    if buildoption == '1':
        buy_building(game_data, choices[0])
        while True:
            buildplace = input("Please select where to place building:")
            if is_valid_position(buildplace):
                #Placing the building
                place_building(game_data, buildplace, field)
                #validity = True
                break
            else:
                print("Invalid position. Please enter a valid position.")
                draw_field()
                choose_building(game_data, choices, validity)

    elif buildoption == '2':
        buy_building(game_data, choices[1])
        

    elif buildoption == '3':
        show_main_menu()

    else:
        print("Invalid option. Please enter a valid choice.")
        
        
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


# Save high scores
def save_high_scores():
    # Load existing high scores from a text file
    high_scores = load_high_scores()

    # Add the current game's score to the list
    current_score = {'name': game_data['name'], 'points': game_data['points']}
    high_scores.append(current_score)

    # Sort the high scores in descending order based on points
    high_scores.sort(key=lambda x: x['points'], reverse=True)

    # Save the top 10 high scores to a text file
    with open("high_scores.txt", "w") as save:
        save.write("Top 10 High Scores:\n")
        for rank, score in enumerate(high_scores[:10], start=1):
            save.write("Rank {}: {} - Points: {}\n".format(rank, score['name'], score['points']))

    print("High scores saved successfully.")

# Function to load existing high scores from a text file
def load_high_scores():
    high_scores = []
    highcount = 0

    try:
        with open("high_scores.txt", "r") as file:
            for line in file:
                # Assuming each line has the format "Rank X: Name - Points: Y"
                match = re.match(r"Rank (\d+): (.+) - Points: (\d+)", line)
                if match and highcount <11:
                    rank, name, points = match.groups()
                    high_scores.append({'name': name, 'points': int(points)})
                    highcount += 1

    except FileNotFoundError:
        pass  

    return high_scores

# Display high scores
def display_high_scores():
    # Load and display high scores
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
        print("Hello!")
        game_data["name"] = input("What's your name?")
        show_main_menu()
       
        i +=1
