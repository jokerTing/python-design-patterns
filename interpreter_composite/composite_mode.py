class Leaf(object):
    def __init__(self, *args, **kwargs):
        pass
    
    def component_function(self):
        print("Leaf")

class Composite(object):
    def __init__(self, *args, **kwargs):
        self.children = []

    def component_function(self):
        for child in self.children:
            child.component_function()
    
    def add(self, child):
        self.children.append(child)
    
    def remove(self, child):
        self.children.remove(child)
