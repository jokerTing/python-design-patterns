import base64
from pprint import PrettyPrinter
pp = PrettyPrinter(indent=4)
#uwsgi --http :9090 --wsgi-file hello_world_server.py

class User(object):
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = password
        self.name = name
        self.email = email

    @classmethod
    def get_verified_user(cls, username, password):
        return User(
            username,
            password,
            username,
            "{}@demo.com".format(username)
        )

#chain mode
class EndHandler(object):
    def __init__(self):
        pass
    
    def handle_request(self, request, response=None):
        return response.encode("utf-8")

class AuthorizationHandler(object):
    def __init__(self):
        self.next_handler = EndHandler()

    def handle_request(self, request, response=None):
        authorization_header = request["HTTP_AUTHORIZATION"]
        header_array = authorization_header.split()
        encoded_string = header_array[1]
        decoded_string = base64.standard_b64decode(encoded_string).decode('utf-8')
        print("AuthorizationHandler->handle_request", decoded_string)
        username, password = decoded_string.split(":")
        request['username'] = username
        request['password'] = password

        return self.next_handler.handle_request(request, response)

class UserHandler(object):
    def __init__(self):
        self.next_handler = EndHandler()

    def handle_request(self, request, response=None):
        user = User.get_verified_user(
            request['username'],
            request['password'])
        request['user'] = user
        return self.next_handler.handle_request(request, response)
    
class PathHandler(object):
    def __init__(self):
        self.next_handler = EndHandler()
    
    def handle_request(self, request, response=None):
        path = request["PATH_INFO"].split("/")
        if "goodbye" in path:
            response = "GoodBye {}!".format(request['user'].name)
        else:
            response = "Hello {}!".format(request['user'].name)
        return self.next_handler.handle_request(request, response)

def application(env, start_response):
    #pp.pprint(env)
    head = AuthorizationHandler()
    current = head
    current.next_handler = UserHandler()
    current = current.next_handler
    current.next_handler = PathHandler()

    start_response('200 OK', [('Content-Type', 'text/html')])    
    return [head.handle_request(env)]
