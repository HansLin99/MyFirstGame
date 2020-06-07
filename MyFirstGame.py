import pygame

# Main Character Class
class Character():
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

    def draw(self):
        pass


class Projectile():
    def __init__(self, x, y, radius, vel, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel = vel
        self.direction = direction

def main():
    pygame.init()

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
    bg = pygame.image.load("Game/bg.jpg")
    stand = pygame.image.load("Game/standing.png")

    # x = 300
    # y = 300
    screenWidth = 800
    screenHeight = 480
    clock = pygame.time.Clock()
    man = Character(300, 300, walkLeft[0].get_size()[0], walkLeft[0].get_size()[1], 5)
    bullets= []


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
        keys = pygame.key.get_pressed()

        # These conditions respond to user key pressed
        if keys[pygame.K_LEFT] and man.x > man.vel:
            man.x -= man.vel
            man.left = True
        if keys[pygame.K_RIGHT] and man.x < screenWidth - man.vel - man.width:
            man.x += man.vel
            man.right = True
        if not man.isJump:
            if keys[pygame.K_UP]:
                man.isJump = True
        else:
            if man.jumpCount >= -10:
                neg = 1
                if man.jumpCount <= 0:
                    neg = -1
                man.y -= (man.jumpCount ** 2) * 0.5 * neg
                man.jumpCount -= 1
            else:
                man.isJump = False
                man.jumpCount = 10
        # On every frame, put the bg image first
        win.blit(bg, (0, 0))

        # Based on the steps the man has walked, put the corresponding image onto the window
        # * Face to the direction which he stopped
        if man.walkCount + 1 >= 27:
            man.walkCount = 0
        if not man.moving:
            if man.left:
                win.blit(walkLeft[0], (man.x, man.y))
            elif man.right:
                win.blit(walkRight[0], (man.x, man.y))
            else:
                win.blit(stand, (man.x, man.y))
        else:
            if man.left:
                win.blit(walkLeft[man.walkCount // 3], (man.x,man.y))
                man.walkCount +=1
                man.moving = True
            elif man.right:
                win.blit(walkRight[man.walkCount // 3], (man.x, man.y))
                man.walkCount += 1
                man.moving = True
            # else:
            #     if man.left:
            #         win.blit(walkLeft[0], (man.x, man.y))
            #     else:
            #         win.blit(walkRight[0], (man.x, man.y))

        pygame.display.update()
        man.left = False
        man.right = False

    pygame.quit()


#Start main window of the game
if __name__ == '__main__':
    main()

