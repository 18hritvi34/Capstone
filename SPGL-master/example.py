import spgl
import random

# Create Classes
class Player(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 3
        self.score = 0

    def tick(self):
        self.move()

    def move(self):
        self.fd(self.speed)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH /2 :
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

    def rotate_left(self):
        self.lt(30)

    def rotate_right(self):
        self.rt(30)

    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1
        if self.speed < 0:
            self.speed = 0

class Orb(spgl.Sprite):
    def __init__(self, shape, color, x, y):
        spgl.Sprite.__init__(self, shape, color, x, y)
        self.speed = 2
        self.setheading(random.randint(0,360))
        self.turn = 0

    def tick(self):
        self.move()
        if random.randint(0, 100) < 5:
            self.clear()

    def move(self):
        self.rt(random.randint(-10, 10))
        self.fd(self.speed)

        if self.xcor() > game.SCREEN_WIDTH / 2:
            self.goto(-game.SCREEN_WIDTH / 2, self.ycor())

        if self.xcor() < -game.SCREEN_WIDTH / 2:
            self.goto(game.SCREEN_WIDTH / 2, self.ycor())

        if self.ycor() > game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), -game.SCREEN_HEIGHT / 2)

        if self.ycor() < -game.SCREEN_HEIGHT / 2:
            self.goto(self.xcor(), game.SCREEN_HEIGHT / 2)

class Particle(spgl.Sprite):
    def __init__(self, spriteshape, color):
        spgl.Sprite.__init__(self, shape, color, 1000, 1000)
        self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
        self.goto(-1000,-1000)
        self.frame = 0.0
        self.max_frame = random.randint(5, 20)

    def tick(self):
        if self.frame != 0:
            self.fd(self.myspeed)
            self.frame += 1

        if self.frame > self.max_frame:
            self.goto(1000, 1000)
            self.frame = 0

    def explode(self, startx, starty):
        self.goto(startx,starty)
        self.setheading(random.randint(0,360))
        self.frame = 1.0
        self.myspeed = random.randint(3, 10)

class Explosion(object):
    def __init__(self):
        self.particles = []
        for _ in range(30):
            color = random.choice(["red", "yellow", "orange"])
            self.particles.append(Particle("circle", color))

    def explode(self, x, y):
        for particle in self.particles:
            particle.explode(x, y)

# Initial Game setup
game = spgl.Game(800, 600, "black", "SPGL Game Demo by /u/wynand1004 AKA @TokyoEdTech", 0)

# Game attributes
game.highscore = 0

# Load high score
highscore = game.load_data("highscore")
if highscore:
    game.highscore = highscore
else:
    game.highscore = 0

# Create Sprites
# Create Player
player = Player("triangle", "white", -400, 0)

# Create Orbs
for i in range(100):
    color = random.choice(["red", "yellow", "green"])
    shape = random.choice(["circle", "square", "triangle", "arrow"])
    orb = Orb(shape, color, 0, 0)
    speed = random.randint(1, 5)
    orb.speed = speed

# Create Explosion
explosion = Explosion()

# Create Labels
score_label = spgl.Label("Score: 0 Highscore: {}".format(game.highscore), "white", -380, 280)

# Create Buttons

# Set Keyboard Bindings
game.set_keyboard_binding(spgl.KEY_UP, player.accelerate)
game.set_keyboard_binding(spgl.KEY_DOWN, player.decelerate)
game.set_keyboard_binding(spgl.KEY_LEFT, player.rotate_left)
game.set_keyboard_binding(spgl.KEY_RIGHT, player.rotate_right)
game.set_keyboard_binding(spgl.KEY_ESCAPE, game.exit)

while True:
    # Call the game tick method
    game.tick()

    # Put your game logic here
    for sprite in game.sprites:
        # Check collisions with Orbs
        if sprite.state and isinstance(sprite, Orb):
            if game.is_collision(sprite, player):
                game.play_sound("collision.wav")
                
                middle_x = (sprite.xcor() + player.xcor()) / 2
                middle_y = (sprite.ycor() + player.ycor()) / 2

                explosion.explode(middle_x, middle_y)
                sprite.destroy()

                # Update Score
                if sprite.pencolor() == "red":
                    player.score -= 10
                if sprite.pencolor() == "green":
                    player.score += 10
                if sprite.pencolor() == "yellow":
                    player.score += 5

                # Update High Score
                if player.score > game.highscore:
                    game.highscore = player.score
                    game.save_data("highscore", game.highscore)

    # Update the Game Score, High Score, and Player Speed
    speed_string = "-" * int(player.speed)
    score_label.update("Score: {} High Score: {} Speed: {}".format(player.score, game.highscore, speed_string))

    # Show game info in terminal
    game.clear_terminal_screen()
    game.print_game_info()