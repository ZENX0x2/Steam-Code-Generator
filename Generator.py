import random
import string

file = open

def MakeKey():
    k1 = ''.join(random.choice(string.ascii_uppercase + string.digits)
                 for _ in range(5))
    k2 = ''.join(random.choice(string.ascii_uppercase + string.digits)
                 for _ in range(5))
    k3 = ''.join(random.choice(string.ascii_uppercase + string.digits)
                 for _ in range(5))
    print(f'{k1}-{k2}-{k3}')
    FinalCode = k1+"-"+k2+"-"+k3



KeyCount = int(input("How many gift-cards do you want to generate? "))

for key in range(KeyCount):
    MakeKey()