# We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies
# (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) we'll say
# have 3 ears, because they each have a raised foot. Recursively return the
# number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).

def bunnies_again(n):
    if n <= 0:
        return n
    else:
        if n % 2 == 0:
            return bunnies_again(n-1) + 3
        else:
            return bunnies_again(n-1) + 2
print(bunnies_again(7))