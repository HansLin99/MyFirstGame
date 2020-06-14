import pygame

pygame.init()
bg = pygame.image.load("Game/bg.jpg")
screenWidth = 800
screenHeight = 480


# Main Character Class
class Character():
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




class Projectile():
    def __init__(self, x, y, radius, color, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.direction = direction
        self.vel = 8 * direction

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class Enemy():
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
        self.width = width
        self.height = height
        self.end = end
        self.vel = 3
        self.walkCount = 0

    def draw(self, win):
        self.walk()
        if self.walkCount + 1 >= 33:
            self.walkCount = 0
        else:
            if
        pass

    def walk(self):
        if self.vel > 0:
            if self.vel + self.x < self.end:
                self.x += self.vel
                self.walkCount += 1
        pass



def reDrawWindow(man, bullets, win):
    # On every frame, put the bg image first
    win.blit(bg, (0, 0))
    man.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


def main():
    # x = 300
    # y = 300
    clock = pygame.time.Clock()
    man = Character(300, 300, walkLeft[0].get_size()[0], walkLeft[0].get_size()[1], 5)
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
                    # if keys[pygame.K_SPACE]:
                    facing = -1 if man.left else 1

                    if len(bullets) < 50:
                        bullets.append(
                            Projectile(round(0.5 * man.width + man.x), round(0.5 * man.height + man.y), 3,
                                       (255, 0, 0),
                                       facing))

        for bullet in bullets:
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
        reDrawWindow(man, bullets, win)
    pygame.quit()


# Start main window of the game
if __name__ == '__main__':
    main()
