class Node:
    def __init__(self, value,favorite):
        self.value = value
        self.favorite = favorite
        print(value)

    def print_value(self):
        print(f'Value is: {self.value}')

    def print_double(self):
        print(self.favorite)
n = Node(10)
n.print_value()
