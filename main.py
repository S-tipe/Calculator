
x = int(input("Upiši vrijednost za x: "))

y = int(input("Upiši vrijednost za y: "))

operation = input("Izaberi matematičku funkciju (+, -, *, /): ")

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)
else:
    print("Provjeri matematičku funkciju.")
