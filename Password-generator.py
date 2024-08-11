import random
import string
randompw = []
while True:
    try:
        pw_length = int(input('\033[1m' + 'Please specify the length of the generated password: ' + '\033[0m')) 
        break
    except ValueError:
        print('Invalid Input, Please enter an integer next time')

for x in range(pw_length):
    elements, weights = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), random.choice(string.digits), random.choice('!@#$%^&*()')],[2.5,2.5,3,2]

    randompw.append(random.choices(elements, weights,)[0])
print(f"Your randomly generated password is: {''.join(randompw)}")