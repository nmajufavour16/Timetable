# Program to print multiplication table of numbers from 2 to 12

for num in range(2, 13): # This checks for the numbers from 2 and 12
    print(f"Multiplication table for {num}:")
    
    # This code block takes each number within the range above and multiplies with the range below
    for n in range(1, 13):
        product = num * n
        print(f"{num} x {n} = {product}")
    print()
