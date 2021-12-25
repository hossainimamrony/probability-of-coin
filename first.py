from random import randint
from time import sleep
heads = 0
tails = 0
flip = int(input("How many coin tosses are you going to do? :"))
for i in range(flip):
    result = randint(0,1)
    sleep(0.7)
    if result == 0:
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails +=1
print("Total Heads :",heads)
print("Total Tails :",tails)
probabilyty_H = f"{heads}/{flip}"
print("probability of Heads :", probabilyty_H);
probabilyty_T = f"{tails}/{flip}"
print("Probabilyty of Tails :", probabilyty_T)
