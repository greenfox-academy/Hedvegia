import random
rand = random.randint(1,100)

vars = 6

print("I've the number between 1-100. You have "+str(vars)+" lives.")
tipp = int(input())

while rand != tipp and vars > 1:
    if rand < tipp:
        vars -= 1
        print("Too high. You have "+str(vars)+" lives left.")
        tipp = int(input())
    else:
        vars -= 1
        print("Too low. You have "+str(vars)+" lives left.")
        tipp = int(input())
if rand == tipp:
    print('Congratulation')
else:
    print("Game Over")
print("The number was: "+str(rand))
