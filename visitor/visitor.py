import abc

class Visitable(object):
    def accept(self, visitor):
        visitor.visit(self)
    
class CompositeVisitable(Visitable):
    def __init__(self, iterable):
        self.iterable = iterable
    
    def accept(self, visitor):
        for element in self.iterable:
            element.accept(visitor)
        visitor.visit(self)

class ConcreteVisitable(Visitable):
    def __init__(self):
        pass

class AbstractVisitor(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def visit(self, element):
        raise NotImplementedError("A visitor needs to define a visit method")

class ConcreteVisitor(AbstractVisitor):
    def visit(self, element):
        pass