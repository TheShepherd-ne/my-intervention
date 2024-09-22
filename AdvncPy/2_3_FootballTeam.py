# (.........: Module :.........)

import random

# (.........: Class :.........)
class Human:
    def __init__(self, name):
        self.name = name

class Footballer(Human):
    def __init__(self, name):
        super().__init__(name)

# (.........: Main :.........)
# names = [
#     "حسین", "مازیار", "اکبر", "نیما", "مهدی",
#     "فرهاد", "محمد", "خشایار", "میلاد", "مصطفی",
#     "امین", "سعید", "پویا", "پوریا", "رضا",
#     "علی", "بهزاد", "سهیل", "بهروز", "شهروز",
#     "سامان", "محسن"
# ]

names = [ 
    "Hossein", "Maziar", "Akbar", "Nima", "Mahdi",
    "Farhad", "Mohammed", "Khashayar", "Milad", "Mustafa",
    "Amin", "Saeed", "Poya", "Puria", "Reza",
    "Ali", "Behzad", "Sohail", "Behrooz", "Shehroz",
    "Saman", "Mohsen"
]

footballers = [Footballer(name) for name in names]

team_A = random.sample(footballers, 11)
team_B = [player for player in footballers if player not in team_A]

print("A Team :")
for player in team_A:
    print(f"{player.name} - A Team")

print("\nB Team :")
for player in team_B:
    print(f"{player.name} - B Team")
