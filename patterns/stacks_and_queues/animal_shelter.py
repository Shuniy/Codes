"""
Animal Shelter: An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first 
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter, 
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of 
that type). They cannot select which specific animal they would like. Create the data structures to 
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, 
and dequeueCat. You may use the built-in Linkedlist data structure. 
"""
# first approach is to create one class and then put all the methods in it
# however the dequeany and enqueueany is easy
# we still have to iterate for dog and cat

# other approach is to create queue for cats and dogs seperately
# then make universal class for that

class Animal:
    def __init__(self, name) -> None:
        self.order = 0
        self.name = name
    
    def getOrder(self):
        return self.order

    def setOrder(self, order):
        self.order = order 

    # compare and return for older animal
    def isOlderAnimal(self, animal):
        return self.order < animal.order

class AnimalQueue:
    def __init__(self) -> None:
        self.order = 0
        self.dogs = LinkedList()
        self.cats = LinkedList()

    def enqueue(self, animal):
        animal.setOrder(self.order)
        self.order += 1

        if animal.instance(self.dog):
            self.dogs.insertAtEnd(animal)
        else:
            self.cats.insertAtEnd(animal)

    def dequeAny(self):
        if (self.dogs.size() == 0):
            return self.dequeCats()
        elif (self.cats.size() == 0):
            return self.dequeDogs()
        else:
            dog = self.dogs.peek()
            cat = self.cats.peek()

            if dog.isOlderThan(cat):
                return self.dequeDogs()
            else:
                return self.dequeCats()

    def dequeDogs(self):
        return self.dogs.poll()

    def dequeCats(self):
        return self.cats.poll()


    
