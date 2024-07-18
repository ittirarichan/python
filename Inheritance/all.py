# Base class
class LivingBeing:
    def breathe(self):
        return "Living beings breathe"
    



# Single Inheritance
class Animal(LivingBeing):
    def move(self):
        return "Animals move"
    



# Multiple Inheritance
class Bird(LivingBeing):
    def fly(self):
        return "Birds fly"
    



# Multilevel Inheritance
class Eagle(Bird):
    def hunt(self):
        return "Eagles hunt"
    



# Hierarchical Inheritance
class Fish(LivingBeing):
    def swim(self):
        return "Fishes swim"
    



# Hybrid Inheritance
class FlyingFish(Animal, Bird):
    def glide(self):
        return "Flying fishes can also glide"
    


def demo_inheritance(entity):
    print(entity.breathe())
    if isinstance(entity, Animal):
        print(entity.move())
    if isinstance(entity, Bird):
        print(entity.fly())
    if isinstance(entity, Eagle):
        print(entity.hunt())
    if isinstance(entity, Fish):
        print(entity.swim())
    if isinstance(entity, FlyingFish):
        print(entity.glide())

living_being = LivingBeing()
animal = Animal()
bird = Bird()
eagle = Eagle()
fish = Fish()
flying_fish = FlyingFish()

print("Demonstrating LivingBeing:")
demo_inheritance(living_being)

print("\nDemonstrating Animal (Single Inheritance):")
demo_inheritance(animal)

print("\nDemonstrating Bird (Multiple Inheritance):")
demo_inheritance(bird)

print("\nDemonstrating Eagle (Multilevel Inheritance):")
demo_inheritance(eagle)

print("\nDemonstrating Fish (Hierarchical Inheritance):")
demo_inheritance(fish)

print("\nDemonstrating FlyingFish (Hybrid Inheritance):")
demo_inheritance(flying_fish)
