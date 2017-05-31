import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False

White = (255, 255, 255)
Black = (0, 0, 0)

class Game:
    def __init__(self): # khoi tao cho doi tuong trong game. # self chay mot ham laf tu co tham so
        pass
        # print("Intialize")
        # pass # de deff khong bi loi viet pass
        # self.map_width = 4
        # self.map_height = 4
        # width and height
    def console_draw(self):
        #draw in console
        for y in range (self.map.height):
            for x in range(self.map.width):
                if y == self.dest.y and x == self.dest.x:
                    print(" D ", end ="")
                elif y == self.box.y and x == self.box.x:
                    print(" B ", end ="")
                elif y == self.pusher.y and x == self.pusher.x:
                    print(" P ", end ="")
                else:
                    print(" - ", end = "")
            print()

    def draw_image_center(self, object, screen):
        pixel = 64

        w = (pixel - object.image.get_width()) / 2 + object.x * pixel
        h = (pixel - object.image.get_height()) / 2 + object.x * pixel
        screen.blit(object.image, (w, h))

    def draw(self):
        pixel = 64
        for y in range(self.map.height):
            for x in range(self.map.width):
                screen.blit(ground_image, (x * pixel, y * pixel))

        # screen.blit(box_image,(self.box.x * pixel , self.box.y * pixel))
        # screen.blit(pusher_image,(self.pusher.x * pixel , self.pusher.y * pixel))
        # screen.blit(dest_image,(self.dest.x * pixel , self.dest.y * pixel))
        self.draw_image_center(self.pusher, screen)
        self.draw_image_center(self.box, screen)
        self.draw_image_center(self.dest, screen)




# chu y chinh ve cung mot he toa do

class Command():
    def __init__(self, dx, dy):
        self.x = dx
        self.y = dy

    def move(self, dx, dy):
        dx = 0
        dy = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    dx = -1
                if event.key == pygame.K_LEFT:
                    dx = 1
                if event.key == pygame.K_DOWN:
                    dy = -1
                if event.key == pygame.K_UP:
                    dy = 1


        self.move(self.pusher, dx, dy)
        self.move(self.box, dx, dy)



class Map:
    def __init__(self, w, h):
        self.width = w
        self.height = h


class Pusher:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Box:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Dest:
    def __init__(self, x, y):
        self.x = x
        self.y = y

sokoban = Game() # mot doi tuong object duoc sinh ra la sokoban trong class game
# object = Class() tao object thuoc kieu class

sokoban.map = Map(5, 5)
sokoban.pusher = Pusher (1, 1)
sokoban.box = Box(2, 2)
sokoban.dest = Dest(3, 3)
sokoban.console_draw()

# sokoban.map.width = 5
# sokoban.map2 = Map(5, 5)
#object.__attribute

# print(sokoban.map2.width, sokoban.map2.height)

# print(sokoban.map.width, sokoban.map.height)

pygame.init()
screen = pygame.display.set_mode((640, 640))
done = False
box_image = pygame.image.load("images/box.png")
pusher_image = pygame.image.load("images/pusher.png")
ground_image = pygame.image.load("images/ground.png")
dest_image = pygame.image.load("images/dest.png")

sokoban.box.image = box_image
sokoban.pusher.image = pusher_image
sokoban.dest.image = dest_image




while not done:
    dx = 0
    dy = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    sokoban.draw()
    pygame.display.flip()


    sokoban.pusher.x += dx
    sokoban.pusher.y += dy