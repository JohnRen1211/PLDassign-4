print("Good morning costumer price the of an apple is 20 pesos and the orange is 25 pesos each:")
apple = 20
orange = 25

def getFruitamount():
    print(" How many apples you want to buy?: ")
    applesFunc = int(input())
    print(" How many oranges you want to buy?: ")
    orangesFunc = int(input())
    amountFunc = float(apple*applesFunc + orange*orangesFunc)
    return applesFunc, orangesFunc, amountFunc
    
def display (applesFunc, orangesFunc, amountFunc): 
    print(f"The total amount of {applesFunc} apple/s and {orangesFunc} orange/s is {amountFunc} pesos")



#Steps in making this program
# 1.Show the price of the fruits in the market.
# 2.Step ask for how many apples you want to buy.
# 3.Step ask for how many oranges you want to buy.
# 4.Step show the total amount that need to be paid in the display.
# 5.The functions used must be combined to apply the global function.
# 6.The variables must be assigned to the fucntion to call using display.
apples,oranges,amount= getFruitamount() 
display(apples,oranges,amount) 


