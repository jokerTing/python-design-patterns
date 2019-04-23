class User:
    def __init__(self, name, info={}):
        self.name = name
        self.info = info

    def __getattr__(self, item):
        print("get->"+item)
        return self.info[item]

    #def __getattribute__(self, item):
    #    return "getattribute item"

if __name__ == "__main__":
    user = User("tom", info={"name":"12345678901", "age":20})
    print(user.name)
    print(user.age)