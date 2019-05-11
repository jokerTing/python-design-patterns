from xmlrpc.client import ServerProxy
from xmlrpc.server import SimpleXMLRPCServer

class Dispatcher(SimpleXMLRPCServer):
    def __init__(self):
        self.topic_subscribers = dict()
        super(Dispatcher, self).__init__(("localhost", 9000))
        print("Listening on port 9000")
     
        self.register_function(self.subscribe, "subscribe")
        self.register_function(self.unsubscribe, "unsubscribe")
        self.register_function(self.unsubscribe_all, "unsubscribe_all")
        self.register_function(self.send, "send")
    
    def subscribe(self, subscriber, topic):
        print('Subscribing {} to {}'.format(subscriber, topic))
        self.topic_subscribers.setdefault(topic, set()).add(subscriber)
        return "OK"
    
    def unsubscribe(self, subscriber, topic):
        print('Unsubscribing {} to {}'.format(subscriber, topic))
        self.topic_subscribers.setdefault(topic, set()).discard(subscriber)
        return "OK"


    def unsubscribe_all(self, topic):
        print('Unsubscribing all {}'.format(topic))
        self.subscribers = self.topic_subscribers[topic] = set()
        return "OK"
    
    def send(self, message):
        print("Sending Message:\nTopic: {}\nPayload: {}".format(
            message["topic"], message["payload"]))
        
        for subscriber in self.topic_subscribers[message.get("topic", "all")]:
            with ServerProxy(subscriber) as subscriber_proxy:
                subscriber_proxy.process(message)
        return "OK"

def main():
    dispatch_server = Dispatcher()
    dispatch_server.serve_forever()

if __name__ == "__main__":
    main()

'''
Subscribing http://localhost:9001 to MessageTopic
127.0.0.1 - - [11/May/2019 13:10:51] "POST /RPC2 HTTP/1.1" 200 -
Sending Message:
Topic: MessageTopic
Payload: This is an awesome payload
'''