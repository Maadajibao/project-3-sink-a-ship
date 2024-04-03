from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    Main board class. Sets Board size, the number of ships,
    the player's name and the board type(player or computer)
    Has methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size 
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self. name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        
    
    def add_ships(self, x, y, type = "computer"):
        # in case we extend code so user can set amout of ships
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add any more ships!")
        else:
            self.ships.append((x,y))
            if self.type == "player":
                self.board[x][y] = "@"


    

def random_point(size):
    """
    Generate a random number between 0 and the length of the board(size) minus one.
    We minus 1 for the size of the board we set.
    """
    return randint(0,size - 1)




def welcome():
    """
    Welcome string that prompt for player name
    """

    print("Welcome to Sink A Ship, a battleship game\n")
    print("You as our general will command a feelt of 4 ship which will be randomly generated on the playboard\n")
    print("-" *35)
    print("\nMission:""You task is to Sink All Enemy Ships\n")
    print("-" *35)
    print(f"\nBoard Size: | Number of Ships")
    print("Top left corner is row: 0, col: 0\n")
    print("-" *35)
    print("Whats your name General?:\n")
    input("Please enter you name: ")


def game_run():


    welcome()


game_run()

