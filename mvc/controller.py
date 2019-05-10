import sys
from model import NameModel
from model import TimeModel
from view import GreetingView 

class GreetingController(object):
    def __init__(self):
        self.name_model = NameModel()
        self.view = GreetingView()
        self.time_model = TimeModel()
    
    def handle(self, request):
        if request in self.name_model.get_name_list():
            self.view.generate_greeting(
                name=request, 
                time_of_day=self.time_model.get_time_of_day(),
                known=True
            )
        else:
            self.name_model.save_name(request)
            self.view.generate_greeting(
                name=request, 
                time_of_day=self.time_model.get_time_of_day(),
                known=False
            )

def main(name):
    request_handler = GreetingController()
    request_handler.handle(name)

if __name__ == "__main__":
    main(sys.argv[1])