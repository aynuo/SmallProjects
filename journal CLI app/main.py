date = input("Enter Today's Date? ")
mood = input("How do you rate your mood today from 1 to 10? ")
journal = input("Let your thoughts flow:\n ")

with open(f"journals/{date}.txt", mode="w") as file:
    file.write(mood + ("\n"*2))
    file.write(journal)
