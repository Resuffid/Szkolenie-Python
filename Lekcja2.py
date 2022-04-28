# Tablica do gry
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
  print("\n")
  print (board[0] + " | " + board[1] + " | " + board[2] + "   1 | 2 | 3")
  print (board[3] + " | " + board[4] + " | " + board[5] + "   4 | 5 | 6")
  print (board[6] + " | " + board[7] + " | " + board[8] + "   7 | 8 | 9")

display_board()

def play_game():
  display_board()
  
play_game()
