from turtle import Turtle

FONT = ("Courier", 20, "normal")
GAMEOVER = ("Courier", 60, "normal")

class Scoreboard(Turtle):

    def __init__(self, show_menu_callback):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-300, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        self.restart_button = None
        self.show_menu = show_menu_callback  # Callback function to show the main menu

    def clear_scoreboard(self):
        self.clear()

    def increase_level(self):
        self.level += 1
        self.clear_scoreboard()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear_scoreboard()
        self.goto(0, 0)
        self.write("GAME OVER!!!", align="center", font=GAMEOVER)
        self.draw_restart_button()

    def draw_restart_button(self):
        self.restart_button = Turtle()
        self.restart_button.penup()
        self.restart_button.goto(0, -50)
        self.restart_button.color("black")
        self.restart_button.hideturtle()
        self.restart_button.write("Quit", align="center", font=("Arial", 16, "normal"))
        self.restart_button.onclick(self.restart_game)

    def is_inside_restart_button(self, x, y):
        if self.restart_button is not None:
            return -50 <= y <= -10
        return False

    def restart_game(self, x, y):
        if self.is_inside_restart_button(x, y):
            self.clear_scoreboard()
            self.show_menu()  # Call the callback function to show the main menu
