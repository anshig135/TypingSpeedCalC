from time import *
import random as r


def mistake(par_test, user_test):
    error = 0
    for i in range(len(par_test)):
        try:
            if par_test[i] != user_test[i]:
                error += 1
        except:
            error += 1
    return error


def speed_time(initial_time, end_time, userinput):
    time_delay = end_time - initial_time
    time_round_off = round(time_delay)
    speed = len(userinput) / time_round_off
    return round(speed)


if __name__ == '__main__':
    while True:
        ck = input("Ready to test: Yes / No : ")
        if ck == "Yes":
            test = [
                "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea.",
                "My name is Anshika Gupta", "Welcome to Typing Speed Test"]

            test1 = r.choice(test)
            print("*****Typing Speed*****")
            print(test1)
            print()
            print()
            time_1 = time()
            test_input = input("Enter : ")
            time_2 = time()
            print('Speed : ', speed_time(time_1, time_2, test_input), "w/sec")
            print("Error : ", mistake(test1, test_input))
        elif ck == "No":
            print("Thank You for visiting!!")
            break
        else:
            print("Wrong Input")
