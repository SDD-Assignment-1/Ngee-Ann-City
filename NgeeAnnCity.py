import pickle
import random
 
building_list = ['Residential', 'Commercial', 'Industry', 'Park', 'Road']
 
# Initialize game data
game_data = {
            "coins":0,
            "points":0,
             "turn": 0,
             "building": '',}
 
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
            print("")
 
 
def draw_field():
    print("   1     2     3     4     5     6      7     8     9    10     11    12    13    14    15    16    17    18    19    20")
    num_row = len(field)
    num_column = len(field[0])
    print(" ", end="")
    for i in range(num_column):
        print("+-----", end="")
    print('+')
    for row in range(num_row):
        print(t[row], end="")
        for column in field[row]:
            print("|{:5}".format(column), end="")
        print("|")
        print(" ", end='')
        for column1 in health[row]:
            print("|{:5}".format(column1), end="")
        print("|")
        print(" ", end='')
        for i in range(num_column):
            print("+-----", end="")
        print("+")

def buy_building(game_data, choice):
    game_data['coin']-=1
    game_data['turn']+=1
    game_data['building'] = choice
def place_building(game_data, buildplace,field, health):
    int(vert_pos) 
    vert_pos = t.index(buildplace[0])

#randomise building choices
def choose_building(game_data):

    
    choice1 = building_list[random.randint(0,4)]
    choice2 = building_list[random.randint(0,4)]
    # ensure the choices dont repeat.
    while choice2 == choice1:
        choice2 = building_list[random.randint(0,4)]
    print("Turn: {}".format(game_data['turn']))
    buildoption = input("Please select a building to place. Your choices are:\n 1. {} \n 2. {}\n".format (choice1, choice2))
    if buildoption == 1:
        buy_building(game_data, choice1)
    elif buildoption == 2:
        buy_building(game_data, choice2)
    buildplace = input("PLease select where to place building.")

        

def show_main_menu():
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
            break

        elif option == '2':
            # Replace 'file_path' with the actual path from where you want to lo1ad the text file
            text_file_path = 'saved_map.txt'
            load_from_textfile(text_file_path)
            print("Map loaded from text file successfully!")
            draw_field()
            break
    
        elif option == '4':
            # Replace 'file_path' with the actual path where you want to save the text file
            text_file_path = 'saved_map.txt'
            save_to_textfile(field, health, text_file_path)
            break
    
        else:
            print("Invalid option. Please enter a valid choice.")

 
print("----------------")
print("| Ngee Ann City |")
print("----------------")
print("Build a prosperous city!")
print()
 
# main game
i=0
while True:
    if i == 0:
        show_main_menu()
        i +=1
    
