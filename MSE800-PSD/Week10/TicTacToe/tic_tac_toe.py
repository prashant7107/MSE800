"""Tic-tac-toe game"""

from typing import List


class TicTacToe:
    """Class representing the Tic-tac-toe game."""

    def __init__(self):
        """Initialize the board."""
        self.board: List[str] = [" "] * 9
        self.p = "X"

    def show_board(self):
        """Display the current state of the board."""
        print(f"\n {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} \n")

    def make_move(self, pos: int):
        """Validate and execute a player's move."""
        if 0 <= pos < 9 and self.board[pos] == " ":
            self.board[pos] = self.p
            return True
        return False

    def swap_player(self):
        """Toggle the active player to move."""
        self.p = "O" if self.p == "X" else "X"

    def check_result(self):
        """Check if there is a winner or a draw."""
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in lines:
            if self.board[a] == self.board[b] == self.board[c] != " ":
                return self.board[a]
        if " " not in self.board:
            return "Draw"
        return None


if __name__ == "__main__":
    game = TicTacToe()
    print("Tic-Tac-Toe Started!")
    while True:
        game.show_board()
        print(f"Player {game.p} turn")
        try:
            choice = int(input("Pick 1-9: ")) - 1
        except ValueError:
            print("Bad input!")
            continue
        if not game.make_move(choice):
            print("Bad move!")
            continue
        winner = game.check_result()
        if winner:
            game.show_board()
            print(f"Winner: {winner}" if winner != "Draw" else "Draw!")
            break
        game.swap_player()
        