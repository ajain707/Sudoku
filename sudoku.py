board = [
    [7,8,5,4,3,9,1,2,6],
    [6,1,2,8,7,5,3,4,9],
    [4,9,3,6,2,1,5,7,8],
    [8,5,7,9,4,3,2,6,1],
    [2,6,1,7,5,8,9,3,4],
    [9,3,4,1,6,2,7,8,5],
    [5,7,8,3,9,4,6,1,2],
    [1,2,6,5,8,7,4,9,3],
    [3,4,9,2,1,6,8,0,7]
]

def display_board(board):
    for i in range(len(board)):
        if i % 3 == 0 or i==len(board)  :
            print(" ---------------------------")

        for j in range(9):
            if j % 3 == 0 :
                print(" | ", end="")
            if j == 8:
                print(str(board[i][j]) + " |")
            else:
                print(str(board[i][j]) + " ", end="")
    print(' ---------------------------')


def find_empty(board):
    for i in range(len(board)):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col

    return None

def game_over(board):
    return not(any(0 in row for row in board)) 


def is_valid(board, num, position):
    # Check if row is valid 
    for i in range(9):
        if board[position[0]][i] == num: #and position[1] != i:
            return False

    # Check if column is valid
    for i in range(len(board)):
        if board[i][position[1]] == num: #and position[0] != i:
            return False

    # Check if box is valid 
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num:
                return False

    return True
def original_board_numbers(board):
    # returns a list of original numbers in board (i.e numbers!=0) , these can't be changed during gameplay 
    original_pos= []
    for i in range(9):
        for j in range(9):
            if board[i][j]!=0:
                original_pos.append((i,j))
    return original_pos

def solve(bo):
    #base case 
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    #recursion 
    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False

def game_play():
    print("Welcome to Sudoku")
    print("Type "+ "\u0332".join("Done") +" at any of the inputs for computer to solve the game for you\n")

    board_copy = board
    original= original_board_numbers(board_copy) #gives list of original board numbers (tuples inside list)    
    game_on= True 
    game_done= False   
    player_quit= False 

    while game_on and not game_done:
        display_board(board)
        game_done= game_over(board)
        if game_done:
            break
        quit= input("Do you want to end the game, type Done: ").lower()
        quit.replace(' ','') 
        #checks if player wants to quit 
        if quit[0]=='d':
            print("Computer will now finish the game for you using some clever backtracking! \n")
            solve(board)
            display_board(board)  
            player_quit= True 
            
            break        
        # validate user input 
        valid_input= False 
        while valid_input is False:
            #check if number input is correct 
            valid_number= False; 
            while not valid_number:            
                number = int(input("Enter a number from 0-9: ")) #validate input later 
                if number<0 or number>9:
                    print("Invalid input try again")
                else:
                    valid_number=True 

            #check if position input is correct 
            valid_position=False
            while valid_position is False:
                pos=input("Enter Row,Column (0-8):")  
                p= (pos.split(","))
                position=[]
                for i in p:
                    position.append(int(i))         
                position = tuple(position)
                print(position)
                if position[0] in range(0,9) and position[1] in range(0,9):                    
                 #check if position entered is that of original numbers in board          
                    if position not in original:           
                        valid_position=True
                        break
                    else:
                        print("Can't Change original numbers of the board") 
                else:
                    print("Invalid position input try again")

            #check if position is valid (according to rules of the game)
            correct_pos= False
            while not correct_pos:
                if is_valid(board,number,position):
                    correct_pos=True
                else:
                    print("You cannot place this number here according to the rules!\n")
                    break                    

            if valid_number and valid_position and correct_pos:
                valid_input=True 
                               
        board[position[0]][position[1]] = number
    if player_quit:
        return ("Game Over....")
    else:
        return("Congratulations on finishing the game!")


        
print(game_play())

            
                

                

            
        


    



