from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

class Subscriber(SimpleXMLRPCServer):
    def __init__(self, dispatcher, topic):
        super(Subscriber, self).__init__(("localhost", 9001))
        print("Listeing on port 9001...")
        self.register_function(self.process, "process")
        #self.register_function(self.subscribe, "subscribe")
        self.subscribe(dispatcher, topic)
    
    def subscribe(self, dispatcher, topic):
        with ServerProxy(dispatcher) as dispatch:
            dispatch.subscribe("http://localhost:9001", topic)
    
    def process(self, message):
        print("Message: {}".format(message.get("payload", "Default message")))
        return "OK"

def main():
    subscriber_server = Subscriber("http://localhost:9000", "MessageTopic")
    subscriber_server.serve_forever()

if __name__ == "__main__":
    main()

'''
Listeing on port 9001...
Message: This is an awesome payload
127.0.0.1 - - [11/May/2019 13:12:28] "POST /RPC2 HTTP/1.1" 200 -
'''