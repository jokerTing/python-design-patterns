class NonTerminal(object):
    def __init__(self, expression):
        self.expression = expression
    
    def interpret(self):
        self.expression.interpret()

class Terminal(object):
    def interpret(self):
        pass