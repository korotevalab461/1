import simpleguitk as simplegui
import random, math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
PAD_WIDTH = 8
PAD_HEIGHT = 80

def draw(c):
    global score1, score2

    c.draw_text(str(score1), (185, 60), 40, "White")
    c.draw_text(str(score2), (400, 60), 40, "White")

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # draw paddles
    c.draw_line([PAD_WIDTH/2, paddle1_pos],
                [PAD_WIDTH/2, paddle1_pos+PAD_HEIGHT],
                PAD_WIDTH, "White")
    c.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos],
                [WIDTH- PAD_WIDTH/2, paddle2_pos+PAD_HEIGHT],
                PAD_WIDTH, "White")

def keydown(key):
    pass

def keyup(key):
    pass

def restart():
    global score1, score2
    global paddle1_pos, paddle2_pos

    score1, score2 = 0, 0

    paddle1_pos, paddle2_pos = (HEIGHT - PAD_HEIGHT)/2, (HEIGHT - PAD_HEIGHT)/2


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)

restart()

# start frame
frame.start()