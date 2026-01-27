import Arithmatic

Result=0

Value1=int(input("Enter a first number:"))
Value2=int(input("Enter a second number:"))

Result=Arithmatic.Addition(Value1,Value2)
print("Addition is:",Result)

Result=Arithmatic.Subtraction(Value1,Value2)
print("Subtraction is:",Result)

Result=Arithmatic.Multiplication(Value1,Value2)
print("Multiplication is:",Result)

Result=Arithmatic.Division(Value1,Value2)
print("Division is:",Result)