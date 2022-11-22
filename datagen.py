import random
import math
random.seed(42)

def funct(x,y):
    return (x+y)**2

for i in range(0,1000):
    
    x = random.randint(1,999)
    y = random.randint(1,999)
    with open('dataset_inp.txt', 'a') as f:
        f.write(f"{x}, {y}, {funct(x,y)}\n")