def sieve():
    quote = input().split(' ')
    filtered = [word[::-1] for word in quote if len(word) >= 5]
    print(filtered)

sieve()