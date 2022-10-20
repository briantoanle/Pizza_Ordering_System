# case insensitive
# constants must be uppercase
import pizzaReceipt

TOPPINGS = ('ONION','TOMATO','GREEN PEPPER','MUSHROOM','OLIVE','SPINACH','BROCCOLI',
            'PINEAPPLE','HOT PEPPER','PEPPERONI','HAM','BACON','GROUND BEEF','CHICKEN',
            'SAUSAGE')
wholeOrder=[]

sizes = ['S','M', 'L', 'XL']
def pickASize(counter):
    pickSize = True
    pizzaSize = ''
    if counter < 1:
        orderPizza = str(input("Do you want to order a pizza?   ")).upper()

    else:
        orderPizza = str(input("Do you want to continue ordering?   ")).upper()
    if orderPizza == 'Q' or orderPizza == 'NO':
        print()
        # generateReceipt(wholeOrder)
        return 'STOP'
        pickSize = False

    while pickSize:

        size = str(input("Choose a size:    S, M, L, or XL:  ")).upper()
        pizzaSize = size
        if size in sizes:
            pickSize = False

    return pizzaSize

def pickSomeToppings():
    pizzaTopping = []
    pickToppings = True

    while pickToppings:
        topping = str(input('Type in one of our toppings to add it to your pizza. To see the list of toppings, enter\n'
                            '"LIST". When you are done adding toppings, enter "X"\n')).upper()
        if topping == 'LIST':
            print(TOPPINGS)
        elif topping == 'X':
            #return 'X'
            break
            #pickToppings = False
        else:
            if topping not in TOPPINGS:
                print('Invalid topping')
            else:
                print(f'Added {topping} to your pizza')
                pizzaTopping.append(topping)
    print(pizzaTopping)
    return pizzaTopping

# test case
# 'M', pepperoni olive
# 'L', mushroom broccoli tomato

# wholeorder =
def main():
    orderPizza = True
    counter = 0
    while orderPizza:


        pizzaSize = pickASize(counter)
        counter += 1
        if pizzaSize == 'STOP':
            break
        listOfToppings = pickSomeToppings()
        if listOfToppings == 'X':
            orderPizza = False
        pizzaAfterToppings = (pizzaSize, listOfToppings)
        wholeOrder.append(pizzaAfterToppings)
    #print(wholeOrder)
    pizzaReceipt.generateReceipt(wholeOrder)





    # After the size has been properly selected, the user must be prompted to enter in their toppings
    #       one at a time until they are finished





    # then they must enter "X", in any case, to indicate that
        # they are finished adding toppings




main()
