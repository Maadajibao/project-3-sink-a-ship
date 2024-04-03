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
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print_board(self):
        for row in self.board:
            print(" ".join(row))
        
    
    def add_ships(self, x, y, type):
        # in case we extend code so user can set amout of ships
        print("Number of ships:", len(self.ships))
        print("Maximum allower ships:", self.num_ships)
        if len(self.ships) >= self.num_ships:
            print("Error: You cannot add any more ships!")
        else:
            self.ships.append((x,y))
            if self.type == "player":
                self.board[x][y] = "@"

    def guess(self, x, y):
        self.guesses.append((x,y))
        self.board[x][y] = "X"

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return "Boom!(Hit)"
        else:
            return "Slaash(Miss)"


    

def random_point(size):
    """
    Generate a random number between 0 and the length of the board(size) minus one.
    We minus 1 for the size of the board we set.
    """
    return randint(0,size - 1)


def populate_board(board):
    """
    Will populate x with random_point and the same with y with ships from add_ship function.
    """


    for _ in range(board.num_ships):
        x = random_point(board.size)
        y = random_point(board.size)
        while (x,y) in board.ships:
            x = random_point(board.size)
            y = random_point(board.size)
        board.add_ships(x,y, board.type)




def welcome():
    """
    Welcome string that prompt for player name
    """

    print("Welcome to Sink A Ship, a battleship game\n")
    print("You as our general will command a feelt of 4 ship which will be randomly generated on the playboard\n")
    print("-" *35)
    print("\nMission:""You task is to Sink All Enemy Ships\n")
    print("-" *35)
    print(f"\nBoard Size:  | Number of Ships: ")
    print("Top left corner is row: 0, col: 0\n")
    print("-" *35)
    print("Whats your name General?:\n")
    




def start_game():

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    


    welcome()
    player_name = input("Please enter you name: ")
    
    computer_board = Board(size, num_ships, "computer", "computer")
    player_board = Board(size, num_ships, player_name, "player")

    for _ in range(num_ships):
        populate_board(player_board)
        populate_board(computer_board)



start_game()

