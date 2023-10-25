from art import logo

print(logo)

operations = ["+", "-", "*", "/"]

def calculator(first_num, operation, second_num):
    if operation == '+':
        return first_num+second_num
    elif operation == '-':
        return first_num-second_num
    elif operation == '*':
        return first_num*second_num
    elif operation == '/':
        return first_num/second_num

keep_going = 1

first_num = int(input("What's the first number?: "))

while keep_going > 0:
   for operators in operations:
    print(operators)
   operation = input("Pick an operation: ")
   second_num = int(input("What's the second number? ")) 
   result = calculator(first_num, operation, second_num)
   print(f"{first_num} {operation} {second_num} = {result}") 

   next = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
   if next == 'y':
      first_num = result
   else:
      keep_going = 0 