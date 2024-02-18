def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

print("Select an operation: ")
print(" 1. ADDITION")
print(" 2. SUBTRACTION")
print(" 3. MULTIPLICATION")
print(" 4. DIVISION")

while True:
    choice = input("Enter your choice : 1/2/3/4 ")
    
    if choice in ('1' , '2' , '3' , '4'):
        
        try:
            num1=float(input("Enter first number: "))
            num2=float(input("Enter second number: "))
            
        except ValueError:
            print("Invalid input !! Enter a proper number !!")
            continue
            
        if choice == '1':
            print(num1, "+" ,num2, "=", add(num1,num2))
            
        elif choice == '2':
            print(num1, "-", num2 ,"=", sub(num1,num2))
        elif choice == '3':
            print(num1, "*", num2 ,"=", multiply(num1,num2))
            
        elif choice == '4':
            print(num1, "/", num2 , "=", divide(num1,num2))
            
        next_cal = input (" Let's do next calculation ? Yes / No ? ")
        print('\n')
        if next_cal == "No":
            break
            
    else:
        print("Invalid input ")
