import simpleguitk as simplegui
import random, math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400


def draw():
    pass

def keydown():
    pass

def keyup():
    pass

def restart():
    pass


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)

# start frame
frame.start()