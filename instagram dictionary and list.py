# list comprehension

numbers = [1, 2, 3, 4, 5, 6]
result = ["even" if num % 2 == 0 else "odd" for num in numbers]
print(result)

#dictionary for instagram username and password

users = {}
username = input("enter username:")
password = input("enter password:")

if username in users:
    print("error: username already exists!")
else:
        users[username] = password
        print("account created successfully!")
