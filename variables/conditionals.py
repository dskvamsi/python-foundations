# # 1) Check eligibility for voting: Input age, 
# # print "Eligible" if ≥18, else "Not eligible".

# age = int (input("Enter age "))
# if (age >= 18):
#     print ("Eligible")
# else:
#     print ("NotEligible")


# # 2) Even or Odd: Input a number, 
# # print whether it’s even or odd.

# n = int (input("Enter a  number "))
# if n % 2 == 0:
#    print("Even")
# else:
#    print("odd")

# # 3) Positive, Negative, or Zero: Classify a number. 
# n= int (input("Enter a number "))
# if (n > 0):
#     print("Positive")
# elif (n < 0):
#     print("Negative")
# else:
#     print("Zero")

# # 4)Greatest of Two Numbers: Compare two inputs and print the larger.
# a = float(input("Enter First Number "))
# b = float(input("Enteer Second Number "))

# if a > b:
#     print("Greatest number is:", a)

# elif b > a:
#     print("Greatest number is:", b)
    
# else:
#     print("Both numbers are equal")





color = input("Enter traffic light color: ").strip().capitalize()

if color == "Red":
    print("Stop! Vehicles must wait.")

elif color == "Yellow":
    print("Get ready to move.")

elif color == "Green":
    print("Go! Vehicles can move.")

else:
    print("Invalid input. Please enter Red, Yellow, or Green.")
