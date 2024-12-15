print("Fahrenheit to Celsius Converter Program")
F = eval(input("Enter temperature in Fahrenheit : "))

C = (F-32) * 5 / 9
print("The conversion of", F, "degrees Fahrenheit is", C, "degrees Celsius.")


print(f"The conversion of {F} degrees Fahrenheit is {round(C,2)} degrees Celsius.")