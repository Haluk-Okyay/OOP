# class MyClass:
#     x = 5

# p1 = MyClass()
# print(p1.x)

# print(MyClass.x)

# class Person:
#     def __init__(silly, name, age):
#         silly.name = name
#         silly.age = age

#     def myfunc(trial):
#         print("Hello my name is " + trial.name)

# p1 = Person("Ozan", 42)
# p1.myfunc()

# del p1
# print(p1.age)

# class Book:
    
#     def __init__(x, title, author):
#         x.title = title
#         x.author = author

#     def display(d1):
#         print("Name of the book is "+ d1.title + " and it's written by " + d1.author)
    
# novel = Book("Sahara", "Clive Cussler")
# novel.display()

# novel.title = "Twenty Thousand Leagues Under the Seas"
# novel.author = "Jules Verne"
# novel.display()


# class Mobile:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def comparison(x):
#         print("The latest model that has been release this year is: " + x.model + " from " + x.brand)

# p1 = Mobile("Apple", "iPhone 13")

# p1.comparison()


# class Mileage:
#     def __init__(self, fuel, dist):
#         self.fuel = fuel
#         self.dist = dist

#     def calc(self):
#         avg = (100 * self.fuel / self.dist)
#         print("Average fuel consumption is: " + str(avg) + " l/100km")

# avg1 = Mileage(3, 25)
# avg1.calc()

# class Shark:
#     animal_type = "fish"
#     location = "ocean"
#     followers = 5

# new_shark = Shark()
# print(new_shark.animal_type)
# print(new_shark.location)
# print(new_shark.followers)

# class Shark:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# new_shark = Shark("Sammy", 5)
# print(new_shark.name)
# print(new_shark.age)

# stevie = Shark("Stevie", 8)
# print(stevie.name)
# print(stevie.age)

# class Shark:

#     # Class variables
#     animal_type = "fish"
#     location = "ocean"

#     # Constructor method with instance variables name and age
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Method with instance variable followers
#     def set_followers(self, followers):
#         print("This user has " + str(followers) + " followers")


# def main():
#     # First object, set up instance variables of constructor method
#     sammy = Shark("Sammy", 5)

#     # Print out instance variable name
#     print(sammy.name)

#     # Print out class variable location
#     print(sammy.location)

#     # Second object
#     stevie = Shark("Stevie", 8)

#     # Print out instance variable name
#     print(stevie.name)

#     # Use set_followers method and pass followers instance variable
#     stevie.set_followers(77)

#     # Print out class variable animal_type
#     print(stevie.animal_type)


# if __name__ == "__main__":
#     main()




# class Driver():
#     demerit = 12

#     def __init__(self, name):
#         self.name = name

# ozan = Driver("oz")

# print(ozan.demerit)
# print(Driver.demerit)

# print(id(Driver.demerit))
# print(id(ozan.demerit))

# ozan.demerit = 9

# print(ozan.demerit)
# print(Driver.demerit)

# print(id(Driver.demerit))
# print(id(ozan.demerit))


class Bikes():
    
    def __init__(self, brand):
        self.__brand = brand

    def set(self, value):
        self.__brand = value

    def get(self):
        return self.__brand

x = Bikes()

x.set("yamaha")

print(x.get())