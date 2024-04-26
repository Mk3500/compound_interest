
principal = int(input("enter your principal: "))
while principal <= 0:
    print("amount can not be negative or zero")
    principal = int(input("enter your principal: "))

time =int(input("enter your time: "))
while  time <= 0:
    print("time can not be negative or zero: ")
    time =int(input("enter your time: "))
rate = int(input("enter rate : "))
while rate <= 0:
    print("rate can not be negative")
    rate = int(input("enter rate : "))
amount = principal * pow(1+rate/100, time)
print(f"your capital is ${principal}")
print(f"your time is {time} years")
print(f"your rate is {rate} %")
print(f"your future value is $ {amount:.2f}")
 

 #sir my code keep looping any time i type a negative figure
 # thank you sir my code has been updated now wooo!