""" Analizar  el  código  del  programa    pilas_tp.py    Identificar  la  clase,  los  métodos. 
Agregar los métdodos: 
- Eliminar un elemento 
- Visualizar la pila  como pila """

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop(self):
        if self.is_empty():
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data

    def display(self):
        current = self.head
        stack_values = []
        while current:
            stack_values.append(str(current.data))
            current = current.next
        print("Stack:")
        for value in reversed(stack_values):
            print("|", value, "|")
        print("-------")
    
    ########################################
    def eliminar_elemento(self, data):
        if self.is_empty():
            return None
        elif self.head.data == data:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None and current.next.data != data:
                current = current.next
            if current.next is not None:
                current.next = current.next.next
    ########################################
    
    
    def visualizar_pila(self):
        current = self.head
        stack_values = []
        while current:
            stack_values.append(str(current.data))
            current = current.next
        print("Stack:")
        for value in stack_values:
            print("|", value, "|")
        print("-------")
    ########################################
    

stack = Stack()
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(8)
stack.push(2)
stack.display()
stack.visualizar_pila()
stack.eliminar_elemento(10)
stack.visualizar_pila()