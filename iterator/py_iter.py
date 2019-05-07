class MyList(object):
    def __init__(self, *args):
        self.list = list(args)
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            self.index += 1
            return self.list[self.index -1]
        except IndexError:
            raise StopIteration()

if __name__ == "__main__":
    my_list = MyList(1, 2, 3, 4, 5, 6)
    for i in my_list:
        print(i)