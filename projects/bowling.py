
class BowlingGame:

    def __init__(self):
        self.game = [0] * 20
        self.num_rolls = 0

    def hit_pins(self, num_pins):
        self.game[self.num_rolls] = num_pins
        self.num_rolls += 1

    def get_score(self):
        score = 0
        for i in range(0, len(self.game), 2):
            if self.game[i] == 10:
                score += self.game[i] + self.get_score_helper(i + 1, 2)
            if self.game[i] + self.game[i + 1] == 10:
                score += self.get_score_helper(i, 1)

        return score

    def get_score_helper(self, i, num_next):
        score = 0; j = 0
        while i + j < len(self.game) and j < num_next:
            score += self.game[i + j]
