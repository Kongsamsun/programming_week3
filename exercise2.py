class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "Name: %s, Age: %d" % (self.name, self.age)
    def human_age(self):
        return self.age * 4
    
class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)
    def bark(self, n):
        for barks in range(n): #매개변수만큼 반복
            print("bark!")
    
class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)
    def meow(self, n):
        for meows in range(n):
            print("meow~")
    
if __name__ == '__main__':
    
    popo = Dog('popo', 10)
    popo.bark(3)
    print(popo)
    print("사람 나이로 환산: %d" % popo.human_age())

    pipi = Cat('pipi', 5)
    pipi.meow(4)
    print(pipi)
    print("사람 나이로 환산: %d" % pipi.human_age())