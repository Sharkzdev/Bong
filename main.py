import pygame,random
pygame.init()

#window
win_height = 500
win_width = 750
win = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption('Pong')
icon = pygame.image.load('ghost.png')
pygame.display.set_icon(icon)

#info.miscalniouse
hit = True
hity = True
font = pygame.font.SysFont(None, 50)
score1 = 0
score2 = 0

#bg_music =  pygame.mixer.Sound("music.mp3")
#pygame.mixer.music.load("music.mp3")
#pygame.mixer.music.play(-1)

#colour palette
white = (255,255,255)
pink = (255,184,191)
brown = (101,56,24)
dark_brown = (78,53,36)
black = (0,0,0)

#paddle 1
p1_x = 0
p1_y = win_height/2 - 30
p1_width = 15
p1_height = 100

#paddle 2
p2_x = win_width - 15
p2_y = win_height/2 - 30
p2_width = 15
p2_height = 100
paddle_vel = 10

#ball
ball_x = win_width/2
ball_y = win_height/2 + 10
ball_radius = 12
ball_border = 3
ball_vel = 5
direction = random.randint(0,1)

#line
line_start_pos = ((win_width/2) -4,0)
line_end_pos = ((win_width/2) -4,500)
line_width = 4
#functions

#pygame.draw.circle(win,(255,255,255),(x,y),r,borderwidth)
#rect(surface, color, rect)
#line(surface, color, start_pos, end_pos, width=1)
#gameloop
running = True
while running:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #keys
    keys = pygame.key.get_pressed()
    #p2 movement
    if keys[pygame.K_UP]:
        p2_y -= paddle_vel
    elif keys[pygame.K_DOWN]:
        p2_y += paddle_vel
    #p1 movement
    if keys[pygame.K_w]:
        p1_y -= paddle_vel
    elif keys[pygame.K_s]:
        p1_y += paddle_vel
    #ball movement


    #collision
    if p1_y >= (win_height - p1_height + 10):
        p1_y -= paddle_vel + 5
    elif p1_y <= 0:
        p1_y += paddle_vel
    if p2_y >= (win_height - p1_height + 10):
        p2_y -= paddle_vel + 5
    elif p2_y <= 0:
        p2_y += paddle_vel
    #ballcollision
    if hit == True:
        ball_x -= ball_vel
    else:
        ball_x += ball_vel
    
    #img = font.render('hello', True, (0,0,234))
    #win.blit(img, (20, 20))
    #score
    if ball_x <= 0:
        ball_x = win_width/2
        ball_y = win_height/2 + 10
        hit = False
        score2 += 1
    if ball_x >= win_width: #+ (ball_radius*2):
        ball_x = win_width/2
        ball_y = win_height/2 + 10
        hit = True
        score1 += 1

    if hity == True:
        ball_y -= ball_vel
    else:
        ball_y += ball_vel
    if ball_y <= 0:
        hity = False
    if ball_y >= win_height: # - (ball_radius*2):
        hity = True

    #draw
    win.fill(white)
    pygame.draw.line(win,pink,line_start_pos,line_end_pos,line_width)
    paddle1 = pygame.draw.rect(win,pink,(p1_x,p1_y,p1_width,p1_height))
    paddle2 = pygame.draw.rect(win,pink,(p2_x,p2_y,p2_width,p2_height))
    ball = pygame.draw.circle(win,pink,(ball_x,ball_y),ball_radius,ball_border)

    if ball.colliderect(paddle2):
        hit = True
    elif ball.colliderect(paddle1):
        hit = False
    
    score_p1 = font.render(str(score1), True, pink)
    score_p2 = font.render(str(score2), True, pink)

    win.blit(score_p1, ((win_width/2) - 70, 20))
    win.blit(score_p2, ((win_width/2) + 50, 20))

    pygame.display.update()