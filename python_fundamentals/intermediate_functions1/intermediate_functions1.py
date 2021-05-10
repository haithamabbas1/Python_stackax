import random
def randInt(min, max):
    num = round(random.random() * (max-min)+ min)
    return num

print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))