from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText, Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    effects = (
        Cycle(
            screen=screen,
            renderer=Fire(height=100, width=100, emitter='X', intensity=0.5, spot=5, colours=5),
            y=int(screen.height / 2 - 8)),
        Cycle(
            screen=screen,
            renderer=FigletText('ACM @ Miami University'),
            y=int(screen.height / 2 - 6)),
        Cycle(
            screen=screen,
            renderer=FigletText('ROCKS!', font='big'),
            y=int(screen.height / 2 + 3)),
        Stars(screen=screen, count=200),
    )
    screen.play([Scene(effects)], repeat=True)

if __name__ == '__main__':
    try:
        Screen.wrapper(demo)
    except KeyboardInterrupt:
        print('You can also press `q` to exit')
