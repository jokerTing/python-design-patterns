def get_message(name):
    if name_in_file('names.dat', name):
        return "Welcome back {}!".format(name)
    write_name('names.dat', name)
    return "Hi {}, it is good to meet you".format(name)

def name_in_file(filename, name):
    if not os.path.exists(filename):
        return False
    return name in read_names(filename)

if __name__ == "__main__":
    main(sys.argv[1])