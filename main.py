from time import sleep
import re

messages = {
    "welcome" : "Welcome to the Floating Fortress \n" +
                "-------------------------------- \n",
    "instructions_1" : "1. The hidden location of the warships should be determined in each \n" +
                       "of the two player's identical grids, while keeping in mind that they cannot join or overlap.",
    "instructions_2" : "2. Each ship is depicted as a line of m squares, where m indicates \n" +
                       "the volume of the ship.",
    "instructions_3" : "3. Each player needs to select a location on the opponent's grid to launch an attack against.",
    "instructions_4" : "4. If the attack hits an opponent's ship, the opponent's ship sinks.",
    "instructions_5" : "5. The player who manages to sink all of their opponent's ships, wins!",
    "player_1"       : "What's player's 1 name? ",
    "player_2"       : "What's player's 2 name? ",
    "size"           : "How big would you like your board to be? (size >= 1 and size <= 20): ",
    "ships"          : "How many ships would you like? (ships >= 1 and ships <= 5): ",
    "set_piece"      : "Where would you like to set your ship? \n" +
                       "Use the coordinates on your map to set your ship. \n" +
                       "(row,column), like : '1,3' or '4,2' \n",
    "start_game"     : "===========================\n" +
                       "    let the games begin    \n" +
                       "===========================\n",
    "turn"           : "It's your turn: ",
    "choose_attack"  : "Where would you like to attack? \n" +
                       "Use the coordinates on your map to set your ship. \n" +
                       "(row,column), like : '1,3' or '4,2' \n",
    "hit"            : "That was a direct hit! Great job!",
    "miss"           : "You missed!",
    "win"            : "You've sunk all of your enemies ships! You've won!"
}

errors = {
    "incorrect_piece_format"    : "Be sure to use the format (row,col). i.e. 1,2",
}

symbols = {
    "ship"           : "^ ",
    "hit"            : "H ",
    "water"          : "w ",
    "empty"          : "0 ",
}

selection_board = {
    'board' : None
}

def print_pause(message, time):
    print(message)
    sleep(time)

def print_player_board(board):

    for col in board:
        for row in col:
            print(row, end="")
        print()

def create_board(size):
    board = []
    for i in range(0, size + 1):
        row = []
        for j in range(0, size + 1):
            if i == size and j == size:
                row.append("|")
            elif i == size:
                row.append(str(j + 1) + "*")
            elif j == size:
                row.append("|" + str(i + 1))
            else:
                row.append(symbols["empty"])
        board.append(row)

    return board

def parse_coordinates(location):
    temp_coordiantes = location.split(',')
    temp_coordiantes[0] = int(temp_coordiantes[0]) - 1
    temp_coordiantes[1] = int(temp_coordiantes[1]) - 1
    return temp_coordiantes

def is_location_valid(location, size):
    if len(location) is not 3:
        return False
    result = re.search(r"[\d][,][\d]", location)
    if result is None:
        return False

    temp_coordinates = parse_coordinates(location)

    if (temp_coordinates[0] >= size or temp_coordinates[1] >= size):
        return False
    if (temp_coordinates[0] < 0 or temp_coordinates[1] < 0):
        return False
    return True

def is_space_valid(location, size, grid, symbol):
    coordinates = parse_coordinates(location)

    for col in range(0, size):
        for row in range(0, size):
            if row == coordinates[0] and col == coordinates[1]:
                if grid[row][col] != symbol:
                    return False
    return True

def set_symbol(row, col, grid, symbol):
    grid[row][col] = symbol

def get_symbol(row, col, grid):
    return grid[row][col]

def set_selection_at(location, size, player_grid, symbol_to_place, symbol_to_validate):
    if not is_location_valid(location, size) or not is_space_valid(location, size, player_grid, symbol_to_validate):
        return False

    coordinates = parse_coordinates(location)

    set_symbol(coordinates[0], coordinates[1], player_grid, symbol_to_place)

    return True

def set_ships(ships, player_1, player_2):
    print_pause(messages["set_piece"], 1)

    print_player_board(player_1["board"])
    for i in range(0, ships):
        location = input(player_1["name"] + ", please set a ship: ")
        while (not set_selection_at(location, player_1["size"], player_1["board"], symbols["ship"], symbols["empty"])):
            print_pause(f"Your coordinates must fit in your {player_1['size']} x {player_1['size']} grid in an empty space.", 0)
            print_pause(errors["incorrect_piece_format"], 0)
            location = input(player_1["name"] + ", please set a ship: ")
        print_player_board(player_1["board"])


    print_pause(messages["set_piece"], 1)

    print_player_board(player_2["board"])
    for j in range(0, ships):
        location = input(player_2["name"] + ", please set a ship: ")
        while (not set_selection_at(location, player_2["size"], player_2["board"], symbols["ship"], symbols["empty"])):
            print_pause(f"Your coordinates must fit in your {player_2['size']}x{player_2['size']} grid\n", 0)
            print_pause(errors["incorrect_piece_format"], 0)
            location = input(player_2["name"] + ", please set a ship: ")
        print_player_board(player_2["board"])

def set_game():
    print_pause(messages["welcome"], 1)

    for i in range(1, 6):
        print_pause(messages["instructions_" + str(i)], 1)

    print_pause(messages["player_1"], 1)
    player_1 = input()
    print_pause(messages["player_2"], 1)
    player_2 = input()
    print_pause(messages["size"], 1)
    size = int(input())
    print_pause(messages["ships"], 1)
    ships = int(input())

    selection_board['board'] = create_board(size)

    player_one_grid = {
        "name" : player_1,
        "size" : size,
        "ships": ships,
        "board": create_board(size)
    }

    player_two_grid = {
        "name" : player_2,
        "size" : size,
        "ships": ships,
        "board": create_board(size)
    }

    game = {
        "player_1" : player_one_grid,
        "player_2" : player_two_grid,
    }


    set_ships(
        ships,
        player_one_grid,
        player_two_grid
    )

    return game

def check_if_player_lost(player):
    if player["ships"] == 0:
        return True
    return False

def remove_ship(player):
    player["ships"] -= 1

def play_game(game_board):

    print_pause(messages["start_game"], 1)

    player_lost = stop_game = False
    while not stop_game:
        for player, board in game_board.items():
            print_pause(messages["turn"] + board["name"], 1)
            print_player_board(selection_board["board"])
            selection = input(messages["choose_attack"])
            while (not is_location_valid(selection, board["size"])):
                print_pause(f"Your coordinates must fit in your {board['size']} x {board['size']}.", 0)
                print_pause(errors["incorrect_piece_format"], 0)
                selection = input(board["name"] + ", please choose where to attack: ")
            coordinates = parse_coordinates(selection)

            if player == 'player_1':
                if is_space_valid(selection, board['size'], game_board["player_2"]["board"], symbols["ship"]):
                    print_pause(messages["hit"], 1)
                    remove_ship(game_board["player_2"])
                    set_symbol(coordinates[0], coordinates[1], game_board["player_2"]["board"], symbols["hit"])

                    player_lost = check_if_player_lost(game_board["player_2"])
                else:
                    print_pause(messages["miss"], 1)
                    set_symbol(coordinates[0], coordinates[1], game_board["player_2"]["board"], symbols["water"])


            if player == 'player_2':
                if is_space_valid(selection, board['size'], game_board["player_1"]["board"], symbols["ship"]):
                    print_pause(messages["hit"], 1)
                    remove_ship(game_board["player_1"])
                    set_symbol(coordinates[0], coordinates[1], game_board["player_1"]["board"], symbols["hit"])

                    player_lost = check_if_player_lost(game_board["player_1"])
                else:
                    print_pause(messages["miss"], 1)
                    set_symbol(coordinates[0], coordinates[1], game_board["player_1"]["board"], symbols["water"])

            if player_lost:
                print_pause(f"{player}, {messages['win']}", 1)
                stop_game = True
                break


if __name__ == "__main__":
    game_board = set_game()
    play_game(game_board)
    print_pause("Here's how player 1's map looks like: ", 1)
    print_player_board(game_board["player_1"]["board"])

    print_pause("Here's how player 1's map looks like: ", 1)
    print_player_board(game_board["player_2"]["board"])

    print_pause("Thanks for playing", 1)
