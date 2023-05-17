################################################################################
########          A program that creates a zoo and adds animals         ########
################################################################################

class Zoo:
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_lion(self,name):
        self.animals.append(Lion(name))

    def add_tiger(self,name):
        self.animals.append(Tiger(name))

    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()


class Animal:
    def __init__(self, name, age, health_level, happiness_level):
        self.name = name
        self. age = age
        self.health_level = health_level
        self.happiness_level = happiness_level

    def feed(self):
        self.health_level += 10
        self.happiness_level += 10

    def display_info(self):
        print(f"animal name is: {self.name}\n current health: {self.health_level}\n current happiness: {self .happiness_level}")


class Lion(Animal):
    def __init__(self, name, age=5, health_level = 100, happiness_level = 80, aggression_level = 0):
        super().__init__(name, age, health_level, happiness_level)
        self.aggression_level = aggression_level

    def feed(self):
        self.health_level += 20
        self.happiness_level += 30
        return self
    
    def aggression(self):
        self.aggression_level = (self.age*self.happiness_level)/100
        return self

    def display_info(self):
        print(f"animal name is: {self.name}\n current health: {self.health_level}\n current happiness: {self .happiness_level}\n aggression level: {self.aggression_level}")


class Tiger(Animal):
    def __init__(self, name, age=10, health_level = 100, happiness_level = 80, aesthetic = 10):
        super().__init__(name, age, health_level, happiness_level)
        self.aesthetic = aesthetic
    
    def feed(self):
        self.health_level += 10
        self.happiness_level += 50
        return self
    
    def beauty(self):
        self.aesthetic = self.age * 10
        return self
    
    def display_info(self):
        print(f"animal name is: {self.name}\n current health: {self.health_level}\n current happiness: {self .happiness_level}\n aesthetic level: {self.aesthetic}")


zoo1 = Zoo("Azzam's zoo")
zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Share Khane")
zoo1.add_tiger("Rajah")
zoo1.print_all_info()