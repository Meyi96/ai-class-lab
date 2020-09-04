import re
import random
_PLAYER = "player"
_MACHINE = "machine"

_PLAYER_SYMBOL = "X"
_MACHINE_SYMBOL = "O"

class TicTacToeGame():
  def __init__(self):
    self.board = [None] * 9
    self.turn = _PLAYER
    self.is_game_over = False
    self.winner = None

  def is_over(self):
    if self.board.count(None) <=4:
      if self.board.count(None)%2==0:
        return self.verify(_PLAYER_SYMBOL)
      else:
        return self.verify( _MACHINE_SYMBOL)
        
  def play(self):
    if self.turn == _PLAYER:
      self.player_turn()
      self.turn = _MACHINE
    else:
      self.machine_turn()
      self.turn = _PLAYER

  def player_choose_cell(self):
    print("Input empty cell bewtween 0 and 8")

    player_cell = input().strip()
    match = re.search("\d", player_cell)

    if not match:
      print("Input is not a number, please try again")

      return self.player_choose_cell()

    player_cell = int(player_cell)

    if self.board[player_cell] is not None:
      print("Cell is already taken, try again")

      return self.player_choose_cell()

    return player_cell

  def player_turn(self):
    chosen_cell = self.player_choose_cell()

    self.board[chosen_cell] = _PLAYER_SYMBOL

  def machine_turn(self):
    free = False
    while not free:
      num = random.randint(0,8)
      if self.board[num] is None:
         self.board[num] = _MACHINE_SYMBOL
         free= True

  def format_board(self):
    board=""
    for x in range(3):
      index = x*3
      a=b=c=" "
      if self.board[index] is not None:
        a = str(self.board[index])
      if self.board[index+1] is not None:
        b = str(self.board[index+1])
      if self.board[index+2] is not None:
        c = str(self.board[index+2])
      board = board+a+"|"+b+"|"+c+"\n"
    return board

  def print(self):
    print("Player turn:" if self.turn == _MACHINE else "Machine turn:")
    print(self.format_board())
    print()

  def print_result(self):
    if self.winner is None:
      print("Anyone's won")
    else:
      print("The winner is: "+ self.winner)

  def verifyMedium(self, symbol):
    return (self.board[3]==self.board[4]==self.board[5]==symbol) or (self.board[1]==self.board[4]==self.board[7]==symbol) or (self.board[0]==self.board[4]==self.board[8]==symbol) or (self.board[2]==self.board[4]==self.board[6]==symbol)

  def verifyEdge(self, symbol, corner):
    if corner ==0:
      return (self.board[corner]==self.board[1]==self.board[2]==symbol) or (self.board[corner]==self.board[3]==self.board[6]==symbol)
    else:
      return (self.board[corner]==self.board[2]==self.board[5]==symbol) or (self.board[corner]==self.board[6]==self.board[7]==symbol)

  def verify(self, symbol):
    state=False
    if self.board[4] == symbol:
      state= self.verifyMedium(symbol)
    if (not state) and self.board[0] == symbol:
      state= self.verifyEdge(symbol, 0)
    if (not state) and self.board[8] == symbol:
      state= self.verifyEdge(symbol, 8)
    if state and symbol== _PLAYER_SYMBOL:
      self.winner=_PLAYER
    elif state and symbol== _MACHINE_SYMBOL:
      self.winner=_MACHINE
    elif not state and self.board.count(None)==0:
      state = True
    return state


