pattern = int(input("Enter the size of the pattern: "))
row = 0 
while row < pattern : 
    for col in range (pattern):
        print(f"*", end="")
    print()
    row +=1 
