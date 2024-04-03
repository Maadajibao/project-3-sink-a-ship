from random import randint



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


def game_run():

    welcome()


game_run()