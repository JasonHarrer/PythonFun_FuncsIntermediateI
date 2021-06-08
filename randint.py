import random

def randInt(min=0, max=100):
    # if min > max in any situation, we will swap them.
    if(min > max):
        return round(random.random() * (min - max) + max)
    return round(random.random() * (max - min) + min)


print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=150, max=25))
print(randInt(min=-14, max=-7))
print(randInt(max=-12))
print(randInt(12, 12))
