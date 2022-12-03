import random

game_board = {"1":" ","2":" ","3":" ",
         "4":" ","5":" ","6":" ",
         "7":" ","8":" ","9":" "}
keys = []

for key in game_board:
    keys.append(key)

def show_board(board):
    print(board["1"] + "|" + board["2"] + "|" + board["3"])
    print('-+-+-')
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print('-+-+-')
    print(board["7"] + "|" + board["8"] + "|" + board["9"])

turn = ["X","O"]
def random_turn():
    return random.choice(turn)

def game():

    turn = random_turn()
    count = 0
    for i in range(10):
        show_board(board=game_board)
        print(f"{turn} your turn choose your place")
        move=input()
        if game_board[move] == " ":
            game_board[move] = turn
            count += 1
        else:
            print("Already filled.")
            continue

        if count >=5:
            if game_board["1"] ==game_board["2"]==game_board["3"] != " ":
                show_board(game_board)
                print("The game is over.")
                print(f"{turn} won.")
                break
            elif game_board["4"] ==game_board["5"]==game_board["6"] != " ":
                show_board(game_board)
                print("The game is over.")
                print(f"{turn} won.")
                break
            elif game_board["7"] ==game_board["8"]==game_board["9"] != " ":
                show_board(game_board)
                print("The game is over.")
                print(f"{turn} won.")
                break
            elif game_board["1"] ==game_board["4"]==game_board["7"] != " ":
                show_board(game_board)
                print("The game is over.")
                print(f"{turn} won.")
                break
            elif game_board["2"] ==game_board["5"]==game_board["8"] != " ":
                show_board(game_board)
                print("The game is over.")
                print(f"{turn} won.")
                break
            elif game_board["3"] ==game_board["6"]==game_board["9"] != " ":
                show_board(game_board)
                print("The game is over.")
                print(f"{turn} won.")
                break
            elif game_board["1"] ==game_board["5"]==game_board["9"] != " ":
                show_board(game_board)
                print("The game is over.")
                print(f"{turn} won.")
                break
            elif game_board["3"] ==game_board["5"]==game_board["7"] != " ":
                show_board(game_board)
                print("The game is over.")
                print(f"{turn} won.")
                break

        if turn == "X":
            turn = "O"
        else:
            turn ="X"
    restart = input("Do you want to play again? (Y/N)").lower()
    if restart == "y":
        for key in keys:
            game_board[key] = " "

        game()

game()
