import random
import time

w = ["cat","dog","fox","monkey","mouse","panda","frog","snake","wolf"]
n = 0
b = 0
time.time()
start = time.time()
while n < 5:
        b = random.choice(w)
        print(b)
        word = input()
        if word == b:
            n += 1
            print("pass")
        else:
            print("fail")
print("--------------")
stop = time.time()
re = stop - start
print(f"걸린시간은 {re}초입니다")