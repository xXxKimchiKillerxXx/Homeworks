def cost():
    value = int(input())
    if 100 <= value <= 2000:
        return value
    else:
        print("Incorrect data, terminating.")
        raise SystemExit

burger = [cost() for _ in range(0,3,1)]
drink = [cost() for _ in range(3,5,1)]

min_set = min(burger) + min(drink)

print("가장 싼 메뉴의 가격 : " + str(min_set))