print("The money inside the wallet.")

def fruitRemainmoney():
    print("How much money you have in wallet?")
    moneyFunc = float(input())
    print("How much is an apple? ")
    appleFunc = float(input()) 
    maxApples = moneyFunc // appleFunc
    remainMoney = moneyFunc - (maxApples * appleFunc)
    return moneyFunc, appleFunc, maxApples, remainMoney 

def displayOutput (maxApples,remainMoney):
     print(f"The amount of apples I can buy are {maxApples} and the remaining money is {remainMoney} pesos")

#Steps in making this program
# 1. Check the amount of money in wallet.
# 2.step ask for how many money left in wallet use float for variable.
# 3.step ask for how much is an apple use float.
# 4.step display the maximum apples that can be bought and the remaining money.
# 5.step show the apples can buy and the remaing money by using global function.

money,apple,maximumApple,remaincash = fruitRemainmoney()

displayOutput(maximumApple,remaincash)

print("Thank you for shopping")   


