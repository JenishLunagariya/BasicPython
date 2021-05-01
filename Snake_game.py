import pygame
import random
pygame.init()

dis_width=800
dis_height=600

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("Snake Game By BunTy")

white=(255,255,255)
blue=(0,0,255)
red=(255,0,0)
black=(0,0,0)
yellow=(255,255,102)
green=(0,255,0)

game_over=False

snake_block=10
snake_speed=15

font_style=pygame.font.SysFont('arial',30)
score_font=pygame.font.SysFont('calibry bold',25)

clock=pygame.time.Clock()

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.circle(dis,black,[x[0],x[1]],snake_block,snake_block) # Updated By BunTy


def Your_score(score):
    value=score_font.render("Score:"+str(score),True,green)
    dis.blit(value,[0,0])

def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[260,230])



def gameloop():
    game_over=False
    game_close=False

    x1 = 260
    y1 = 230

    x1_change = 0
    y1_change = 0

    snake_list=[]
    Length_of_snake=1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    # To prevent screen from being disappear
    while not game_over:

        while game_close==True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again",red)
            Your_score((Length_of_snake-1)*10)
            pygame.display.update()

            # Ask Player to Continue game or Quit the Game
            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True
                        game_close=False
                    if event.key==pygame.K_c:
                        gameloop()

        # To Close the Window ,when player click on close button at the right corner
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            # Below Code, moves the snake Up,Down,Right & Left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -10  # instead of 10, you can use snake_block also.
                    y1_change = 0  # To move snake Diagonally comment out this line
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0  # To move snake Diagonally comment out this line
                elif event.key == pygame.K_UP:
                    x1_change = 0  # To move snake Diagonally comment out this line
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0  # To move snake Diagonally comment out this line
                    y1_change = 10
        '''below condition is used, to Show Lose , when snake go beyond screen
        if x1>=dis_width or x1<0 or y1>=dis_width or y1<0:
            game_over=True'''

        # when Snake goes beyond display, Below code will Reappear it as Nokia Phones
        # Updated By BunTy
        if x1 >= dis_width:
            x1 = 0
            y1 = y1
        elif x1 < 0:
            x1 = dis_width
            y1 = y1
        elif y1 >= dis_height:
            y1 = 0
            x1 = x1
        elif y1 < 0:
            y1 = dis_height
            x1 = x1

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)

        pygame.draw.circle(dis,blue,[foodx,foody],10,10)  # Updated By BunTy

        snake_head=[]
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list)>Length_of_snake:
            del snake_list[0]
        for x in snake_list[:-1]:
            if x==snake_head:
                game_close=True

        our_snake(snake_block,snake_list)
        Your_score((Length_of_snake-1)*10)
        # snake_speed=10


        if x1==foodx and y1==foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake+=1
            # snake_speed+=10

        clock.tick(snake_speed)  # To adjust the speed of snake By BunTy
        pygame.display.update()

    pygame.quit()
    quit()


gameloop()

