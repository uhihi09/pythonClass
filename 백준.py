a = int(input())
for i in range(a):
    b = int(input())
    c = ""
    if b <= 25:
        c = "World Finals"
    elif b <= 1000:
        c = "Round 3"
    elif b <= 4500:
        c = "Round 2"
    else:
        c = "Round 1"
    print(f"Case #{i+1}: {c}")