import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

class GameManager:
    def __init__(self):
        self.board_state = []
        self.players = ["Player1", "AI1", "Player2", "AI2"]
        self.current_turn = 0

    def update_board(self, move):
        self.board_state.append(move)
        self.current_turn = (self.current_turn + 1) % len(self.players)

    def get_board_state(self):
        return self.board_state

    def get_current_player(self):
        return self.players[self.current_turn]