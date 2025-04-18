import pygame
from os.path import join
from random import randint

#general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface= pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Space Shooter')
running = True
clock = pygame.time.Clock()

#plain surface
surf = pygame.Surface((50, 100))
surf.fill('green')
x = 100

# importing the image
player_surf = pygame.image.load('../images/player.png').convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

meteor_surd = pygame.image.load('../images/meteor.png').convert_alpha()
meteor_rect = meteor_surd.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2))

laser_surf = pygame.image.load('../images/laser.png').convert_alpha()
laser_rect = laser_surf.get_frect(bottomleft = (20, WINDOW_HEIGHT-20))
#player_surf = pygame.transform.scale(player_surf, (50, 100))

star_surf = pygame.image.load('../images/star.png')
star_position = [(randint(0, WINDOW_WIDTH),randint(0, WINDOW_HEIGHT)) for i in range(20)]

player_direction = pygame.math.Vector2(1, 1)
plaryer_speed = 200


# Game loop
while running:
    dt = clock.tick(40)/1000 #time per frame
    #event loop 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    #draw the game
    #fill the window with red color
    display_surface.fill('dark gray')
    for pos in star_position: 
     display_surface.blit(star_surf,pos)

    display_surface.blit(meteor_surd, meteor_rect)
    display_surface.blit(laser_surf, laser_rect)

   #player movement
    if player_rect.left <=0 or player_rect.right >= WINDOW_WIDTH:
        player_direction.x *= -1
    if player_rect.top <= 0 or player_rect.bottom >= WINDOW_HEIGHT:
        player_direction.y *= -1
    player_rect.center += player_direction* plaryer_speed*dt
    display_surface.blit(player_surf,player_rect)

    pygame.display.update()



pygame.QUIT()