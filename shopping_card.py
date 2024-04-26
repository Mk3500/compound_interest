***
***
foods = []
prices = []
total = 0
while True:
    food = input("enter food you will like to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price =int(input(f"enter price you will like to buy {food} $: "))
        foods.append(food)
        prices.append(price)
print("---------your  cards ------------")
for food in foods:
    print(f,end= " ")
for price in prices:
    total += price
print(f"your total is {total} ")
