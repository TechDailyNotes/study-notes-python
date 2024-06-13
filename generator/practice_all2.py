def gen(num):
    while num > 0:
        yield num
        num -= 1


g = gen(5)
print(f"next(g) = {next(g)}")
print(f"g.send(None) = {g.send(None)}")
for i in g:
    print(i)


def gen2(num):
    while num > 0:
        tmp = yield num
        if tmp is not None:
            num = tmp
        num -= 1


g2 = gen2(5)
# print(f"next(g2) = {next(g2)}")
print(f"g2.send(None) = {g2.send(None)}")
print(f"g2.send(10) = {g2.send(10)}")
for i in g2:
    print(i)


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next


node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)
