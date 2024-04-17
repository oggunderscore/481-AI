from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with the number of objects in each row."""

    def __init__(self, board=None):
        if board is None:
            board = [3, 1]  # Default board setup
        moves = self.get_moves(board)
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def get_moves(self, board):
        """Generate all possible moves given the current board state."""
        moves = []
        for index, piles in enumerate(board):
            for count in range(1, piles + 1):
                moves.append((index, count))
        return moves

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
        """Implement the result of a move."""
        new_board = state.board[:]
        new_board[move[0]] -= move[1]
        new_moves = self.get_moves(new_board)
        new_to_move = 'MIN' if state.to_move == 'MAX' else 'MAX'
        new_state = GameState(to_move=new_to_move, utility=self.compute_utility(new_board), board=new_board, moves=new_moves)
        return new_state

    def compute_utility(self, board):
        """Utility is 1 if game over on this board and the last player to move played a winning move (last move)."""
        if sum(board) == 0:  # Game over
            return 1  # Last move was winning move # LMAO SHOULD BE LOSING?
        return 0

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if player == 'MAX':
            return -state.utility
        else:
            return state.utility

    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return sum(state.board) == 0

    def display(self, state):
        print("board:", state.board)

if __name__ == "__main__":
    nim = GameOfNim(board=[7,5,3,1])  # Creating the game instance
    print("Initial board:", nim.initial.board)  # Output: [0, 5, 3, 1]
    print("Initial moves:", nim.initial.moves)  # Output will show all possible moves from this state

    # Example of playing the game against another agent (simulation)
    utility = nim.play_game(alpha_beta_player, query_player)  # Computer moves first using alpha_beta_player
    if utility < 0:
        print("alpha_beta_player won the game")
    else:
        print("User has won the game")

