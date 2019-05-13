def executor(arg1, arg2, func=None):
    if func is None:
        return "Strategy not implemented..."
    return func(arg1, arg2)

def strategy_1(arg1, arg2):
    return f_1(arg1, arg2)

def strategy_2(arg1, arg2):
    return f_2(arg1, arg2)