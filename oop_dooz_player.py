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