class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class MyTree(object):
    def __init__(self, root):
        self.root = root
    
    #左枝小 右枝大
    def add_node(self, node):
        current = self.root

        while True:
            if node.data <= current.data:
                if current.left is None:
                    current.left = node
                    return 
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return 
                else:
                    current = current.right
    
    def __iter__(self):
        if self.root is None:
            self.stack = []
        else:
            self.stack = [self.root]
            current = self.root
            while current.left is not None:
                current = current.left
                self.stack.append(current)
        return self
    
    def __next__(self):
        if len(self.stack) <= 0:
            raise StopIteration
        
        while len(self.stack) > 0:
            current = self.stack.pop()
            data = current.data

            if current.right is not None:
                current = current.right
                self.stack.append(current)

                while current.left is not None:
                    current = current.left
                    self.stack.append(current)
            return data
        raise StopIteration
    
if __name__ == "__main__":
    tree = MyTree(Node(16))
    tree.add_node(Node(8))
    tree.add_node(Node(1))
    tree.add_node(Node(17))
    tree.add_node(Node(13))
    tree.add_node(Node(14))
    tree.add_node(Node(9))
    tree.add_node(Node(10))
    tree.add_node(Node(11))
    
    
    print([x for x in tree])
    print("maximum value: {}".format(max(tree)))
    print("total of value: {}".format(sum(tree)))