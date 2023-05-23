class Person:
    def __init__(self, initialAge):
        if initialAge >= 0:
            self.initialAge = initialAge
        else:
            print(f'Age is not valid, setting age to 0.')
            self.initialAge = initialAge
            initialAge = 0

    def amIOld(self):
        if self.initialAge < 13:
            print("You are young.")
        elif 18 > self.initialAge >= 13:
            print("You are a teenager.")
        else:
            print("You are old.")
        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        self.initialAge += 1


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")