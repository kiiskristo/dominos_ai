import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

class AIAgent:
    def __init__(self, name):
        self.name = name

    def generate_move(self, board_state):
        prompt = f"The current board state is: {board_state}\nWhat should {self.name} do next?"
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=50
        )
        return response.choices[0].text.strip()