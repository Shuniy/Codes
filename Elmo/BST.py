from collections import deque

class node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

    def setLeftChild(self, node):
        self.left = node

    def setRightChild(self, node):
        self.right = node

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def hasLeftChild(self):
        return self.left != None

    def hasRightChild(self):
        return self.right != None

    def _repr_(self):
        return f"Node ({self.getValue()})"

    def _str_(self):
        return f"Node ({self.getValue()})"


class Tree(object):
    def __init__(self, value):
        self.root = None

    def getRoot(self):
        return self.root

    def setRoot(self, value):
        self.root = node(value)

    def compare(self, node, newNode):
        if newNode.getValue() == node.getValue():
            return 0
        elif newNode.getValue() < node.getValue():
            return -1
        else:
            return 1

    def insertWithLoop(self, newValue):
        newNode = node(newValue)
        node = self.getRoot()
        if node == None:
            self.root = newNode
            return
        while(True):
            comparison = self.compare(node, newNode)
            if comparison == 0:
                break
            elif comaprison == -1:
                if node.hasLeftChild():
                    node = node.getLeftChild()
                else:
                    node = setLeftChild(newNode)
                    break
            else:
                if node.hasLeftChild():
                    node = node.getRightChild()
                else:
                    node.setRightChild(newNode)
                    break
    def insertWithRecursion(self, value):
        if self.getRoot() == None:
            self.setRoot(value)
            return
        self.insertRecursively(self.getRoot(), node(value))

    def insertRecursively(self, node, newNode):
        comparison = self.comapre(node, newNode)
        if comparison == 0:
            if node.hasLeftChild():
                self.insertRecursively(node.getLeftChild(), newNode)
            elif comparison == -1:
                if node.hasLeftChild():
                    self.insertRecursively(node.getLeftChild(), newNode)
                else:
                    node.setLeftChild(newNode)
            else:
                if node.hasRightChild():
                    self.insertRecursively(node.getRightChild(), newNode)
                else:
                    node.setRightChild(newNode)

    def _repr_(self):
        level = 0
        q = Queue()
        visitOrder = list()
        node = self.getRoot()
        q.enq((node, level))
        while len(q) > 0:
            node, level = q.deq()
            if node == None:
                visitOrder.append(("<empty", level))
                continue
            visitOrder.append((node, level))
            if node.hasLeftChild():
                q.enq((node.getLeftChild(), level + 1))
            else:
                q.enq((None, level + 1))
        s = "Tree \n"
        previous_level = -1
        for i in range(len(visitOrder)):
            node, level = visitOrder[i]
            if level == previous_level:
                s += " | " + str(node)
            else:
                previous_level = level
        return s


class Queue():
    def __init__(self):
        self.q = deque()

    def enq(self, value):
        self.q.appendleft(value)

    def deq(self):
        if len(self.q) > 0:
            return self.q.pop()
        else:
            return None

    def _len_(self):
        return len(self.q)

    def _repr_(self):
        if len(self.q) > 0:
            s = "< enqueue here >\n ________________________\n"
            s += "\n______________________\n".join([str(item)
                                                    for item in self.q])
            s += "\n_______________________\n <dequeue here >"
            return s
        else:
            return "<queue is empty>"

    def search(self, value):
        node = self.getRoot()
        s_node = node(value)
        while(True):
            comparison = self.comapre(node, s_node)
            if comparison == 0:
                return True
            elif comparison == -1:
                if node.hasLeftChild():
                    node = node.getLeftChild()
                else:
                    return True
            else:
                if node.hasRightChild():
                    node = node.getRightChild()
                else:
                    return False


# If duplicates then keep track or just overwrite it
# Two methods one by loop and recursion
