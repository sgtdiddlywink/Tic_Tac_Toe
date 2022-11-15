# Import Statements.
import random

game_winning_conditions = [
    {"A1": "X", "A2": "X", "A3": "X", "B1": " ", "B2": " ", "B3": " ", "C1": " ", "C2": " ", "C3": " "},
    {"A1": " ", "A2": " ", "A3": " ", "B1": "X", "B2": "X", "B3": "X", "C1": " ", "C2": " ", "C3": " "},
    {"A1": " ", "A2": " ", "A3": " ", "B1": " ", "B2": " ", "B3": " ", "C1": "X", "C2": "X", "C3": "X"},
    {"A1": "X", "A2": " ", "A3": " ", "B1": " ", "B2": "X", "B3": " ", "C1": " ", "C2": " ", "C3": "X"},
    {"A1": " ", "A2": " ", "A3": "X", "B1": " ", "B2": "X", "B3": " ", "C1": "X", "C2": " ", "C3": " "},
    {"A1": "X", "A2": " ", "A3": " ", "B1": "X", "B2": " ", "B3": " ", "C1": "X", "C2": " ", "C3": " "},
    {"A1": " ", "A2": "X", "A3": " ", "B1": " ", "B2": "X", "B3": " ", "C1": " ", "C2": "X", "C3": " "},
    {"A1": " ", "A2": " ", "A3": "X", "B1": " ", "B2": " ", "B3": "X", "C1": " ", "C2": " ", "C3": "X"},
    {"A1": "O", "A2": "O", "A3": "O", "B1": " ", "B2": " ", "B3": " ", "C1": " ", "C2": " ", "C3": " "},
    {"A1": " ", "A2": " ", "A3": " ", "B1": "O", "B2": "O", "B3": "O", "C1": " ", "C2": " ", "C3": " "},
    {"A1": " ", "A2": " ", "A3": " ", "B1": " ", "B2": " ", "B3": " ", "C1": "O", "C2": "O", "C3": "O"},
    {"A1": "O", "A2": " ", "A3": " ", "B1": " ", "B2": "O", "B3": " ", "C1": " ", "C2": " ", "C3": "O"},
    {"A1": " ", "A2": " ", "A3": "O", "B1": " ", "B2": "O", "B3": " ", "C1": "O", "C2": " ", "C3": " "},
    {"A1": "O", "A2": " ", "A3": " ", "B1": "O", "B2": " ", "B3": " ", "C1": "O", "C2": " ", "C3": " "},
    {"A1": " ", "A2": "O", "A3": " ", "B1": " ", "B2": "O", "B3": " ", "C1": " ", "C2": "O", "C3": " "},
    {"A1": " ", "A2": " ", "A3": "O", "B1": " ", "B2": " ", "B3": "O", "C1": " ", "C2": " ", "C3": "O"}
]
# Initial tables of grid layout.
table_dict = {"A1": " ", "A2": " ", "A3": " ", "B1": " ", "B2": " ", "B3": " ", "C1": " ", "C2": " ", "C3": " "}
table_1 = {"A1": " ", "A2": " ", "A3": " ", "B1": " ", "B2": " ", "B3": " ", "C1": " ", "C2": " ", "C3": " "}
table_2 = {"A1": " ", "A2": " ", "A3": " ", "B1": " ", "B2": " ", "B3": " ", "C1": " ", "C2": " ", "C3": " "}
choice_list = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]


# Function for displaying the grid layout and shortening the code.
def grid_layout(table):
    # Board Layout
    print(f"     1   2   3  ")
    print(f"   -------------")
    print(f" A | {table_dict['A1']} | {table_dict['A2']} | {table_dict['A3']} |")
    print(f"   -------------")
    print(f" B | {table_dict['B1']} | {table_dict['B2']} | {table_dict['B3']} |")
    print(f"   -------------")
    print(f" C | {table_dict['C1']} | {table_dict['C2']} | {table_dict['C3']} |")
    print(f"   -------------")


# Ask the player for their name.
# Included while statement because further down the code if the player used "AI" as their name it wouldn't work.
variable = True
while variable:
    player_1_name = input("What is your name? ")
    if player_1_name == "AI":
        print("Invalid player name. Try again.")
    else:
        variable = False

# Ask the player whether they want to play against another human or against the machine.
# While statement to ensure that user puts in the correct response.
variable = True
while variable:
    game_choice = input("Do you want to play against another person or the AI? Type '1' for Human or '2' for AI: ")
    if game_choice == "1":
        player_2_name = input("What is Player 2's name? ")
        variable = False
    elif game_choice == "2":
        print("You have chosen to play against the most advance AI in the world. Good Luck!")
        variable = False
    else:
        print("You have chosen an invalid response. Try again.")

# Explain the rules of the game.
print(f"\nWelcome to Extreme Python Tic Tac Toe!\nSee the board layout below:")
grid_layout(table=table_dict)
print("The game will choose a player at random to start.\nWhen it is your turn, enter the space you want to place "
      "your mark in starting with the row.\nFor example: A1, B2, C3, etc.")
print("You can only place your mark in a space that has no mark in it already.\nTry to get three of your marks in a "
      "line")
print("GLHF!\n")

# Choose first player at random.
if game_choice == "1":
    players = [player_1_name, player_2_name]
    first_player = random.choice(players)
    if first_player == player_1_name:
        second_player = player_2_name
    else:
        second_player = player_1_name
    print(f"{first_player} will go first!")
else:
    players = [player_1_name, "AI"]
    first_player = random.choice(players)
    if first_player == player_1_name:
        second_player = "AI"
    else:
        second_player = player_1_name
    print(f"{first_player} will go first!")

# Set game start.
game_start = True

# Start the game for Game Option 1.
if game_choice == "1":
    while game_start:
        variable = True
        while variable:
            choice = input(f"{first_player} choose an empty spot for your mark: ")
            if choice_list.count(choice) > 0:
                if table_dict[choice.upper()] == " ":
                    table_dict[choice.upper()] = "X"
                    table_1[choice.upper()] = "X"
                    choice_list.remove(choice.upper())
                    variable = False
                else:
                    print("There is already a mark in that location. Try again.")
            else:
                print("Incorrect response. Try again.")

        grid_layout(table_dict)

        # Check to see if anyone has won.
        for n in game_winning_conditions:
            if table_1 == n:
                print(f"{first_player} Wins! Congratulations!")
                game_start = False
                exit()
            elif choice_list == []:
                print("Draw Game. Thanks for Playing!")
                game_start = False
                exit()

        # Let second player do their turn.
        variable = True
        while variable:
            choice = input(f"{second_player} choose an empty spot for your mark: ")
            if choice_list.count(choice) > 0:
                if table_dict[choice.upper()] == " ":
                    table_dict[choice.upper()] = "O"
                    table_2[choice.upper()] = "O"
                    choice_list.remove(choice.upper())
                    variable = False
                else:
                    print("There is already a mark in that location. Try again.")
            else:
                print("Incorrect response. Try again.")

        grid_layout(table_dict)

        # Check to see if anyone has won.
        for n in game_winning_conditions:
            if table_2 == n:
                print(f"{second_player} Wins! Congratulations!")
                game_start = False
                exit()
            elif choice_list == []:
                print("Draw Game. Thanks for Playing!")
                game_start = False
                exit()

# Start the game for Game Option 2.
else:
    while game_start:
        if first_player == "AI":
            ai_choice = random.choice(choice_list)
            print(f"AI chooses: {ai_choice}")
            table_dict[ai_choice] = "X"
            table_1[ai_choice] = "X"
            choice_list.remove(ai_choice)
            grid_layout(table_dict)

            # Check to see if anyone has won.
            for n in game_winning_conditions:
                if table_1 == n:
                    print(f"The AI Wins!")
                    game_start = False
                    exit()
                elif choice_list == []:
                    print("Draw Game. Thanks for Playing!")
                    game_start = False
                    exit()

            # Let second player do their turn.
            variable = True
            while variable:
                choice = input(f"{second_player} choose an empty spot for your mark: ")
                if choice_list.count(choice) > 0:
                    if table_dict[choice.upper()] == " ":
                        table_dict[choice.upper()] = "O"
                        table_2[choice.upper()] = "O"
                        choice_list.remove(choice.upper())
                        variable = False
                    else:
                        print("There is already a mark in that location. Try again.")
                else:
                    print("Incorrect response. Try again.")

            grid_layout(table_dict)

            # Check to see if anyone has won.
            for n in game_winning_conditions:
                if table_2 == n:
                    print(f"{second_player} Wins! Congratulations!")
                    game_start = False
                    exit()
                elif choice_list == []:
                    print("Draw Game. Thanks for Playing!")
                    game_start = False
                    exit()
        else:
            variable = True
            while variable:
                choice = input(f"{first_player} choose an empty spot for your mark: ")
                if choice_list.count(choice) > 0:
                    if table_dict[choice.upper()] == " ":
                        table_dict[choice.upper()] = "X"
                        table_1[choice.upper()] = "X"
                        choice_list.remove(choice.upper())
                        variable = False
                    else:
                        print("There is already a mark in that location. Try again.")
                else:
                    print("Incorrect response. Try again.")

            grid_layout(table_dict)

            # Check to see if anyone has won.
            for n in game_winning_conditions:
                if table_1 == n:
                    print(f"{first_player} Wins! Congratulations!")
                    game_start = False
                    exit()
                elif choice_list == []:
                    print("Draw Game. Thanks for Playing!")
                    game_start = False
                    exit()

            # Let the AI go next.
            ai_choice = random.choice(choice_list)
            print(f"AI chooses: {ai_choice}")
            table_dict[ai_choice] = "O"
            table_2[ai_choice] = "O"
            choice_list.remove(ai_choice)
            grid_layout(table_dict)

            # Check to see if anyone has won.
            for n in game_winning_conditions:
                if table_2 == n:
                    print(f"The AI Wins!")
                    game_start = False
                    exit()
                elif choice_list == []:
                    print("Draw Game. Thanks for Playing!")
                    game_start = False
                    exit()
