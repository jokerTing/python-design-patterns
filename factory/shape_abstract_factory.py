import abc
import pygame
from shape_factory import Circle, Square

class AbstractFactory(object):
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod
    def make_object(self):
        return 

class CircleFactory(AbstractFactory):
    def make_object(self):
        # do something
        return Circle(100, 100)
    
class SquareFactory(AbstractFactory):
    def make_object(self):
        return Square(100, 100)


def draw_function(factory):
    drawable = factory.make_object()
    drawable.draw()

def prepare_client():
    squareFactory = SquareFactory()
    draw_function(squareFactory)

    circleFactory = CircleFactory()
    draw_function(circleFactory)

if __name__ == "__main__":
    windows_dimensions = 800, 600
    screen = pygame.display.set_mode(windows_dimensions)
    player_quits = False
    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True
        screen.fill((0, 0, 0))
        prepare_client()
        pygame.display.flip()