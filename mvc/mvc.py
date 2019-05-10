import sys

class GenericController(object):
    def __init__(self):
        self.model = GenericModel()
        self.view = GenericView()
    
    def handle(self, request):
        data = self.model.get_data(request)
        self.view.generate_response(data)

class GenericModel(object):
    def __init__(self):
        pass
    
    def get_data(self, request):
        return {'request': request}

class GenericView(object):
    def __init__(self):
        pass
    
    def generate_response(self, data):
        print(data)

def main(name):
    request_handler = GenericController()
    request_handler.handle(name)
if __name__ == "__main__":
    main(sys.argv[1])