# import the random module
import random

# create the class Dice
class Dice:
    # create the constructor (__init__) method
    # it takes as input the number sides and if none is specified use 6
    # it sets the dice object's number of sides (instance variable)
    # it sets the list that tracks the rolls to the empty list (instance variable)

    def __init__(self, sides = 6):
        self.sides = sides
        self.rolls = []
    


    # create the __str__ method
    # it returns "Last roll: value" where value is the last value in the list that tracks the rolls
    def __str__(self):
        return "Last roll: " + str(self.rolls[-1])


    # create the roll method
    # it randomly picks a value from 1 to the number of sides this dice object has
    # it adds that value to the end of the list that tracks all the rolls
    # it returns the value
    def roll(self):
        roll = random.randrange(1, self.sides)
        self.rolls.append(roll)
        return roll

    def num_rolls(self):
        num_roll = input("How many times do you want to roll? ")
        for i in range(int(num_roll)):
            print(self.roll())



    # BONUS
    # create the print_count_for_num method
    # it will count how many times the passed number has been rolled and print 
    # number was rolled x times - where number is the number and x is the count
    def print_count_for_num(self, number):
        x = 0
        for num in self.rolls:
            if(num == number):
                x += 1
        print(number, "was rolled", x, "times")



# main function
def main():
    
    # Create an instance
    three_sided = Dice(3)
    print("Three sides dice")

    # Roll dice 5 times
    for i in range(5):
       print(three_sided.roll())

    # Print last roll
    print(three_sided)

    # Create an instance
    six_sided = Dice()
    print("\nSix sides dice")

    # Roll dice 5 times
    for i in range(5):
       print(six_sided.roll())

    # Print last roll
    print(six_sided)

    # BONUS quiz
    # Print accumulation
    six_sided.print_count_for_num(3)

    six_sided.num_rolls()

if __name__ == "__main__":
    main()
