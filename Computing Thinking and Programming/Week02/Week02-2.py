def add(X):
    if len(X) == 1:
        return X[0]
    else:
        return add(X[1:]) + X[0]

while True:
    prev = input("Enter integers separated by spaces ==> ").split(' ')

    if prev == ['done']:
        print("program terminated. good bye !!")
        break

    elif len(prev) <= 1:
        print("must enter more than one integer")

    else:
        try:
            next = list(map(int, prev))
            print(add(next))
        except:
            print("must enter integers separated by spaces")