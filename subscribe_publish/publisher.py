from xmlrpc.client import ServerProxy

class Publisher(object):
    def __init__(self, dispatcher):
        self.dispatcher = dispatcher
    
    def publish(self, message):
        with ServerProxy(self.dispatcher) as dispatch:
            dispatch.send(message)

def main():
    message = {
        "topic": "MessageTopic",
        "payload": "This is an awesome payload"
    }
    publisher = Publisher("http://localhost:9000")
    publisher.publish(message)
    
if __name__ == "__main__":
    main()