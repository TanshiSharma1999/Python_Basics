matrix = []

print("Enter 9 numbers:")

for i in range(3):
    row = []
    for j in range(3):
        num = int(input("Enter a number"))
        row.append(num)
    matrix.append(row)

# Display row by row
for row in matrix:
    print(row)