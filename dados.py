import random
option = int(input("Do you wanna drop a dice?. \n 1: Yes \n 2: No \n"))
while (option == 1):
    number = random.randint(1,6)
    print(f'Your number is [{number}]')
    option = int(input("Try Again?. \n 1: Yes \n 2: No \n"))
print("App ended")