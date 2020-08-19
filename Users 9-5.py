class Users():
    def __init__(self,first_name,last_name,age,location,sex):
        self.name = first_name
        self.last = last_name
        self.age = age
        self.location = location
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        info = "Name: " + self.name.title() \
               + "\nLast Name: " + self.last \
               + "\nAge: " + self.age \
               + "\nLocation: " + self.location \
               + "\nSex: " + self.sex
        print("User's information: " + info)

    def greet_user(self):
        message = "Greetings " + self.name.title() + "! Nice to meet you!"
        print("\n" + message)

    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1


    def reset_login_attempts(self):
        self.login_attempts = 0

userObject = Users('Marcase', 'Darius', '23', 'Timisoara', 'Male')
userObject1 = Users('Steopan', 'Denisa', '21', 'Deva', 'Female')
userObject2 = Users('Donesi', 'Iulia', '25', 'Lugoj', 'Female')

userObject.describe_user()
userObject.greet_user()

userObject1.describe_user()
userObject1.greet_user()

userObject2.describe_user()
userObject2.greet_user()

userObject.increment_login_attempts()
userObject.increment_login_attempts()
userObject.increment_login_attempts()
userObject.increment_login_attempts()

print(" Login Attempts: " + str(userObject.login_attempts))

print(" Resetting login attempts... ")

userObject.reset_login_attempts()

print(" Login attempts: " + str(userObject.login_attempts))

