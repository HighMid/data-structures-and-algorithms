from data_structures.queue import Queue


class AnimalShelter:
    def __init__(self):
        self.animals = Queue()

    def enqueue(self, animal):
        
        if isinstance(animal, Dog) or isinstance(animal, Cat):
            self.animals.enqueue(animal)

    def dequeue(self, pref):
        if pref not in ["dog", "cat"]:
            return None

        temp_queue = Queue()
        found_animal = None

        while not self.animals.is_empty():
            animal = self.animals.dequeue()
            if not found_animal and animal.species == pref:
                found_animal = animal
            else:
                temp_queue.enqueue(animal)

        while not temp_queue.is_empty():
            self.animals.enqueue(temp_queue.dequeue())

        return found_animal

class Dog:
    
   def __init__(self):
       self.species = "dog"
        
    
class Cat:
    def __init__(self):
        self.species = "cat"
