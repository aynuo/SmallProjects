# give an input
password = input("Enter you password to check => ")

# result
result = []

# check password length
if len(password) > 8:
    result.append("True")
else:
    result.append("False")

# check for include number
is_digit = False
for char in password:
    if char.isdigit():
        is_digit = True
result.append(is_digit)

# check for include uppercase
is_upper = False
for char in password:
    if char.isupper():
        is_upper = True
result.append(is_upper)

# show result
if all(result) == "True":
    print("Strong Password ")
else:
    print("Week Password")
