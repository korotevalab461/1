import simpleguitk as simplegui
import random, math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400

def draw(c):
    global score1, score2

    c.draw_text(str(score1), (185, 60), 40, "White")
    c.draw_text(str(score2), (400, 60), 40, "White")

def keydown(key):
    pass

def keyup(key):
    pass

def restart():
    global score1, score2

    score1, score2 = 0, 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)

restart()

# start frame
frame.start()