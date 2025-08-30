# Assignment 2: Polymorphism Challenge! 🎭
# Simple example showing different animals and vehicles moving differently

# ANIMALS - All have move() method but do it differently
class Dog:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"🐕 {self.name} is running on four legs!")

class Bird:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"🐦 {self.name} is flying in the sky!")

class Fish:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"🐠 {self.name} is swimming in the water!")


# VEHICLES - All have move() method but do it differently  
class Car:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"🚗 {self.name} is driving on the road!")

class Plane:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"✈️ {self.name} is flying through the clouds!")

class Boat:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print(f"🚤 {self.name} is sailing on the water!")


# Test all our animals and vehicles
def main():
    print("🎭 Polymorphism Challenge - Same Method, Different Actions!")
    print("=" * 60)
    
    # Create animals
    print("\n🐾 ANIMALS:")
    dog = Dog("Buddy")
    bird = Bird("Eagle")
    fish = Fish("Nemo")
    
    # All animals have move() but they move differently!
    dog.move()
    bird.move()
    fish.move()
    
    # Create vehicles
    print("\n🚗 VEHICLES:")
    car = Car("Honda Civic")
    plane = Plane("Boeing 747")
    boat = Boat("Yacht")
    
    # All vehicles have move() but they move differently!
    car.move()
    plane.move()
    boat.move()
    
    print("\n🎯 This is POLYMORPHISM!")
    print("   Same method name (move) but different behaviors!")
    
    # Show polymorphism in action with a list
    print("\n📝 Moving everything in a list:")
    everything = [dog, bird, fish, car, plane, boat]
    
    for thing in everything:
        thing.move()  # Same method call, but different results!
    
    print("\n✅ Challenge Complete!")


# Run the program
if __name__ == "__main__":
    main()
