class Friend:
    def __init__(self,name):
        self.name = name

    def say(self):
        print(self.name, "is a nice imaginary friend")


friend = Friend("Killian")
friend.say()
