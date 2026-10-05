print("welcome to the interactive personal data collector:")

name=input("please enter your name:")
age=int(input("please enter your age:"))
height=float(input("please enter your height:"))
favourite_number=int(input("please enter your favourite number:"))

current_year = 2026
birth_year  = current_year - age
rounded_height = int(height)

print("name:" , name)
print("age:" , age)
print("height:" , height)
print("favourite_number:" , favourite_number)

print("type:",type(name))
print("type:",type(age))
print("type:",type(height))
print("type:",type(favourite_number))

print("memory address:", id(name))
print("memory address:", id(age))
print("memory address:", id(height))
print("memory address:", id(favourite_number))

print("your birth year is approximately:", birth_year)
print("original height:", height)

print("thank you for using the personal data collector!")
