import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))
COLOR_INACTIVE = pg.Color(127, 127, 127, 255)
COLOR_ACTIVE = pg.Color('dodgerblue2')
font_size = 20
FONT = pg.font.Font(None, font_size)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = ['', '', '', '']
        self.label = []
        for line in range(len(self.text)):
            self.label.append(FONT.render(self.text[line], True, self.color))
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False
        self.current_line = 0

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    # self.text = ''
                    self.current_line += 1
                    self.current_line = self.current_line % 4
                elif event.key == pg.K_BACKSPACE:
                    self.text[self.current_line] = self.text[self.current_line][:-1]
                else:
                    self.text[self.current_line] += event.unicode
                # Re-render the text.
                for line in range(len(self.text)):
                    self.label[line] = FONT.render(self.text[line], True, self.color)


    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.es
        # for line in range(len(self.label)):
        #     screen.blit(self.label[line], (self.rect.x+5, self.rect.y+5 + font_size*line))
        screen.blit(self.label[0], (self.rect.x+5, self.rect.y+5 + font_size * 0))
        screen.blit(self.label[1], (self.rect.x + 5, self.rect.y + 5 + font_size * 1))
        screen.blit(self.label[2], (self.rect.x + 5, self.rect.y + 5 + font_size * 2))
        screen.blit(self.label[3], (self.rect.x + 5, self.rect.y + 5 + font_size * 3))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)



def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 280, 80)
    # input_box2 = InputBox(100, 300, 280, 80)
    input_boxes = [input_box1]
    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()