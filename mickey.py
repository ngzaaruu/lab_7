import pygame
import datetime

pygame.init()
isDone = True
white = (255, 255, 255)
size = (450, 400)
screen = pygame.display.set_mode(size)
screen.fill(white)
clock = pygame.image.load("lab_7/images/mickeyWithoutArms.png")
leftArmIMAGE = pygame.image.load("lab_7/images/leftarm (2).png")
rightArmIMAGE = pygame.image.load("lab_7/images/rightarm.png")
pygame.display.update()

leftArm = 0
rightArm = 0
left1 = pygame.transform.scale(leftArmIMAGE, (20, 20))
right = pygame.transform.scale(rightArmIMAGE, (20, 20))

while isDone:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isDone = False
            pygame.quit()

    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second

    clock1 = pygame.transform.scale(clock, (clock.get_width() // 3, clock.get_height() // 3))
    screen.blit(clock1, (0, 0))

    leftArm = second * (-6)
    rightArm = minute * (-6)

    pygame.display.update()
    pygame.display.flip()