def get_append_write(filename):
    if os.path.exists(filename):
        return 'a'
    return 'w'

def read_names(filename):
    with open(filename, 'r') as data_file:
        names = data_file.read().split('\n')
    return names
    
def write_name(filename, name):
    with open(filename, get_append_write(filename)) as data_file:
        data_file.write("{}\n".format(name))