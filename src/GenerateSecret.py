import random
class GenerateSecret:
    def __init__(self):
        secret = ''
        pattern = 'dfjkjJH03489JDJKdlskfj9731456hlse80458JHS-df-3354--#kjd(kdfj)gg%'
        choice = int(input("Enter length for your secret\n"))
        for data in range(choice):
            limit = len(pattern)-1
            index = random.randint(0,limit)
            secret = secret+pattern[index]
        print(secret,'\n')