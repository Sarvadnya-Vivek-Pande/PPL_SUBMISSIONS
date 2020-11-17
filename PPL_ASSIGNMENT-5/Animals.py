import cv2


class Animals(object):
    def __int__(self):
        print("Animal object Created")
    def speak(self):
        pass
    def eat(self):
        pass
    def display_image(self):
        pass


class LandAnimals(Animals):
    def home(self):
        print("Place of Living : Land")
    def walk(self):
        print("Done walking")


class AquaticAnimals(Animals):
    def home(self):
        print("Place of Living : Water")
    def swim(self):
        print("Done swimming")


class Amphibians(LandAnimals, AquaticAnimals):
    def home(self):
        print("Place of Living : Land and Water")


class Dog(LandAnimals):
    def about(self):
        print("Name : Dog\nType : Domestic, Land Animal")
    def speak(self):
        print("Sound : Bark")
    def favourite_food(self):
        print("Favourite Food : Bones")
    def display_image(self):
        img=cv2.imread("image/dog.jpg")
        cv2.imshow("Dog", img)
        cv2.waitKey(0)


class Cat(LandAnimals):
    def about(self):
        print("Name : Cat\nType : Domestic, Land Animal")
    def speak(self):
        print("Sound : Meow")
    def favourite_food(self):
        print("Favourite Food : Fish , Milk")
    def display_image(self):
        img = cv2.imread("image/cat.jpg")
        cv2.imshow("Cat", img)
        cv2.waitKey(0)


class Elephant(LandAnimals):
    def about(self):
        print("Name : Elephant")

    def type(self):
        print("Type : Wild, Herbivores, Land Animal")

    def favourite_food(self):
        print("Favourite Food : Grass, Fruits")

    def display_image(self):
        img = cv2.imread("image/elephant.jpg")
        cv2.imshow("Elephant", img)
        cv2.waitKey(0)


class Cheetah(LandAnimals):
    def about(self):
        print("Name : Cheetah")
    def type(self):
        print("Type : Wild, Carnivores, Land Animal")
    def favourite_food(self):
        print("Favourite Food : Meat, Flesh")
    def speed(self):
        print("Speed : 100 km/h")
    def display_image(self):
        img = cv2.imread("image/cheetah.jpg")
        cv2.imshow("Cheetah", img)
        cv2.waitKey(0)


class Lion(LandAnimals):
    def about(self):
        print("Name : Lion")
        print("King of the jungle")
    def type(self):
        print("Type : Wild, Carnivores, Land Animal")
    def favourite_food(self):
        print("Favourite Food : Meat, Flesh")
    def speak(self):
        print("Sound : Roar")
    def display_image(self):
        img = cv2.imread("image/lion.jpg")
        cv2.imshow("Lion", img)
        cv2.waitKey(0)


class Deer(LandAnimals):
    def about(self):
        print("Name : Deer")
    def type(self):
        print("Type : Wild, Herbivores, Land Animal")
    def favourite_food(self):
        print("Favourite Food : Grass")
    def display_image(self):
        img = cv2.imread("image/deer.jpg")
        cv2.imshow("Deer", img)
        cv2.waitKey(0)


class Rabbit(LandAnimals):
    def about(self):
        print("Name : Rabbit")

    def type(self):
        print("Type : Wild, Herbivores, Land Animal")

    def favourite_food(self):
        print("Favourite Food : Grass, Carrot")

    def display_image(self):
        img = cv2.imread("image/rabbit.jpg")
        cv2.imshow("Rabbit", img)
        cv2.waitKey(0)


class Fish(AquaticAnimals):
    def about(self):
        print("Name : Fish")

    def type(self):
        print("Type : Aquatic Animal")

    def favourite_food(self):
        print("Favourite Food : Earthworms")

    def display_image(self):
        img = cv2.imread("image/fish.jpg")
        cv2.imshow("Fish", img)
        cv2.waitKey(0)


class Dolphins(AquaticAnimals):
    def about(self):
        print("Name : Dolphin")

    def type(self):
        print("Type : Aquatic Animal")

    def favourite_food(self):
        print("Favourite Food : Fish")

    def display_image(self):
        img = cv2.imread("image/dolphin.jpg")
        cv2.imshow("Dolphin", img)
        cv2.waitKey()


class Turtle(Amphibians):

    def about(self):
        print("Name : Turtle")

    def type(self):
        print("Type : Amphibian ")

    def favourite_food(self):
        print("Favourite Food : Beans, Corn")

    def display_image(self):
        img = cv2.imread("image/Turtle.jpg")
        cv2.imshow("Turtle", img)
        cv2.waitKey()


# D1=Dog()
# D1.about()
# D1.speak()
# D1.favourite_food()
# D1.display_image()

# C1=Cat()
# C1.about()
# C1.speak()
# C1.favourite_food()
# C1.display_image()

# E1=Elephant()
# E1.about()
# E1.type()
# E1.favourite_food()
# E1.display_image()

# Ch=Cheetah()
# Ch.about()
# Ch.type()
# Ch.favourite_food()
# Ch.speed()
# Ch.display_image()

# L1=Lion()
# L1.about()
# L1.type()
# L1.speak()
# L1.favourite_food()
# L1.display_image()

# D1=Deer()
# D1.about()
# D1.type()
# D1.favourite_food()
# D1.display_image()

# R1=Rabbit()
# R1.about()
# R1.type()
# R1.favourite_food()
# R1.display_image()

# F1=Fish()
# F1.about()
# F1.home()
# F1.type()
# F1.favourite_food()
# F1.display_image()

# Do1=Dolphins()
# Do1.about()
# Do1.home()
# Do1.type()
# Do1.favourite_food()
# Do1.display_image()

T1=Turtle()
T1.about()
T1.home()
T1.type()
T1.favourite_food()
T1.display_image()
