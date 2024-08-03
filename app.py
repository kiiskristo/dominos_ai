from game_manager import GameManager
from ai_agent import AIAgent

# Initialize game manager and AI agents
game_manager = GameManager()
ai_agent1 = AIAgent("AI1")
ai_agent2 = AIAgent("AI2")

# Game loop
while True:
    current_player = game_manager.get_current_player()
    print(f"It's {current_player}'s turn.")

    if "AI" in current_player:
        ai_agent = ai_agent1 if current_player == "AI1" else ai_agent2
        move = ai_agent.generate_move(game_manager.get_board_state())
        print(f"{current_player} plays: {move}")
    else:
        move = input(f"{current_player}, enter your move: ")

    game_manager.update_board(move)
    print(f"Board state: {game_manager.get_board_state()}")