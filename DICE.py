import random
while True:
    read = input()
    if read == 'row':
        print(random.randint(1, 6))
    elif read == 'stop':
        break
