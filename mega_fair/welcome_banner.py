# This file has been modified from its original form

# Copyright 2016 Peter Brittain
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from random import randint, choice

from asciimatics.effects import Cycle
from asciimatics.effects import Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, \
    PalmFirework
from asciimatics.renderers import FigletText, Rainbow
from asciimatics.renderers import Fire
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def demo(screen):
    scenes = []
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
    scenes.append(Scene(effects, duration=50))

    effects = (
        Print(screen=screen,
              renderer=Fire(screen.height, 80, '*' * 70, 0.8, 60, screen.colours,
                            bg=screen.colours >= 256),
              y=0,
              speed=1,
              transparent=False),
        Print(screen=screen,
              renderer=FigletText('Python', font='banner3'),
              y=(screen.height - 4) // 2,
              colour=Screen.COLOUR_BLACK,
              speed=1,
              start_frame=30,
              stop_frame=50),
        Print(screen=screen,
              renderer=FigletText('is', font='banner3'),
              y=(screen.height - 4) // 2,
              colour=Screen.COLOUR_BLACK,
              speed=1,
              start_frame=50,
              stop_frame=70),
        Print(screen=screen,
              renderer=FigletText('Awesome!', font='banner3'),
              y=(screen.height - 4) // 2,
              colour=Screen.COLOUR_BLACK,
              speed=1,
              start_frame=70),
    )
    scenes.append(Scene(effects, duration=100))

    effects = [Stars(screen, screen.width)]
    for _ in range(20):
        fireworks = [
            (PalmFirework, 25, 30),
            (PalmFirework, 25, 30),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (StarFirework, 25, 35),
            (RingFirework, 20, 30),
            (SerpentFirework, 30, 35),
        ]
        firework, start, stop = choice(fireworks)
        effects.append(
            firework(screen,
                     randint(0, screen.width),
                     randint(screen.height // 8, screen.height * 3 // 4),
                     randint(start, stop),
                     start_frame=randint(0, 250)))

    effects.append(Print(screen,
                         Rainbow(screen, FigletText("Join our")),
                         screen.height // 2 - 6,
                         speed=1,
                         start_frame=100))
    effects.append(Print(screen,
                         Rainbow(screen, FigletText("club!")),
                         screen.height // 2 + 1,
                         speed=1,
                         start_frame=100))
    scenes.append(Scene(effects, duration=150))

    screen.play(scenes, repeat=True)

if __name__ == '__main__':
    try:
        Screen.wrapper(demo)
    except KeyboardInterrupt:
        print('You can also press `q` to exit')
