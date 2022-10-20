

def generateReceipt(pizzaOrder):
    PRICING = {'S':7.99,'M':9.99,'L':11.99,'XL':13.99}
    TOPPING_PRICING = {'S':0.50,'M':0.75,'L':1.00,'XL':1.25}
    TAX = 0.13

    total = 0
    if len(pizzaOrder) == 0:
        print('You did not order anything')
    else:
        print('Your order:')
        for i in range(len(pizzaOrder)):
            toppingCost = 0
            pizza = pizzaOrder[i]
            #print('pizza',pizza)
            pizzaSize = pizza[0]
            #print('pizza size',pizzaSize)
            pizzaCost = PRICING[pizzaSize]
            #print('pizza cost',pizzaCost)
            pizzaTopping = pizza[1]
            #print(pizzaTopping)

            if len(pizzaTopping) > 3:
                toppingCost = (len(pizzaTopping)-3)*TOPPING_PRICING[pizzaSize]
            total +=pizzaCost +toppingCost

            print(f'Pizza {i+1}: {pizzaSize}           {pizzaCost}')
            for j in range(len(pizzaTopping)):
                print('- '+pizzaTopping[j])
            if toppingCost !=0:
                print(f'Extra Topping ({pizzaSize})    {toppingCost:.2f}')
    tax = total * TAX
    totalWithTax = total + tax
    print(total)
    print(tax)
    print(totalWithTax)


def main():
    pizza1 = ("M", ["PEPPERONI", "OLIVE"])

    pizza2 = ("L", ["MUSHROOM", "BROCCOLI", "TOMATO"])
    pizza3 = ('L',['HAM','PEPPERONI','ONION','GREEN PEPPER'])

    listPizza = []
    listPizza.append(pizza1)
    listPizza.append(pizza2)
    example2 = [pizza3]
    generateReceipt(listPizza)
    #print(listPizza[1][0])
main()