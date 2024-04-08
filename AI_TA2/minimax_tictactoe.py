from random import randint

def sum(a, b, c ):
    return a + b + c

def minimax(depth, nodeIndex, isMax, scores, h):
    if depth == h:
        return scores[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, scores, h),
            minimax(depth + 1, nodeIndex * 2 + 1, False, scores, h)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, scores, h),
            minimax(depth + 1, nodeIndex * 2 + 1, True, scores, h)
        )

def log2(n):
    return 0 if n == 1 else 1 + log2(n // 2)

def o_player(xState, zState):
    availableMoves = [x for x in range(len(xState)) if xState[x] == 0 and zState[x] == 0]
    n = len(availableMoves)
    if len(availableMoves) == len(zState):
        availableMoves.sort()
        res = randint(availableMoves[0], availableMoves[-1])
    else:
        h = log2(n)
        res = minimax(0, 0, True, availableMoves, h)
    return res

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)
    print(f"{zero} | {one} | {two} ")
    print(f"--|---|---")
    print(f"{three} | {four} | {five} ")
    print(f"--|---|---")
    print(f"{six} | {seven} | {eight} ") 

loss_moves = []

def checkWin(xState, zState):
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in wins:
        if(sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3):
            print("X Won the match")
            o_player_moves = [x for x in range(len(zState)) if zState[x] == 1]
            loss_moves.append(o_player_moves)
            return 1
        if(sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3):
            print("O Won the match")
            return 0
    return -1
    
if __name__ == "__main__":
    while True:

        xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        turn = 1 
        print("Welcome to Tic Tac Toe")
        while(True):
            printBoard(xState, zState)
            if(turn == 1):
                print("O's Chance")
                value = o_player(xState, zState)
                zState[value] = 1
            else:
                print("X's Chance")
                value = int(input("Please enter a value: "))
                xState[value] = 1
            cwin = checkWin(xState, zState)
            if(cwin != -1):
                print("Match over")
                break
        
            turn = 1 - turn
        
        print("\nDo you want to play again? (y/n): ")
        if(input() == 'n'):
            # for i in loss_moves:
            #     print("[", end=" ")
            #     for j in i:
            #         print(j, end = ", ")
            #     print("]")
            break