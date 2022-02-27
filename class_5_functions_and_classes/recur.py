count = 0

def recur(count):
    if count == 10:
        return

    print("*", end= " ")
    count = count + 1
    recur(count)

recur(count)