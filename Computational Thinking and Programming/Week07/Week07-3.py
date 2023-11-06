def sieve(text):
    quote = text.split(' ')
    filtered = [word[::-1] for word in quote if len(word) >= 5]
    print(filtered)

sieve("This is a more advanced comprehension exercise to practice")