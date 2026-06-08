# Multiplication table of numbers from 2 to 12
for num in range(2, 13):
    print(f"Multiplication table for {num}:")
    for n in range(1, 13):
        product = num * n
        print(f"{num} x {n} = {product}")
    print()
