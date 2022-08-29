import random
import numpy as np

#
#     Let's Make a Deal
#     A contestant is given three doors to choose from and randomly guesses either 1, 2, or 3.
#     Behind 1 of the 3 doors is a car.
#     Behind the remaining 2 doors is a goat.
#     The host, Monte Hall, knows what is behind the doors and opens a door that has the goat
#     Should the contestant stay with their initial guess or switch the guess to the remaining door?
#

# counter for correct by staying
correctStaying = 0
# counter for correct by switching
correctSwitching = 0

# simulate 2000 times
for x in range(2000):

    # The contestant makes a random guess between 1 - 3
    guess = random.randint(1, 3)
    # print("The contestant chose door", guess)

    # The car is behind a random door between 1 - 3
    car = random.randint(1, 3)
    # print("The car is behind door", car)

    # need to keep track of the doors
    doors = [1, 2, 3]

    # the host cannot choose the contestant's door (guess), so we remove it
    # print("removing contestant guess door number: ", guess)
    doors.remove(guess)

    # the host is not going to reveal the door the car is behind, so we remove it
    if not (guess == car):
        # print("removing car door number: ", car)
        doors.remove(car)

    # on one hand, the host is left to reveal the door that is not the guess or the car
    # on the other hand, the host has to randomly choose if the guess and the car are equal
    # ie: guess = 2 and car = 2 | that would leave doors = [1, 3]
    host_choice = random.choice(doors)
    # print("host's reveals door number", host_choice)

    # if the guess is equal to the car - then staying with the original guess wins !
    # find the mean of the two counters
    if guess == car:
        correctStaying += 1
        # print("Staying wins")
        # print("\n================================\n")

    # otherwise, the guess is not equal to the car - then the contestant should have switched their guess
    else:
        correctSwitching += 1
        # print("Switching wins")
        # print("\n================================\n")

print("\nRunning simulation 2000 times..")

print("\nCorrect by staying with original guess:", correctStaying)
print("\nCorrect by switching guess:", correctSwitching)

meanStaying = (correctStaying / 2000) * 100
print(f'\nMean staying: {meanStaying:.2f}%')

meanSwitching = (correctSwitching / 2000) * 100
print(f'\nMean switching: {meanSwitching:.2f}%')
