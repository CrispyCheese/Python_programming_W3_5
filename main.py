print ("Program starting.\n")
print ("Options:\n1 - Celsius to Fahrenheit\n2 - Fahrenheit to Celsius\n0 - Exit")
choice = int(input("Your choice: "))
if (choice == 0):
    print("Ending...\n")
elif (choice == 1):
    Celsius = float(input("Insert the amount of Celsius: "))
    print (f"{round(Celsius,1)} °C equals to {round((Celsius * 1.8) + 32, 1)} °F\n")
elif (choice == 2):
    Fahrenheit = float(input("Insert the amount of Fahrenheit: "))
    print (f"{round(Fahrenheit, 1)} °F equals to {round((Fahrenheit - 32) / 1.8, 1)} °C\n")
else:
    print ("Unknown option\n")
print ("Program ending.")