class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def print_elem(self):
        temp = self.head
        while (temp):
            print(temp.data, end='->')
            temp = temp.next
        if temp == None:
            print("Null")

    def insert_elem_after(self, elem, after_this_elem=None):
        if after_this_elem is None:
            temp = self.head
            self.head = Node(elem)
            self.head.next = temp
        else:
            temp = self.head
            while temp:
                if temp.data == after_this_elem:
                    node_after_temp = temp.next
                    temp.next = Node(elem)
                    temp.next.next = node_after_temp
                    return
                temp = temp.next

    def delete_elem_once(self, elem_tobe_del):
        if elem_tobe_del == self.head.data:
            temp = self.head.next
            self.head = None
            self.head = temp
            return
        temp = self.head.next
        prev = self.head

        while temp:
            if temp.data == elem_tobe_del:
                break
            prev = prev.next
            temp = temp.next

        if temp is None:
            print('\nType a valid input. %d is not present in the linkedlist. Proceed again.' % (elem_tobe_del))
            return

        prev.next = temp.next
        return

    def delete_elem_everyplace(self, elem_tobe_del):  # if we have to delete every node corresponding to the same value
        count = 0
        temp = self.head
        prev = None

        while True:
            while temp:
                if temp.data == elem_tobe_del:
                    count += 1
                    break
                prev = temp
                temp = temp.next

            if temp is None:
                if count == 0:
                    print('\nType a valid input. %d is not present in the linkedlist. Proceed again.' % (elem_tobe_del))
                    return
                else:
                    print('\nThe element %d was deleted %d times from the linkedlist.' % (elem_tobe_del, count))
                    return
            if prev is None:
                self.head = temp.next
            else:
                prev.next = temp.next
            temp = temp.next

        if count > 0:
            print('\nThe element %d was deleted %d times from the array.' % (elem_tobe_del, count))
        return


if __name__ == '__main__':
    my_linked_list = linkedlist()
    my_linked_list.head = Node(1)
    node2 = Node(3)
    node3 = Node(3)

    my_linked_list.head.next = node2
    node2.next = node3

    print('the linkedlist formed is:')
    my_linked_list.print_elem()

    my_linked_list.insert_elem_after(
        0)  # base condition : if the element has to inserted in the start of the linkedlist
    my_linked_list.insert_elem_after(0)
    my_linked_list.insert_elem_after(0)
    my_linked_list.insert_elem_after(5, 1)  # if the element has to be inserted in the middle of the linkedlist
    my_linked_list.insert_elem_after(5, 5)

    print('\nOur linkedlist after insertion of elements:')
    my_linked_list.print_elem()

    my_linked_list.delete_elem_once(
        0)  # base condition: if the element has to be deleted from the start of the linkedlist
    my_linked_list.delete_elem_once(5)  # deletion of an element from the linkedlist
    my_linked_list.delete_elem_once(22)  # deletion of an element from the linkedlist not present

    print('\nOur linkedlist after the deletion of elements:')
    my_linked_list.print_elem()

    my_linked_list.delete_elem_everyplace(0)  # deletion of all element from the linkedlist matching a value
    my_linked_list.delete_elem_everyplace(5)

    print('\nOur linkedlist after the MULTIPLE deletion of elements:')
    my_linked_list.print_elem()