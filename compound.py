
principal = int(input("enter your principal: "))
p = principal
while p <= 0:
    print("amount can not be negative")
    principal = int(input("enter your principal: "))

time =int(input("enter your time: "))
t = time
while  t <= 0:
    print("time can not be negative: ")
    time =int(input("enter your time: "))
rate = int(input("enter rate : "))
r = rate/100
while r <= 0:
    print("rate can not be negative")
    rate = int(input("enter rate : "))
amount = p * pow(1+r,t)
print(f"your capital is ${p}")
print(f"your time is {t} years")
print(f"your rate is {r} %")
print(f"your future value is $ {amount:.2f}")
 

 sir my code keep looping any time i type a negative figure
