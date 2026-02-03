# mixing color game
col1 = input("Enter the 1st colour (red, blue, yellow): ").lower()
col2 = input("Enter the 2nd colour (red, blue, yellow): ").lower()
colors = [col1, col2]

if col1 == col2:
    print("You have chosen the same colour twice. You get the same colour :", col1)

elif "red" in colors and "blue" in colors:
    print("You have made purple")

elif "red" in colors and "yellow" in colors:
    print("You have made orange")

elif "yellow" in colors and "blue" in colors:
    print("You have made green")

else:
    print("Invalid colour combination. Please enter red, blue, or yellow.")
