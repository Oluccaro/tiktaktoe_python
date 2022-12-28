import os

#n counts the number of plays

turn = 'X'

def display_board(game_list):
    if 'X' not in game_list or 'O' not in game_list:
        print("\nThe board position is enumerated as following: ")
    print(' %s | %s | %s ' %(game_list[0],game_list[1],game_list[2]))
    print('---|---|---')
    print(' %s | %s | %s ' %(game_list[3],game_list[4],game_list[5]))
    print('---|---|---')
    print(' %s | %s | %s ' %(game_list[6],game_list[7],game_list[8]))


def choose_position(game_list,turn):
    choice = 'wrong'

    while choice not in game_list:
        print("\nIt's {} turn!".format(turn))
        choice=input("\nChoose one of the position available\n")
        if choice not in game_list:
            os.system('clear')
            print("Not a valid position, choose another one\n")
            display_board(game_list)
    game_list[int(choice)-1] = turn
    if turn == 'X':
        return 'O'
    else:
        return 'X'

def check_win(list):
    numSet = set([str(x) for x in range(1,10)])
    winning_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for x in winning_list:
        if list[x[0]] == list[x[1]] == list[x[2]]:
            print("\n{} ganhou!\n".format(list[x[0]]))
            display_board(game_list)
            return False
    gameSet = set(game_list)
    if len(numSet.intersection(game_list))==0:
        print("\nIt's a Tie!")
        return False
    return True

def playAgain(game_list):
    choice = 'wrong'
    validChoice = ['Y','y','n','N']
    while choice not in validChoice:
        choice = input("\nWanna play more? [y/n]: ")
        if choice == 'y' or choice == 'Y':
            return True
        elif choice == 'n' or choice == 'N':
            print("\nThank you for playing!")
            return False
        else:
            os.system('clear')
            print("\nPlease, choose a valid choice!")

game_list=[str(x) for x in range(1,10)]

playing=True

while(playing):
    os.system('clear')
    display_board(game_list)
    turn=choose_position(game_list,turn)
    playing=check_win(game_list)
    if(not playing):
        game_list=[str(x) for x in range(1,10)]
        playing=playAgain(game_list)
