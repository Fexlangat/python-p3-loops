#!/usr/bin/env python3

def happy_new_year():
    i = 10
    # code goes here!
    while i > 0:
        print(i)
        i -=1
    print("Happy New Year!")
            
happy_new_year()


def square_integers(int_list):
    # code goes here!
    squared_list = []
    for num in int_list:
        squared_list.append(num ** 2)
    return squared_list

print(square_integers([1, 2, 3, 4, 5]))
    


def fizzbuzz():
    # code goes here!
     for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()

    






# player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]

# inch_heights = list()
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)
#     inch_heights = [height * 7920 for height in player_heights]
#     player_heights = [height * 7920 for height in player_heights]

# print(player_heights)