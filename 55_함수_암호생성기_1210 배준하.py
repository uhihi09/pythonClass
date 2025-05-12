import random

def genPass():
    chr = 'abcdefghijklmnopqrstuvwxyz0123456789'
    passwd = ' '
    for i in range(8):
        passwd += random.choice(chr)
    return passwd

for i in range(3):
    result = genPass()
    print(f"암호 {i+1}: {result}")