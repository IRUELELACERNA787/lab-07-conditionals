value1 = input("Enter a first value: ")
value2 = input("Enter a second value: ")
modifier = input("Enter your operation (mul, div, or mod): ")

mulVal = str(float(value1) * float(value2))
divVal = str(float(value1) / float(value2))
modVal = str(float(value1) % float(value2))


if(modifier == "mul"):
    print(mulVal)
elif(modifier == "div"):
    print(divVal)
elif(modifier == "mod"):
    print(modVal)
else:
    print("INVALID OPERATION")