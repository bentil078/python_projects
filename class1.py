class SayMyName:
    def __init__ (self, myname, myage):
        self.myname = myname
        self.myage = myage

    def say(self):
        print("Hello, my name is %s and %d years old" %(self.myname, self.myage))


if __name__ == '__main__':
    while True:
        name = str(input("what is your name?\n"))
        age1 = input("how old are you?\n")

        try:
            age = int(age1)
            name1 = SayMyName(name, age)
            name1.say()
            
        except ValueError:
            print("enter integers only\n")

    
    