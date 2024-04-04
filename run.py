from random import randint

scores = {"computer": 0, "player": 0}

class Board:
    """
    Main board class. Sets Board size, the number of ships,
    the player's name and the board type(player or computer)
    Has methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, num_ships, name, board_type):
        self.size = size 
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = board_type
        self.guesses = []
        self.ships = []

    def print_board(self):
        """
        Prints board to terminal
        """

        # Print player's name

        print(f"\n{self.name}'s board:")

        for row in self.board:
            print(" ".join(row))
        
    
    def add_ships(self, x, y):
        # in case we extend code so user can set amout of ships    


        self.ships.append((x,y))
        if self.type == "player":
            self.board[x][y] = "@"


    def guess(self, x, y):
        """
        Accepts the coordinates of a guess and updates the board accordingly.
        Returns a message indicating whether the guess was hit or miss
        """

        self.guesses.append((x,y))
        

        if (x, y) in self.ships:
            self.board[x][y] = "*"
            return f"Boom! It Hits {self.name}"

        else:
            self.board[x][y] = "X"
            return f"Slaash! It Misses {self.name}"


    

def random_point(size):
    """
    Generate a random number between 0 and the length of the board(size) minus one.
    We minus 1 for the size of the board we set.
    """
    return randint(0, size - 1)


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
        board.add_ships(x, y)

    # Print the board after popilating with ships

    board.print_board()


def valid_coordinates(x, y):

    """
    Validates that the input coordinates are within the board
    """

    try:
        x = int(x)
        y = int(y)

        if x < 0 or x > 4 or y < 0 or y > 4:
            raise ValueError("Your shot is out of bounds! Choose a number within the board's range")
    
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.")
        print("Please enter an number between 1 and 5")
        return False
    return True



def make_guess(board):
    """
    Prompt the user to enter coordinates for a guess and checks if they are valid.
    If valid, returns the coordinates as tuple (x, y), otherwise returns None.
    """

    while True:
        x = input("Enter row (0-4): ")
        y = input("Enter column (0-4): ")

        if valid_coordinates(x, y):
            x = int(x) 
            y = int(y)
            if (x,y) not in board.guesses:  # Checks if the have not been guessed before
                return x, y
            else:
                print("\nYou'have already guessed these coordinates. Please try again.\n")
        else:
            print("invalid coordinates! Please try again")
    



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
    


def run_game(computer_board, player_board):
    """
    Runs the game loop until one of the players wins
    """

    while True:

        # Players turn

        print("\nPlayer's turn:")
        player_guess = make_guess(computer_board)
        if player_guess:
            x, y = player_guess
            player_result = computer_board.guess(x, y)
            player_board.guesses.append(player_guess)

            if  "Boom" in player_result:  # Check if the player hit a shit so that i can increment it
                scores["player"] += 1

            if not computer_board.ships:
                print("Congratulations! You have sunk all the enemy ships!")
                break
        
    


        
        # Computer's turn
        print("\nComputer's turn:")
        computer_guess = (random_point(len(player_board.board)), random_point(len(player_board.board)))
        computer_result = player_board.guess(computer_guess[0], computer_guess[1])
        computer_board.guesses.append(computer_guess)

        if  "Boom" in computer_result:  # Check if the computer hit a shit so that i can increment it
            scores["computer"] += 1


        if not player_board.ships:
            print("The computer has sunk all you ships. You lose!")
            break
        

        # Prints both player's and computer's boards after each turn

        player_board.print_board() 
        computer_board.print_board()   
    

        # Print player's and computer's guess and the result of the attacks

        print("-" * 35)        
        print("\nPlayer's guess:", player_guess)
        print("Player shoots....", player_result)
        
        print("\nComputer's guess:", computer_guess)
        print("Computer shoots...", computer_result)
        print("-" * 35)
        
        

        # Prints score

        print("-" * 35)
        print("\nAfter this round, scores are:")
        print(f"{player_board.name}:", scores["player"])
        print("Computer:", scores["computer"], "\n")
        print("-" * 35)

        # Prompt to quite the game

        quite_game = input("\nDo you want to quit the game? \nPress (y) otherwise press any other key: ")
        
        if quite_game.lower() == "y":
            print("Final Score:")
            print(f"{player_board.name}:", scores["player"])
            print("Computer:", scores["computer"])
            print("Thank you for playing!")
            return

    # Print the players and computer board

    print("\nPlayer's board:")
    player_board.print_board()
    print("Computer's board:")
    computer_board.print_board()
        
        



        
    



def start_game():
    """
    Sets the amout of ships and size of the board, it event sets the scores for both players.
    Runs the welcome function and prompt player for a name. 
    It also set the board for both player and computer and then generats the ships
    """

    size = 5
    num_ships = 4
    scores["computer"] = 0
    scores["player"] = 0
    
    welcome() 
    player_name = input("Please enter you name: ")
    
    
    computer_board = Board(size, num_ships, "computer", "computer")
    player_board = Board(size, num_ships, player_name, "player")

    
    populate_board(player_board)
    populate_board(computer_board)

    run_game(computer_board, player_board)



start_game()



