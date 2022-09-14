

# Today's question:
#1  Ask a two integer number with user and a function should return their addition

#2  Ask an information of your laptop and a function should return like this: 
""" 
Brand_Name Model_Name available_at Price

Ex: Dell Vostro @ Rs. 80000

"""

brand_name, model_name, price = input("Please input the your laptop details (brand_name,model_name,price):").split(",")

def laptop_info(brand,model,price):
    return f"{brand} {model} @ Rs. {price}"

print(laptop_info(brand_name,model_name,price))


first_num = int(input("Please provide the first number: "))
second_num = int(input("Please provide the second number"))

print(type(first_num))

print(f"The sum of two number is: {int(first_num)+int(second_num)}")

print("------------------------------------------------------------")
#creation of addition function

def addition(num1,num2):
    sum = num1+num2
    return sum

#calling addition function
print(f"the sum return by the function is: {addition(first_num,second_num)}")

# python 3
print("the sum return by the function is: {}".format(addition(first_num,second_num)))


"""
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.  
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


"""
