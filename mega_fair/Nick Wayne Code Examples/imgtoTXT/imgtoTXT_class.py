import pygame
import os


def main():
    pygame.init()
    pygame.font.init()
    font_size = 3
    my_font = pygame.font.SysFont('Courier New', font_size)
    done = False
    size = (600, 600)  # Width and height of the window
    screen = pygame.display.set_mode(size)
    active_resolution = (150, 150)
    path = "C:\Users\Nicholas Wayne\Desktop\TEST"
    frame = 0
    frame_count = 1000
    # images = []
    # for file in os.listdir(path):
    #     if file.endswith(".jpg"):
    #         images.append((pygame.image.load(path + "\\" + file), []))
    # print images

    def run_set(image):
        SIZE = (image.get_width(), image.get_height())
        canvas = pygame.Surface(SIZE)
        canvas.blit(image, (0, 0))
        colors = []


        total = 0
        # print SIZE
        x = SIZE[0] // active_resolution[0]
        y = SIZE[1] // active_resolution[1]
        resolution = (SIZE[0] - x * active_resolution[0], SIZE[1] - y * active_resolution[1])
        avg_count = x * y
        for j in range(resolution[1]):
            colors.append([])
            for h in xrange(resolution[0]):
                total = 0
                for g in range(y):
                    for i in range(x):
                        # print j, h, g, i
                        # print (g + (y * j), i + (x * h))
                        # print conbright(tuple(canvas.get_at((g + (y*j), i + (x*h)))))
                        # print "\n"
                        total += conbright(tuple(canvas.get_at((i + (x*h), g + (y*j)))))
            # print total, avg_count
                colors[j].append(total/avg_count)



        # for i in range(SIZE[1]):
        #     colors.append([])
        #     for g in range(SIZE[0]):
        #         colors[i].append(conbright(tuple(canvas.get_at((g, i)))))
        # print colors


        return display(colors)

    def reload_font(b, font_size):
        if b:
            font_size += 1
            my_font = pygame.font.SysFont('Courier New', font_size)
        else:
            font_size -= 1
            my_font = pygame.font.SysFont('Courier New', font_size)
        return my_font, font_size

    def conbright(color):
        return 0.2126*color[0] + 0.7152*color[1] + 0.0722*color[2]

    def clamp(value):
        if 230 < value <= 256:
            return "7"
        if 200 < value <= 230:
            return "7"
        if 170 < value <= 200:
            return "6"
        if 140 < value <= 170:
            return "5"
        if 110 <= value <= 140:
            return "4"
        if 80 <= value <= 110:
            return "3"
        if 50 <= value <= 80:
            return "2"
        if 0 <= value <= 50:
            return "1"

    def switch(value):
        return {
            "1": "@",
            "2": "$",
            "3": "&",
            "4": "#",
            "5": "*",
            "6": "^",
            "7": "'"
        }[value]

    def display(bright):
        f = open("test.txt", "w")
        # x = SIZE[0] // active_resolution[0]
        # y = SIZE[1] // active_resolution[1]
        # images = []
        # for j in y:
        #     images.append([])
        #     for h in x:
        #         images[j].append([])
        #         for g in range(active_resolution[1]):
        #             for i in range(active_resolution[0]):

        text_lst = []
        text = ""
        for i in bright:
            for g in i:
                text += switch(clamp(g))
                text += " "
                f.write(switch(clamp(g)))
            text_lst.append(text)
            text = ""
            f.write("\n")
        f.close()
        return text_lst

    # for i in range(SIZE[1]):
    #     colors.append([])
    #     for g in range(SIZE[0]):
    #         colors[i].append(conbright(tuple(canvas.get_at((g,i)))))
    #
    # print "Thinking..."
    # text = display(colors)
    # print "All DONE!!!"

    print "thinking"
    texts = []
    for i in range(100,150):
        texts.append(run_set(pygame.image.load(path + "\\" + "testing%04d.jpg"%(i))))
        print i

    print "done"

    while not done:
        pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:  # Escape to close program
                    done = True

                if event.key == pygame.K_f:  # Escape to close program
                    frame += 1
                    print frame

                if event.key == pygame.K_g:  # Escape to close program
                    frame += 10
                    print frame

                if event.key == pygame.K_r:  # Escape to close program
                    my_font, font_size = reload_font(True, font_size)

                if event.key == pygame.K_t:  # Escape to close program
                    my_font, font_size = reload_font(False, font_size)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    frame += 1
                    print frame

        screen.fill((0, 0, 0))
        for j,i in enumerate(texts[frame]):
            font_render = my_font.render(i,False, (255, 255, 255))
            screen.blit(font_render, (0, j*font_size))
        # frame += 1
        pygame.display.flip()


pygame.quit()

if __name__ == '__main__':
    main()
