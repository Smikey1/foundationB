#  This is a single line comment

"""
This is a multi line comment
we can write many lines here
as much as you want
no matter
This all above lines are consider as
comment in python
"""

# this is a print function in python
# which provides output to the console
print("Hello! Batch 33B")

print(2+2)


'''# Button calling --> Dial
def dail(phone_num):
    print(f"{phone_num} \n Calling ... ")

def openConatctDialer(num_length,user_provided_num):
    if num_length > 10 and type(user_provided_num)==str:
        print("Number Invalid")
    elif num_length<10:
        print("call ended")
    elif num_length==10 and type(user_provided_num)==int:
        dail(int(user_provided_num))
    else:
        return

#6789403--> 7
recipent_num = input("Please provide number: ")
openConatctDialer(len(recipent_num),recipent_num)
'''

# continue
name = input("Please provide your name: ")
print(f"Hi! {name}, How are you?")  # String formating


# ask a user info such as name, age:

#Solution
# name = input("Please provide your name")
# age = input("Please provide your age")
name,age = input("Please provide your name and age (comma seprated)").split(",")
print(f"Your name is {name} and age is {age}")
