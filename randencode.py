import random
seed = 78965454654684654455555555555555513456516564
def randencode(message, seed):
    output = ""
    random.seed(seed)
    for letter in message:
        output += chr(ord(letter) ^ random.randrange(32,256))
    return output


print("This is a secret message")
print()
print(randencode("This is a secret message", seed))
print()
print(randencode(randencode("This is a secret message", seed), seed))
