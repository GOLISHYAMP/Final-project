# TIC TAC TOE GAME
import random 
def display(board):
    print(f'''
 {board[1]} | {board[2]} | {board[3]}                           1  |  2  |  3                                     
-----|-----|-----                        -----|-----|-----                                                              
 {board[4]} | {board[5]} | {board[6]}        POSITIONS---->     4  |  5  |  6  
-----|-----|-----                        -----|-----|-----                                                   
 {board[7]} | {board[8]} | {board[9]}                           7  |  8  |  9      
''')

def valid_posi(board,turn):
    print(turn +"chance")
    posi = valid_input()
    while True:
        if board[posi] == "   ":
            board[posi]= turn
            break
        else :
            print("sorry! overright cannot be done!")
            posi = valid_input() 
                
def valid_input():
    while True:
        posi = input("Enter the position\n")
        if posi != "   ":
            imp = int(posi)
            if imp in range(1,10):
                return imp
            else:
                print("invalid position")    
                        
        else:
            print("Thankyou for playing TIC TAC TOE game!")
            exit()

def check(board):
    check = 0
    #ROWS
    if board[1]==board[2]==board[3] !='   '  or  board[4]==board[5]==board[6] !='   '  or  board[7]==board[8]==board[9] !='   ' :
        check = 1
    #COLUMNS    
    elif board[1]==board[4]==board[7] !='   '  or  board[2]==board[5]==board[8] !='   '  or  board[3]==board[6]==board[9] !='   ' :
        check = 1
    #DIAGONALS
    elif board[1]==board[5]==board[9] !='   '  or  board[3]==board[5]==board[7] !='   ' :
        check = 1
    return check    






def userinput(board,symbol):
    player1,player2 = symbol[random.randint(0,1)]
    print(f"{player1} goes first")
    for i in range(9):
        if i % 2 ==0:
            turn=' '+player1+' '
        else:
            turn=' '+player2+' '
        valid_posi(board,turn)
        display(board)    
        if i>=4:
            condition = check(board)
            if condition==1:
                print(f"{turn} WON THE GAME!")
                break
        if i == 8:
            condition = check(board)
            if condition != 1:
                print("GAME IS DRAW!")
        
               

def main():
    repeat = True
    while repeat:
        board = ["making 9 places for X and O","   ","   ","   ","   ","   ","   ","   ","   ","   "]
        symbol = [('X','O'),('O','X')]
        print("WELCOME! LETS PLAY TIC TAC TOE GAME!")
        while True:
            marker = input("ENTER YOUR MARKER :    'X'   or  'O'\n").upper()
            if marker =='X' or marker=='O':
                print("GAME STARTS NOW!")
                display(board)
                break
            else :
                print("please enter the letter 'X' or 'O'")
        userinput(board,symbol)
        choice=input("want to play again! \npress: any letter for YES\npress: 'N' for NO\n").upper()
        if choice == 'N':
            repeat = False
    
        

main()