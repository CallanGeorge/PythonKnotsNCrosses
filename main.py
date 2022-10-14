import random





def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    team = 'Y'
    choices = ['X','O']

    while team not in choices:

        team = input("What team are you? X or O")

        if team not in choices:
            print("please enter X or O: ")

    if team.upper() == 'X':
        p1 = 'X'
        p2 = 'O'
    else:
        p1 = '0'
        p2 = 'X'

    return(p1,p2)



def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
        if board[1] == mark and board[2] == mark and board[3] == mark:
            return True
        elif board[1] == mark and board[4] == mark and board[7] == mark:
            return True
        elif board[4] == mark and board[5] == mark and board[6] == mark:
            return True
        elif board[7] == mark and board[8] == mark and board[9] == mark:
            return True
        elif board[2] == mark and board[5] == mark and board[8] == mark:
            return True
        elif board[3] == mark and board[6] == mark and board[9] == mark:
            return True
        elif board[1] == mark and board[5] == mark and board[9] == mark:
            return True
        elif board[3] == mark and board[5] == mark and board[7] == mark:
            return True
        else:
            return False

def choose_first():
    toss = random.randint(0,10)

    if toss %2 == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board,position):

    if board[position] != ' ':
        return False
    else:
        return True


def full_board_check(board):
    full = False

    for i in range(1,len(board)):
        if board[i] == ' ':
            full = False
        else:
            full = True

    return full


def player_choice(board):
    choice = 'Wrong'
    posAns = [1,2,3,4,5,6,7,8,9]

    while choice not in posAns:

        choice = int(input('Enter a position between 1-9 as a number'))

        if choice not in posAns:
            print('please enter a number between 1 and 9')

        if space_check(board, choice) == False:
            print('Space taken please choose another space')

    return choice

def replay():
    choice = 'Wrong'
    posAns = ['Y','N']

    while choice not in posAns:

        choice = input('Would you like to play again? Y or N')

        if choice not in posAns:
            print('please enter Y or N')

    if choice == 'Y':
        return True
    else:
        return False


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1, player2 = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1, position)

            if win_check(theBoard, player1):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2, position)

            if win_check(theBoard, player2):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break














