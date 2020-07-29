#Function to select the marker (X or O) for the first Player
#Player1 is always set to go first
def player_choice():
    
    pl_choice = 'Player 1 '
    
    while pl_choice not in ('X','O','x','o'):
        pl_choice = input("Hey Player1!, please choose 'X' or 'O' : ")
        
        if pl_choice not in ('X','O','x','o'):
            print("Hey Player1, please enter a valid choice")
    
    if pl_choice in ('x','X'):
        return ('X','O')
    else:
        return ('O','X')
    


#Function to place the marker on the board
def place_marker(board,pl_position,pl_marker):
    
    board[pl_position] = pl_marker 



#Function to check if the choosen position is not taken previously
def space_check(board, position):
    
    return board[position] == ' '



#Function to get the position from the players
#Validate the choosen position
def position(player,board):
    
    pl_position = 'None'
    player_no = player
    
    while pl_position not in range (1,10) or not space_check(board, pl_position):
        pl_position = input(player_no + " please select a position (1 to 9) : ")
        
        if pl_position.isdigit() == True:
            
            pl_position = int(pl_position)
            
            if pl_position not in range (1,10):
                print("Input is not in the range of 1 to 9 ")
        
        else:
            print("Input is not a digit")
        
    return pl_position




#Print the board
def print_board(board):

    
    print("  " +board[7]+ "  |  " +board[8]+ "  |  " +board[9]+ "  ")
    print("-----------------")
    print("  " +board[4]+ "  |  " +board[5]+ "  |  " +board[6]+ "  ")
    print("-----------------")
    print("  " +board[1]+ "  |  " +board[2]+ "  |  " +board[3]+ "  ")




#Check the winning conditions
def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal




#Check if the board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True



#Main module 
print("Welcome to Tic Tac Toe")

replay = 'Ask'

while True :
    

    play = 'New'
    close_game = 'N'
    player = 'Player1'
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

    while play not in ('Y','y','n','N'):
    
    
        if replay not in ('Y','y'):
            play = input("Play the game? (Y/N)")
        
        else:
            play = 'Y'
            
            
        if play in ('y','Y'):
            game_on = True
            replay ='Ask'
            pl1_marker , pl2_marker = player_choice()
            
        elif play in ('n','N'):
            replay = 'No'
            game_on = False
            break
        else:
            print("Invalid choice")
            
    
    while game_on == True :
        
        #Player1 moves
        if player == 'Player1' : 
            print_board(board)
            pl1_position = position(player,board)
            place_marker(board,pl1_position,pl1_marker)
            
            if win_check(board,pl1_marker):
                print_board(board)
                print("Player 1 has won this round")
                game_on = False
                break
                
            else:
                if full_board_check(board):
                    print_board(board)
                    print('The game is a draw!')
                    break
                else:
                    player = 'Player2'

        
        #Player2 moves
        else :           
            print_board(board)
            pl2_position = position(player,board)
            place_marker(board,pl2_position,pl2_marker)
            
            if win_check(board,pl2_marker):
                print_board(board)
                print("Player1 has won this round")
                gamre_on = False
                break
                
            else:
                if full_board_check(board):
                    print_board(board)
                    print('The game is a draw!')
                    break
                else:
                    player = 'Player1'
            
            
            
    #check for replay   
    if replay != 'No' :

        replay = input("Do you want to play again? Choose Y or N")
    
        if replay in ('Y','y') :
            pass
        elif replay in ('N','n') :
            break
        
    else:
        break
        

        

    
