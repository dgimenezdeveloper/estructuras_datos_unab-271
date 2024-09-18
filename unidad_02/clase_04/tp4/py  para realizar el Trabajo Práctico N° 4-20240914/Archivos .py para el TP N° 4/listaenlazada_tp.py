class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        new_node = Node(data) 
        if self.is_empty() or self.head.data >= data: 
            new_node.next = self.head # El nuevo nodo se enlaza con la cabeza de la lista
            self.head = new_node # La cabeza de la lista es el nuevo nodo
        else:
            current = self.head # Se guarda la cabeza de la lista en un nodo auxiliar
            while current.next is not None and current.next.data < data: 
                current = current.next # Se recorre la lista hasta encontrar el lugar donde se debe insertar el nuevo nodo
            new_node.next = current.next # El nuevo nodo se enlaza con el nodo siguiente al nodo actual
            current.next = new_node # El nodo actual se enlaza con el nuevo nodo

    def display(self):
        if self.is_empty():
            print("Linked list is empty")
        else:
            current = self.head
            while current:
                print(f"|{current.data}| -> ", end="")
                current = current.next
            print("None")
            
    
# Example usage of LinkedList class
my_list = LinkedList()

# Append elements to the linked list
my_list.append(10)
my_list.append(70)
my_list.append(30)
my_list.append(35)

# Display the linked list
my_list.display()


