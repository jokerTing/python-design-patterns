'''
def text_writer(string1, string2):
    print("Writing {} - {}".format(string1, string2))
'''
class Invoker(object):
    def __init__(self):
        self.commands = []

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        for cmd in self.commands:
            #cmd.execute()
            cmd["function"](*cmd["params"])

if __name__ == "__main__":
    text_writer = lambda string1, string2: print("Writing {} - {}".format(string1, string2))
    invoker = Invoker()
    invoker.add_command({
        "function": text_writer,
        "params": ("cmd1", "string 1")
    })
    invoker.add_command({
        "function": text_writer,
        "params": ("cmd2", "string 2")
    })
    invoker.run()