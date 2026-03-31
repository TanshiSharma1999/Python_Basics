# Linear Search function

def linearSearch(arr, targetVal):
    for i in range(len(arr)):
        if arr[i] == targetVal:
            return i
    return -1

mycountries = ["japan","france","germany","spain","italy"]

# 2 chances using for loop
for attempt in range(2):
    country = input("Guess a country that I wish to travel: ").lower()

    result = linearSearch(mycountries, country)

    if result != -1:
        print("That is", result + 1, "on my list")
        break
    else:
        if attempt < 1:
            print("Wrong guess! Try again.")
        else:
            print("No chances left. Not found.")
