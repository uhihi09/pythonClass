from math import floor
def tuppers_formula(x,y):
    return 0.5 < floor((y// 17 // 2 ** (17 * floor(x) + floor(y) %17))%2)

k = 960939379918588497167296212785275471500433966012930665150551927170280239526642468964284217435071812126

for y in range(k,k+17):
    for x in range(105, -1, -1):
        if tuppers_formula(x, y):
            print('@', end='')
        else:
            print(' ', end=' ')
    print(' ')