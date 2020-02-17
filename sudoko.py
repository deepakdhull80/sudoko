import time
'''board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

'''
def print_board(bo):

    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print('---------------------')
        for j in range(len(bo[0])):
            if j%3==0 and j!=0:
                print('|',end=' ')
            print(bo[i][j],end=' ')
            
        print('')

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return(i,j)
def valid(bo,num,co):
    # check the row
    for i in range(len(bo[0])):
        if bo[co[0]][i] ==num and i!=co[1]:
            return False

    #check the columns
    for i in range(len(bo)):
        if bo[i][co[1]]==num and i!=co[0]:
            return False
    # check for the box
    box_x=co[0]//3
    box_y=co[1]//3
    for i in range(box_x*3,box_x*3 +3):
        for j in range(box_y*3,box_y*3+3):
            if bo[i][j]==num and (i,j)!=co:
                return False
    return True

def solve(board):
    find=find_empty(board)
    if not find:
        return True
    else :
        x,y=find
    for i in range(1,10):
        if valid(board,i,find):
            board[x][y]=i

            if solve(board):
                return True
            board[x][y]=0
    return False
cur=time.time()

#print_board(board)
#print('\n')
#solve(board)
#print_board(board)
#now=time.time()

