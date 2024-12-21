from graphics import *
import random


def main():
    global win
    win = GraphWin("Title", 1200, 700, autoflush=False)
    win.setBackground('white')
    objects = []
    bat = drawImage(800, 300, 'HalloweenBat.png')
    witch = drawImage(-500, 300, 'WitchOnBroom.png')
    cloud1 = drawImage(100, -450, 'GrayCloud.png')
    cloud2 = drawImage(500, -525, 'GrayCloud.png')
    objects.append(bat)
    raindrops = []
    for i in range(74):
        rain = drawImage(random.randint(0, 1200), random.randint(-100, 700), 'Raindrop.png')
        raindrops.append(rain)
    over = False
    shapeWeather()
    while not over:
        key = win.checkKey()
        if key == "x":
            over = True
        for image in objects:
            bat.move(random.randint(-2, 6), random.randint(-6, 2))
            witch.move(6, 0)
            update(60)
        for rain in raindrops:
            if rain.getAnchor().getY() < 750:
                rain.move(0, random.randint(3, 10))
            else:
                rain.move(0, random.randint(-900, -800))

def drawImage(x, y, file):
    image = Image(Point(x, y), file)  # load in the image file to the location
    image.draw(win)  # draw on the screen
    return image


def drawCircle(x, y, radius, color):
    image = Circle(Point(x, y), radius)
    image.setFill(color)
    image.draw(win)
    return image


def shapeWeather():
    sun1 = drawCircle(1200, 0, 100, 'orange')
    sun2 = drawCircle(1200, 0, 90, 'yellow')
    rainbow = drawImage(1300, 250, 'Rainbow.png')


main()
