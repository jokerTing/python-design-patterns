class CatchAll(object):
    def __init__(self):
        self.next_to_execute = None
    
    def execute(self, request):
        print(request)

class Function1Class(object):
    def __init__(self):
        self.next_to_execute = CatchAll()
    
    def execute(self, request):
        if '1' in request:
            print("func 1", request)
            request = "".join([x for x in request if x != '1'])
        self.next_to_execute.execute(request)

class Function2Class(object):
    def __init__(self):
        self.next_to_execute = CatchAll()
    
    def execute(self, request):
        if '2' in request:
            print("func 2", request)
            request = "".join([x for x in request if x != '2'])
        self.next_to_execute.execute(request)
    
class Function3Class(object):
    def __init__(self):
        self.next_to_execute = CatchAll()
    
    def execute(self, request):
        if '3' in request:
            print("func 3", request)
            request = "".join([x for x in request if x != '3'])
        self.next_to_execute.execute(request)

class Function4Class(object):
    def __init__(self):
        self.next_to_execute = CatchAll()
    
    def execute(self, request):
        if '4' in request:
            print("func 4", request)
            request = "".join([x for x in request if x != '4'])
        self.next_to_execute.execute(request)

def main_function(head, request):
    head.execute(request)

if __name__ == "__main__":
    hd = Function1Class()
    current = hd
    current.next_to_execute = Function2Class()

    current = current.next_to_execute
    current.next_to_execute = Function3Class()

    current = current.next_to_execute
    current.next_to_execute = Function4Class()

    main_function(hd, '12214549')