num1 = int(input("Enter your first number: "))

num2 = int(input("Enter your second number: "))

operation = input("Choose the operation (+, -, *, /): ")

match operation : 
    case "+":
        result = num1 + num2 
        print(f"The result is :{result}")
    case "-":
        result = num1 - num2
        print(f"The result is : {result}")
    case "*" :
        result = num1 * num2 
        print (f"The result is : {result}")
    case "/": 
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else :
            result = num1/num2 
            print (f"The result is {result}")
    case _: 
        print("Infalid operation. Please choose from +, -, *, /." )