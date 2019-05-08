def reducer(arg1, arg2, strategy=None):
    if strategy == "addition":
        print(arg1 + arg2)
    elif strategy == "subtraction":
        print(arg1 - arg2)
    else:
        print("Strategy not implemented...")

def main():
    reducer(4, 6)
    reducer(4, 6, "addition")
    reducer(4, 6, "subtraction")

if __name__ == "__main__":
    main()