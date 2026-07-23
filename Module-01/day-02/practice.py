#PRACTICE EXRERCISSES

# 1.Temperature label.Ask for a temperature in °C,then print "cold" below 15,"warm" from 15–28, and "hot" above 28, using if / elif / else.


temp = int(input("enter a temprature in oC:"))
if temp <15:
    print("cold")
elif temp>=15 and temp<=28:
    print("warm")
else:
    print("hot")



# 2. Receipt loop. Use a for loop and range to print receipt numbers 1 through 10, each on its own line as "Receipt #N".
for i in range(1,11):
    print("reciept #",i)



# 3. Even numbers. Print every even number from 1 to 20 using a loop and the modulo operator %.

for i in range (1,21):
    if  i%2 == 0:
        print(i)
    else:
        continue




#4. Discount function. Write apply_discount(price, percent=10) that returns the price after the discount. Test it with and without the default percent.
 

def apply_discount(price, percent=10):
    discount_amount = price * (percent / 100)
    return price - discount_amount

user_price = int(input("enter the price: "))

result_default = apply_discount(user_price)
print("Price with default 10% discount:", result_default)

result_custom = apply_discount(user_price, percent=25)
print("Price with custom 25% discount:", result_custom)



#5. Countdown. Use a while loop to count down from 5 to 1, printing each number, then print "Lift off!" after the loop.
countdown =5
while countdown>0:
    print(countdown)
    countdown=countdown-1
    
print("lift off!")