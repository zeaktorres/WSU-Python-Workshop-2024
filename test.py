class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def increaseAge(self):
        self.age += 1
class GoldenRetriever(Dog):
    def __init__(self, name, age, furColor):

        super().__init__(name, age)

        self.furColor = furColor

myDog = GoldenRetriever("Lucky", 2, "Gold")

myDog.increaseAge()

print(myDog.age)

print(myDog.furColor)
myDog = Dog("Lucky", 3)
myDog.increaseAge() 
print(myDog.age)
