
"""
Player class that has
    following attrs => marker, name, score, turn
    following methods => choose_position, select_marker, cal_score
"""
class Player:
    def __init__(self,name):
        # marker will be 'X' or 'O'
        self.marker = None
        # name of the player
        self.name = name
        self.score = 0
        self.turn = False

    # gets board object from Board class and returns the valid position between 1 and 9 based on the board 
    def choose_position(self, board):
        while True:
            position=input('Dear '+ self.name +' please choose a position:')
            if position.isdigit():
                position=int(position)
                if position in range(1,10) and board.free_space(position): 
                    return position

    # based on player input, it figures the marker and returns the (selected_marker, other_marker)
    def select_marker(self):
      while True:
        player_sign = input(f'Dear {self.name}, choose X or O:')
        if player_sign in ['x','X']:
          self.marker = 'X'
          return ('X', 'O')
        elif player_sign in ['o','O']:
          self.marker = 'O'
          return ('O', 'X')
        
    # it gets the checker object and board object from Checker and Board classes and checks a player with specific name has won. if yes, the score will be incremented by 1
    def cal_score(self, checker, board):
       if checker.win_check(board, self.name):
          self.score += 1