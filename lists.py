import random

fruits = ("apple", "banana", "cherry")
fruits.append("date")
fruits.extend(["elderberry","fig","grape"])
fruits += ["honeydew", "kiwi", "lemon"]

prints (fruits)

while true
    fruit= random.choice(fruits)
    like= input (f"do you like (fruit)? (yes/no/stop) ")
    if like.lower ()=="yes":
        new_fruit = input(f"Name another fruit to add: ")
        fruits.apprend (new_fruit)
    elif like. lower () == "no":
        print(f"removing (fruit) from the list")
        fruits.remove (fruit)
    elif.like. lower() == "stop":
        break

        with open ("fruits.txt","w") as fd:
            for fruit in fruits:
                fd.write(fruit +"/n")
