from player import Player
import random

class ComputerPlayer(Player):
    def get_move(self, board):
        move = self.find_winning_move(board, self.symbol)
        if move:
            print(f"Computer ({self.symbol}) chooses: {move}")
            return move

        opponent_symbol = 'X' if self.symbol == 'O' else 'O'
        move = self.find_winning_move(board, opponent_symbol)
        if move:
            print(f"Computer ({self.symbol}) chooses: {move}")
            return move

        if board.cells[5] == " ":
            print(f"Computer ({self.symbol}) chooses: 5")
            return 5

        for corner in [1, 3, 7, 9]:
            if board.cells[corner] == " ":
                print(f"Computer ({self.symbol}) chooses: {corner}")
                return corner

        available_cells = [cell for cell in board.cells if board.cells[cell] == " "]
        move = random.choice(available_cells)
        print(f"Computer ({self.symbol}) chooses: {move} (random move)")
        return move

    def find_winning_move(self, board, symbol):
        win_combos = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9], 
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  
            [1, 5, 9], [3, 5, 7]              
        ]
        for combo in win_combos:
            cells = [board.cells[cell] for cell in combo]
            if cells.count(symbol) == 2 and cells.count(" ") == 1:
                return combo[cells.index(" ")]
        return None
