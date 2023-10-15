import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Crossy Road in 2D")

# Create a Turtle for drawing buttons
button_turtle = turtle.Turtle()
button_turtle.speed(0)
button_turtle.color("white")
button_turtle.penup()
button_turtle.hideturtle()

# Function to draw a button with text
def draw_button(x, y, text):
    button_turtle.goto(x, y)
    button_turtle.pendown()
    button_turtle.fillcolor("white")
    button_turtle.begin_fill()
    for _ in range(2):
        button_turtle.forward(200)
        button_turtle.left(90)
        button_turtle.forward(40)
        button_turtle.left(90)
    button_turtle.end_fill()
    button_turtle.penup()
    button_turtle.goto(x + 80, y + 10)
    button_turtle.color("black")
    button_turtle.write(text, align="center", font=("Arial", 16, "normal"))

# Function to check if the mouse is inside a button
def is_inside_button(x, y, button_x, button_y):
    return x >= button_x and x <= button_x + 200 and y >= button_y and y <= button_y + 40

# Variable to track whether the menu is open
menu_open = True  # Define menu_open here

# Define the show_menu function
def show_menu():
    global menu_open
    menu_open = True

# Function to handle button clicks
def on_click(x, y):
    global menu_open
    if is_inside_button(x, y, -100, 30):
        menu_open = False
        button_turtle.clear()  # Clear the buttons
        screen.onclick(None)  # Remove the event listeners
        import main
    elif is_inside_button(x, y, -100, -30):
        turtle.bye()  # Close the menu

# Register the click event
screen.onclick(on_click)

# Draw buttons
draw_button(-100, 30, "Start Game")
draw_button(-100, -30, "Quit")

# Main event loop
while menu_open:
    try:
        screen.update()
    except turtle.Terminator:
        pass
