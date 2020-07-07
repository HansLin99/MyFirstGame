import pygame
from pygame import *

pygame.init()
bg = pygame.image.load("Game/bg.jpg")
screenWidth = 800
screenHeight = 480

score = 0

# Main Character Class
class Character:
    # Image load
    walkLeft = [pygame.image.load("Game/L1.png"), pygame.image.load("Game/L2.png"), pygame.image.load("Game/L3.png"),
                pygame.image.load("Game/L4.png"),
                pygame.image.load("Game/L5.png"), pygame.image.load("Game/L6.png"), pygame.image.load("Game/L7.png"),
                pygame.image.load("Game/L8.png"),
                pygame.image.load("Game/L9.png")]
    walkRight = [pygame.image.load("Game/R1.png"), pygame.image.load("Game/R2.png"), pygame.image.load("Game/R3.png"),
                 pygame.image.load("Game/R4.png"),
                 pygame.image.load("Game/R5.png"), pygame.image.load("Game/R6.png"), pygame.image.load("Game/R7.png"),
                 pygame.image.load("Game/R8.png"),
                 pygame.image.load("Game/R9.png")]
    stand = pygame.image.load("Game/standing.png")

    def __init__(self, x, y, width, height, vel):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10
        self.walkCount = 0
        self.right = False
        self.left = False
        self.moving = False
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    # Based on the steps the man has walked, put the corresponding image onto the window
    # * Face to the direction which he stopped
    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.moving:
            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(self.walkLeft[0], (self.x, self.y))
            elif self.right:
                win.blit(self.walkRight[0], (self.x, self.y))
            else:
                win.blit(self.stand, (self.x, self.y))
            # else:
            #     if man.left:
            #         win.blit(walkLeft[0], (man.x, man.y))
            #     else:
            #         win.blit(walkRight[0], (man.x, man.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)




class Projectile:
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8 * direction

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy:
    walkLeft = [pygame.image.load("Game/L1E.png"), pygame.image.load("Game/L2E.png"), pygame.image.load("Game/L3E.png"),
                pygame.image.load("Game/L4E.png"),
                pygame.image.load("Game/L5E.png"), pygame.image.load("Game/L6E.png"), pygame.image.load("Game/L7E.png"),
                pygame.image.load("Game/L8E.png"),
                pygame.image.load("Game/L9E.png"), pygame.image.load("Game/L10E.png"), pygame.image.load("Game/L11E.png")]
    walkRight = [pygame.image.load("Game/R1E.png"), pygame.image.load("Game/R2E.png"), pygame.image.load("Game/R3E.png"),
                pygame.image.load("Game/R4E.png"),
                pygame.image.load("Game/R5E.png"), pygame.image.load("Game/R6E.png"), pygame.image.load("Game/R7E.png"),
                pygame.image.load("Game/R8E.png"),
                pygame.image.load("Game/R9E.png"), pygame.image.load("Game/R10E.png"),
                pygame.image.load("Game/R11E.png")]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.start = x
        self.width = width
        self.height = height
        self.end = end
        self.vel = 5
        self.walkCount = 0
        self.hitbox = (self.x + 20, self.y, 28, 60)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.walk()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            self.hitbox = (self.x + 20, self.y, 28, 60)
            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0), (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def walk(self):
        if self.vel > 0:
            if self.vel + self.x < self.end:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                # self.walkCount = 0
        else:
            if self.vel + self.x > 0:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                # self.walkCount = 0

    def hit(self):
        if self.health > 0:
            global score
            score += 1
            self.health -= 1
        else:
            self.visible = False



def reDrawWindow(man, goblin, bullets, win, font):
    # On every frame, put the bg image first
    win.blit(bg, (0, 0))
    text = font.render("Score: " + str(score),  1, (0,0,0))
    win.blit(text, (390, 10))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


def main():
    # x = 300
    # y = 300
    clock = pygame.time.Clock()
    man = Character(300, 300, 64, 64, 5)
    goblin = Enemy(100, 300, 64, 64, 600)
    font = pygame.font.SysFont("comicans", 30, True)
    bullets = []

    # width  = walkLeft[0].get_size()[0]
    # height = walkLeft[0].get_size()[1]
    # vel = 5
    # isJump = False
    # jumpCount = 10
    # walkCount = 0
    # right = False
    # left = False

    win = pygame.display.set_mode((screenWidth, screenHeight))
    pygame.display.set_caption("First Game")

    run = True
    while run:
        clock.tick(27)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    facing = -1 if man.left else 1

                    if len(bullets) < 50:
                        bullets.append(
                            Projectile(round(0.5 * man.width + man.x), round(0.5 * man.height + man.y), 3,
                                       (255, 0, 0),
                                       facing))

        for bullet in bullets:
            # Condition: if the bullets are within the hitbox of the enemy
            if goblin.visible:
                if bullet.y - bullet.radius > goblin.hitbox[1] and bullet.y + bullet.radius < goblin.hitbox[1] + goblin.hitbox[3]:
                    if bullet.x - bullet.radius > goblin.hitbox[0] and bullet.x + bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
                        goblin.hit()
                        bullets.pop(bullets.index(bullet))

            if 0 < bullet.x < screenWidth:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))

        keys = pygame.key.get_pressed()

        # These conditions respond to user key pressed
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
            man.right = False
            man.moving = True
        elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.vel - man.width:
            man.x += man.vel
            man.right = True
            man.left = False
            man.moving = True
        else:
            man.moving = False
            man.walkCount = 0

        if not man.isJump:
            if keys[pygame.K_UP]:
                man.isJump = True
                man.walkCount = 0
                # man.left = False
                # man.right = False
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount <= 0:
                    neg = -1
                man.y -= round((man.jumpCount ** 2) * 0.5 * neg)
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10
        reDrawWindow(man, goblin, bullets, win, font)
    pygame.quit()


# Start main window of the game
if __name__ == '__main__':
    main()
