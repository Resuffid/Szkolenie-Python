# Tablica do gry
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

def display_board():
  print("\n")
  print (board[0] + " | " + board[1] + " | " + board[2] + "   1 | 2 | 3")
  print (board[3] + " | " + board[4] + " | " + board[5] + "   4 | 5 | 6")
  print (board[6] + " | " + board[7] + " | " + board[8] + "   7 | 8 | 9")

# Tura gracza
def handle_turn(player):
  print(player + " twoja kolej")
  position = input("Wybierz pozycję od 1 do 9: ")
  while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    position = input("Błędna wartość. Wybierz pozycję od 1 do 9: ")
  position = int(position) - 1
  if board[position] != "-":
    print("To miejsce na planszy już jest zajęte")
  board[position] = player
  display_board()

# Sprawdzanie wygranej
def check_rows():
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  if row_1 or row_2 or row_3:
    return True
  else:
    return False

def check_columns():
  column_1 == board[0] == board[3] == board[6] != "-"
  column_2 == board[1] == board[4] == board[7] != "-"
  column_3 == board[2] == board[5] == board[8] != "-"
  
  if column_1 or column_2 or column_3:
    return True
  else:
    return False

def check_diagonals():
  diagonal_1 == board[0] == board[4] == board[8] != "-"
  diagonal_2 == board[2] == board[4] == board[6] != "-"
  if diagonal_1 or diagonal_2:
    return True
  else:
    return False

def flip_player(current_player):
  if current_player == "X":
    current_player = "O"
  else:
    current_player = "X"
  return current_player

def check_if_game_is_on(current_player):
  if check_rows() or check_columns() or check_diagonals():
    winner = flip_player(current_player)
    print("Gratulacje" + winner + "! Wygrałeś!")
    return False
  elif "-" not in board:
    print("Mamy remis!")
    return False
  else:
    return True

def play_game():
  display_board()
  current_player = "X"
  while check_if_game_is_on(current_player):
    handle_turn(current_player)
    current_player = flip_player(current_player)
    
play_game()
