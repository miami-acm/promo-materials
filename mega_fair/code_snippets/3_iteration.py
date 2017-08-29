from collections import namedtuple

Point = namedtuple('Point', 'x, y')

points_of_a_triangle = (
    Point(x=1, y=3),
    Point(x=4, y=5),
    Point(x=3, y=0)
)

for x_coordinate, y_coordinate in points_of_a_triangle:
    print(f'X Coordinate {x_coordinate}')
    print(f'Y Coordinate {y_coordinate}')
    print()
