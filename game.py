import pygame as pg

pg.init()

screen_width, screen_height = 800, 600


display = pg.display.set_mode((screen_width, screen_height))

display.fill('blue',(0, 0, screen_width, screen_height))

FPS = 24
clock = pg.time.Clock()

#изображения
bg_img = pg.image.load('src/background.png')
icon_img = pg.image.load('src/ufo.png')

pg.display.set_icon(icon_img)
pg.display.set_caption('Космическое вторжение')

#paint
sys_font = pg.font.SysFont('arial', 34)
font = pg.font.Font('src/04B_19.TTF', 48)

display.blit(bg_img, (0, 0))

text_img = sys_font.render('Score 123', True,'white')
display.blit(text_img,(0,0))

name_text = sys_font.render('Привет, меня зовут Евгений!', True, 'white')

game_over_text = font.render('Game Over', True, 'red')
w, h = game_over_text.get_size()
display.blit(game_over_text,(screen_width/2 - w/2, screen_height/2 - h/2))

#игрок
player_img = pg.image.load('src/player.png')
player_width, player_height = player_img.get_size()
player_gap = 10
display.blit(game_over_text,(screen_width/2 - w/2, screen_height/2 - h/2))


running = True
while running:
    pg.display.update()


    for event in pg.event.get():
        #Нажатие на крестик
        if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_q:
            running = False


    clock.tick(FPS)

pg.quit()