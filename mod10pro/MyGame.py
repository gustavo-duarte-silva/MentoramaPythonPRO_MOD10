import pygame
import time
 
pygame.init()
 
clock = pygame.time.Clock()
autog = 0
coins = 0
display_width = 800
display_height = 600
white = (255, 255, 255)
black = (0, 0, 0)
grey = (128, 128, 128)
light_grey = (224, 224, 224)
 
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("MinerarBitCoins")

def autominer():
    global coins
    global autog
    time.sleep(0.1)
    coins = coins + autog
 
def DrawText(text, Textcolor, Rectcolor, x, y, fsize):
    font = pygame.font.Font('freesansbold.ttf', fsize)
    text = font.render(text, True, Textcolor, Rectcolor)
    textRect = text.get_rect()
    textRect.center = (x, y)
    gameDisplay.blit(text, textRect)
 
def rectangle(display, color, x, y, w, h):
    pygame.draw.rect(display, color, (x, y, w, h))
 
def main_loop():
    global clock
    global autog
    global ver
    mong = 1
    cost = 50
    cost2 = 50
    global coins
    game_running = True
    while game_running:
        if game_running: 
            autominer()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
 
            if event.type == pygame.MOUSEBUTTONDOWN:
                mopos = pygame.mouse.get_pos()
                if mopos >= (350, 0):
                    if mopos <= (450, 0):
                        coins += mong
 
                if mopos <= (800, 0):
                    if mopos >= (600, 0):
                        if coins >= cost:
                            coins = coins - cost
                            cost = cost * 1.5
                            mong = mong * 1.1
                            cost = round(cost, 0)
 
                if mopos >= (50, 0):
                    if mopos <= (245, 0):
                        if coins >= cost2:
                            coins = coins - cost2
                            cost2 = cost2 * 1.5
                            autog = autog + 0.5
                            cost2 = round(cost2, 0)
 
                if coins == 2147483647:
                    print("Voce Coletou Todos os BitCoins")
                    game_running = False
 
        gameDisplay.fill(white)
        DrawText("Clique Para Obter Bitcoins", black, white, 400, 180, 50)
        DrawText("BitCoins: " + str(f'{coins:.2f}') + " coins", black, white, 180, 50, 30)
        DrawText("Comprar Auto-Coletor: " + str(cost2), black, white, 171, 480, 20)
        rectangle(gameDisplay, black, 350, 250, 100, 100)
        rectangle(gameDisplay, light_grey, 100, 500, 50, 50)
        pygame.display.update()
        clock.tick(60)
 
main_loop()
pygame.quit()
quit()