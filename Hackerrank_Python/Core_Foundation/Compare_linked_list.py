def compare_lists(llist1, llist2):
    # Traverse both lists until at least one reaches the end
    while llist1 is not None and llist2 is not None:
        # If data doesn't match, the lists are not equal
        if llist1.data != llist2.data:
            return 0
        
        # Move to the next nodes
        llist1 = llist1.next
        llist2 = llist2.next
    
    # If both are None, they are equal in length and data.
    # If one is not None, one list was longer than the other.
    if llist1 is None and llist2 is None:
        return 1
    else:
        return 0
