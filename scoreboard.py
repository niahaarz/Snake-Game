from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier", 20, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open ('data.txt', mode='r') as f:
            self.high_score = int(f.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as f:
                f.write(f'{self.high_score}')
        self.score = 0
        self.update_scoreboard()



    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER!!', False, ALIGNMENT, FONT)

    def counter(self):
        self.score += 1
        self.update_scoreboard()
        
