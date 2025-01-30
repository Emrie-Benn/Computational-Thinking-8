#Section 1: Setup
import codesters
from codesters import StageClass
stage = StageClass()

stage.set_background("moon")
s1 = codesters.Sprite("person1",0,-200)
s1.set_size(0.5)

Speed = 5

#section 2: define controls
def move_up(sprite):
        sprite.move_up(Speed)

def move_down(sprite):
        sprite.move_down(Speed)

def move_left(sprite):
        sprite.move_left(Speed)

def move_right(sprite):
        sprite.move_right(Speed)

#section 3: define hide amd show
def hide (sprite):
        sprite.hide()
def show (sprite):
        sprite.show()
def turn_left (sprite):
        heading = sprite.heading
        sprite.set_heading (heading + Speed)
def turn_right (sprite):
        heading = sprite.heading
        sprite.set_heading (heading - Speed) 
def forward (sprite):
        sprite.forward(Speed)   
def draw (sprite):
        sprite.pen_down()
def stop_drawing (sprite):
        sprite.pen_up()
def erase (sprite):
        sprite.pen_clear()
def yellow_pen (sprite):
        sprite.set_color("yellow")
def pink_pen (sprite):
        sprite.set_color("pink")

#section 4:bind controls
s1.event_key("w", move_up)
s1.event_key("s", move_down)
s1.event_key("a", move_left)
s1.event_key("d", move_right)
s1.event_key("h", hide)
s1.event_key("g", show)
s1.event_key("z", turn_left)
s1.event_key("x", forward)
s1.event_key("c", turn_right)
s1.event_key("o", draw)
s1.event_key("p", stop_drawing)
s1.event_key("e", erase)
s1.event_key("y", yellow_pen)
s1.event_key("u", pink_pen)


#section 5: reminder
print("Game has started. Open the screen using PORTS")