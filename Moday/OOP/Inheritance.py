
#  ======================================= 8.Inheritance =======================================

# Parent Class (ថ្នាក់មេ)
class Animal:
    def eat(self):
        print("សត្វនេះកំពុងស៊ីចំណី។")

# Child Class (ថ្នាក់កូន) ស្នងមរតកពី Animal ដោយប្រើសញ្ញាវង់ក្រចក (Animal)
class Dog(Animal):
    def bark(self):
        print("ឆ្កែកំពុងព្រុស៖ វូសៗ!")

# បង្កើត Object ចេញពី Class កូន
my_dog = Dog()
my_dog.bark() 
my_dog.eat() 
