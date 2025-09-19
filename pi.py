import math
import random

def print_pi(digits):
    cur_dig = math.pi
    for i in range (digits):
        nex_dig = cur_dig % 1
        nex_dig = nex_dig * 10
        cur_dig = cur_dig // 1
        print(cur_dig)
        cur_dig = nex_dig

for j in range(50):
    print(random.randrange(0,9))


