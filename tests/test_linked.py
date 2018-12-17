from algo.linked import LinkedList, LinkedListFakeNode


def test_linked_list():
    ll = LinkedList()
    ll.insert('once', -1)
    ll.insert('upon')
    ll.insert('a')
    ll.insert('time')
    assert len(ll) == 4

    ll.reverse()
    assert ll.find('a') == 2

    ll.remove(-2)
    ll.insert('b', 2)
    assert ll.find('a') == -1 and ll.find('b') == 2

    l1 = ['once', 'upon', 'b', 'time']
    i = 0
    for j in ll:
        assert j == l1[i]
        i += 1

    ll.remove(0)
    assert len(ll) == 3

    fn = LinkedListFakeNode()
    fn.insert('Mary')
    fn.insert('had')
    fn.insert('a')
    fn.insert('little')
    fn.insert('cat')
    fn.insert('.')
    fn.reverse()
    fn.remove(4)
    fn.insert('lamb', 4)
    l2 = ['Mary', 'had', 'a', 'little', 'lamb', '.']
    i = 0
    for j in fn:
        assert j == l2[i]
        i += 1

    fn.head.obj == 'Jack'
    assert fn.head.obj == 'Mary'
