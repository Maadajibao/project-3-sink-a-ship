from random import randint

class Board:
    """
    Main board class, as size, board and ship attribute. 
    """

    def __init__(self, size):
        self.size = size 
        self.board = [["." for x in range(size)] for y in range(size)]
    

def random_point(size):
    """
    Generate a random number between 0 and the length of the board minus one.
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

