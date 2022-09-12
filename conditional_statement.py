age = int(input("Please provide your age: "))

# conditional Statement
# if block only


print("Code started .....")
if age>18:
	print(f"You can play this game because you are above {age}")

print("Code ended ......")

# if-else block
if age>18:
	print(f"You can play this game because you are above {age}")
else:
	print("You need to be above 18 years old to play this game")

## proper use of if-elif-else block


if age<0:
	print("please input your valid age")
elif age>0 and age <= 10:
	print("So you are kid, your movie ticket is Nrs.100")
elif 10<age<20:
	print("Your movie ticket is Nrs.200")
else:
	print("Your movie ticket is Nrs.300")