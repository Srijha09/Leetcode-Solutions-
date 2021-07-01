# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 22:55:35 2021

@author: Srijhak
On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.
"""

def numRookCaptures(board):
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]=='R':
                row,col = i,j
                break
            
    res = 0
    
    for i in range(row-1,-1,-1):
        if board[i][col]=='B':
            break
        if board[i][col]=='r':
            res+=1
            break
    
    for i in range(row+1,8):
        if board[i][col]=='B':
            break
        if board[i][col]=='r':
            res+=1
            break
    
    for j in range(col-1,-1,-1):
        if board[row][j]=='B':
            break
        if board[row][j]=='r':
            res+=1
            break
    
    for j in range(col+1,8):
        if board[row][j]=='B':
            break
        if board[row][j]=='r':
            res+=1
            break
    
            