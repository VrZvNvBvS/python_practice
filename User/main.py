class User:

    def __init__(self, first_name, last_name, email, age, is_rewards_members=False, gold_card_points=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age

        self.is_rewards_members = is_rewards_members
        self.gold_card_points = gold_card_points

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)

    def enroll(self, is_rewards_members):
        if is_rewards_members == True:
            print("User already a member.")
            return False
        else:
            self.gold_card_points = 200
            return True

        # change the user's member status to True
        # and set their gold card points to 200

    def spend_points(self, amount):
        self.gold_card_points -= amount
        return

        # decrease the user's points by the amount specified

    def verify_email(self, email):
        if self.email == email:
            print("Email confirmed!")
        else:
            print("Email does NOT match!")

    def age_guess(self, age):
        if age == self.age:
            print("You guessed CORRECT!")
        else:
            print("INCORRECT, guess again!")


jay = User('jay', 'Nguyen', 'jay@pm.me', 36)

jay2 = User('Homer', 'Simpson', 'dohnuts@gmail.com', 52)

jay3 = User('Bart', 'Simpson', 'bart@gmail.com', 18, False, 100)
jay3.spend_points(40)

jay2.enroll(True)

jay.display_info()
jay2.display_info()


jay.enroll(False)
print(jay.is_rewards_members)

jay.spend_points(50)
print(jay.gold_card_points)

jay.verify_email("jjj@gmail.com")
print(jay.email)

jay.age_guess(55)


# print(dir(jay))
