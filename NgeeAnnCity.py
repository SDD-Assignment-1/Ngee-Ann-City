import pickle

building_list = ['Residential', 'Commercial', 'Industry', 'Park', 'Road']

# Initialize game data
game_data = {
    'turn':0,
    'coins':16,
    'points': 0,
}

t = ["A", "B", "C", 'D', "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]

field = [['' for _ in range(20)] for _ in range(20)]
health = [['' for _ in range(20)] for _ in range(20)]

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
            print("Error: Required markers not found in the text file. Unable to load the map.")


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

print("----------------")
print("| Ngee Ann City |")
print("----------------")
print("Build a prosperous city!")
print()

while True:
    print("Please select an option \n\
    1. Start New Game\n\
    2. Load Saved Game\n\
    3. Display High Scores\n\
    4. Save and exit Game")
    option = input("Enter your choice: ")

    if option == '1':
        draw_field()

    elif option == '2':
        # Replace 'file_path' with the actual path from where you want to load the text file
        text_file_path = 'saved_map.txt'
        load_from_textfile(text_file_path)
        print("Map loaded from text file successfully!")
        draw_field()

    elif option == '4':
        # Replace 'file_path' with the actual path where you want to save the text file
        text_file_path = 'saved_map.txt'
        save_to_textfile(field, health, text_file_path)
        print("Map saved to text file successfully!")
        break

    elif option == '0':
        print("Exiting the program.")
        break

    else:
        print("Invalid option. Please enter a valid choice.")

    
