# class Player
# attrs : {marker,score,name ,turn:bool }
# methods : { choose position,select marker }


class Checker:
   pass
class Player: 
   pass
class Board:
   pass



# class Board
# attrs : {board  }
# methods : { full, free space,clear,set position }

class Board:
    def __init__(self, board):
      self.board = board

    def free_space(self, position):
       return self.board[position] != ''
    def is_full(self):
       return ' ' is not self.board
    def clear_board(self):
        self.board = ['']*10

    def set_position():
       pass


class Player:
    def __init__(self,name):
        self.marker = None
        self.name = name
        self.score = 0
        self.turn = False

    def choose_position(self, board: Board):
        # cheker : check input
        while True:
            position=input('Dear '+ self.name +' please choose a position:')
            if position.isdigit():
                position=int(position)
                if position in range(1,10) and board.free_space(position): #board command
                    return position

    def select_marker(self):
      while True:
        player_sign = input(f'Dear {self.name}, choose X or O:')
        if player_sign in ['x','X']:
          self.marker = 'X'
          return ('X', 'O')
        elif player_sign in ['o','O']:
          self.marker = 'O'
          return ('O', 'X')
        
    def cal_score(self, checker: Checker, board: Board):
       if checker.win_check(board, self.name):
          self.score += 1

class Checker:
    def __init__(self):
      pass

    def win_check(board: Board, player: Player):
        win_list = [[1,2,3], [4,5,6], [7,8,9], [7,4,1], [8,5,2], [9,6,3], [7,5,3], [1,5,9]]
        board = ''.join(board).lower()
        player.marker

        for item in win_list:
            if (board[item[0]] == board[item[1]] == board[item[2]] == player.marker):
                return True
        else: 
            return False