class State(object):
    pass

class ConcreteState1(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
    
    def switch_state(self):
        self.state_machine.state = self.state_machine.state2

class ConcreteState2(State):
    def __init__(self, state_machine):
        self.state_machine = state_machine
    
    def switch_state(self):
        self.state_machine.state = self.state_machine.state1
    
class StateMachine(object):
    def __init__(self):
        self.state1 = ConcreteState1(self)
        self.state2 = ConcreteState2(self)
        self.state = self.state1
    
    def switch(self):
        self.state.switch_state()

    def __str__(self):
        return str(self.state)
    
def main():
    state_machine = StateMachine()
    print(state_machine)

    state_machine.switch()
    print(state_machine)

if __name__ == "__main__":
    main()