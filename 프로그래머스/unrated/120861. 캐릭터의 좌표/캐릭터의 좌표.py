def solution(keyinput, board):
    result = [0, 0]
    ud = {'up':1,'down':-1}
    lr = {'right':1,'left':-1}
    for i in range(len(keyinput)):
        if keyinput[i] in ud:
            result[1]+=ud[keyinput[i]]
        elif keyinput[i] in lr:
            result[0]+=lr[keyinput[i]]
        if result[1] >= (board[1]-1)//2:
            result[1] = (board[1]-1)//2
        elif result[1] <= (board[1]-1)//2*-1:
            result[1] = (board[1]-1)//2*-1
        if result[0] >= (board[0]-1)//2:
            result[0] = (board[0]-1)//2
        elif result[0] <= (board[0]-1)//2*-1:
            result[0] = (board[0]-1)//2*-1
    return result