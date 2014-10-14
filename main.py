import simpleguitk as simplegui
import random, math

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
PAD_WIDTH = 8
PAD_HEIGHT = 80
BALL_RADIUS = 20
PAD_VEL = 3

# helper function that spawns a ball by updating the ball's position vector
# and velocity vector if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists

    ball_pos = [WIDTH/2, HEIGHT/2]
    if right == True:
        ball_vel = [random.randrange(2, 4),-random.randrange(1, 3)]
    else:
        ball_vel = [-random.randrange(2, 4),-random.randrange(1, 3)]

def draw(c):
    global score1, score2
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel

    c.draw_text(str(score1), (185, 60), 40, "White")
    c.draw_text(str(score2), (400, 60), 40, "White")

    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update paddle's vertical position, keep paddle on the screen
    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel

    # draw paddles
    c.draw_line([PAD_WIDTH/2, paddle1_pos],
                [PAD_WIDTH/2, paddle1_pos+PAD_HEIGHT],
                PAD_WIDTH, "White")
    c.draw_line([WIDTH - PAD_WIDTH/2, paddle2_pos],
                [WIDTH- PAD_WIDTH/2, paddle2_pos+PAD_HEIGHT],
                PAD_WIDTH, "White")

    # update ball
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 0.1, "White", "White")

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = PAD_VEL
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -PAD_VEL
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = PAD_VEL
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -PAD_VEL

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0

def restart():
    global score1, score2
    global paddle1_pos, paddle2_pos
    global side
    global paddle1_vel, paddle2_vel

    score1, score2 = 0, 0

    paddle1_pos, paddle2_pos = (HEIGHT - PAD_HEIGHT)/2, (HEIGHT - PAD_HEIGHT)/2

    paddle1_vel = paddle2_vel = 0

    side = True
    ball_init(side)


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)

restart()

# start frame
frame.start()