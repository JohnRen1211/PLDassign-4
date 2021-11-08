# Programming using Global Function.

def getUserinput():
    name_=input ("Name: ")
    age_=int(input("Age: "))
    add_=input("Address: ")
    return name_, age_, add_


def display(name_, age_, add_):
    print(f"Hi my name is {name_}. I'am {age_} years old and lived in {add_}.")



#Steps in making this program
# 1.step ask for name age address save to variable
name, age, add = getUserinput() 
# The global function contains a lot of variable of the program.
# To use display or displayoutput variables used must be included.
# 2. step display name age and address display 

display(name, age, add)   




