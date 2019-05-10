import sys
import os

def get_append_write(filename):
    if os.path.exists(filename):
        return 'a'
    return 'w'

def name_in_file(filename, name):
    if not os.path.exists(filename):
        return False
    return name in read_names(filename)

def read_names(filename):
    with open(filename, 'r') as data_file:
        names = data_file.read().split('\n')
    return names

def write_name(filename, name):
    with open(filename, get_append_write(filename)) as data_file:
        data_file.write("{}\n".format(name))

def get_message(name):
    if name_in_file('names.dat', name):
        return "Welcome back {}!".format(name)
    write_name('names.dat', name)
    return "Hi {}, it is good to meet you".format(name)

def main(name):
    print(get_message(name))

if __name__ == "__main__":
    main(sys.argv[1]) 