color = input("Enter traffic light color: ").strip().capitalize()

if color == "Red":
    print("Stop! Vehicles must wait.")

elif color == "Yellow":
    print("Get ready to move.")

elif color == "Green":
    print("Go! Vehicles can move.")

else:
    print("Invalid input. Please enter Red, Yellow, or Green.")