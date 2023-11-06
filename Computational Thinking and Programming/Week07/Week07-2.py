def Fortytwo():
    value = int(input())
    if 0 <= value <= 1000:
        return value % 42
    else:
        print("Incorrect data, terminating.")
        raise SystemExit

rem = [Fortytwo() for _ in range(10)]
rem_set = set(rem)

print(len(rem_set))