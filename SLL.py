""" SLL list, to search, add, and remove
"""


class SLLNode:  # node for SLL list - data and none (Head ->)
    def __init__(self, node_data):
        self.node_data = node_data
        self.next = None

    def __repr__(self):
        """ return a string output to the console."""
        return "The Node for SLL object is: node_data={}".format(self.node_data)

    def get_node(self):
        """ return the node_data (true, false etc..."""
        return self.node_data

    def set_node(self, new_node_data):
        """ Goal is to replace the old node_data with new_node_data here"""
        return self.node_data

    def get_next_node(self):
        """ want to return (get) the self.next attribute"""
        return self.next

    def set_next_node(self, new_next_node):
        """ declare the new next self"""
        self.next = new_next_node


class SLList:
    """ Now need a class to handle, the needed functions to traverse and update node """

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "the SLList object is: head={}".format(self.head)

    """ need a add, size, search, remove functions... """

    def node_empty(self):
        """ acts like a boolean, will return true or false if a node exists..."""
        return self.head is None  # Head always point to None"""
        #  done

    def add_front(self, new_node_data):
        temp = SLLNode(new_node_data)
        temp.set_next_node(self.head)
        self.head = temp  # updating

    def size(self):
        size = 0
        if self.head is None:
            return 0

        current_state = self.head
        while current_state is not None:  # only count if there are nodes
            size += 1
            current_state = current_state.get_next_node()

        return size

    def search_node(self, node_data):
        if self.head is None:
            return "List is empty"

        current_state = self.head
        while current_state is not None:
            if current_state.get_node == node_data:
                return True
            else:
                current_state = current_state.get_next_node()

    def remove_node(self, node_data):
        if self.head is None:
            return "List is empty. no nodes to be found here LOL"

        current_state = self.head
        previous = None  # single link list do not go front and back like DLL list
        found = False
        while not found:
            if current_state.get_node() == node_data:
                found = True
            else:
                if current_state.get_next_node() == None:
                    return " A node with matching data value is not here"
                else:
                    previous = current_state
                    current_state = current_state.get_next_node()

        if previous is None:
            self.head = current_state.get_next_node()
        else:
            previous.set_next_node(current_state.get_next_node)


""" console output below...
>>> sll.search_node(10)
'List is empty'
>>> sll.add_front(10)
>>> sll.search_node(10)
>>> sll.size()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\escob\PycharmProjects\OOPs_in_Python\SLL.py", line 60, in size
    current_state = current_state.get_next_node
AttributeError: 'function' object has no attribute 'get_next_node'
>>> sll.size()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\escob\PycharmProjects\OOPs_in_Python\SLL.py", line 60, in size
    current_state = current_state.get_next_node
AttributeError: 'function' object has no attribute 'get_next_node'
>>> sll.remoce_node(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SLList' object has no attribute 'remoce_node'. Did you mean: 'remove_node'?
>>> sll.remove(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'SLList' object has no attribute 'remove'
>>> sll.remove_node(10)
>>> sll.size()
0
>>> sll.search(10)
Traceback (most recent call last):
AttributeError: 'SLList' object has no attribute 'search'
>>> sll.node_empty()
True
>>> sll.add_front(10)
>>> sll.size()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\escob\PycharmProjects\OOPs_in_Python\SLL.py", line 60, in size
    current_state = current_state.get_next_node
AttributeError: 'function' object has no attribute 'get_next_node'
>>> exit
Use exit() or Ctrl-Z plus Return to exit
>>> exit()
PS C:\Users\escob\PycharmProjects\OOPs_in_Python> python3 -i SLL.py
>>> sll.add_front(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sll' is not defined. Did you mean: 'all'?
>>> sll = SLList()
>>> sll.add_front(10)
>>> sll.add_front(20)
>>> sll.add_front(30)
>>> sll.add_front(40)
>>> sll.size()
4
>>> sll.search_node(30)
>>> sll.size()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\escob\PycharmProjects\OOPs_in_Python\SLL.py", line 60, in size
    current_state = current_state.get_next_node()  # forgot parenthesis
AttributeError: 'function' object has no attribute 'get_next_node'
>>> sll.size()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\escob\PycharmProjects\OOPs_in_Python\SLL.py", line 60, in size
    current_state = current_state.get_next_node()
AttributeError: 'function' object has no attribute 'get_next_node'
>>> exit()
PS C:\Users\escob\PycharmProjects\OOPs_in_Python> python3 -i SLL.py
>>> sll = SLList()
>>> sll.size()
0
>>> Sll.add_node(10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Sll' is not defined. Did you mean: 'sll'?
>>> sll.add_front(10)
>>> sll.size()
1
>>> sll.add_front(20)
>>> sll.size()
2
>>> sll.add_front(30)
>>> sll.add_front(40)
>>> sll.add_front(50)
>>> sll.add_front(60)
>>> sll.size()
6
>>> sll.search_node(30)
>>> sll.remove_node(60)
>>> sll.size()
5
>>> works fine, missing some print statement for search but that is fine...

"""