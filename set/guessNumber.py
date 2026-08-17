numbers={1,5,7,8,9}
score=0
temp=set()
print(f"Your guess Game!Only Unique values.\nOnly {len(numbers)} attempts")
for i in range(len(numbers)):
    guess=int(input("Enter a guess(1-10): "))
    if guess in temp:
        print("You already guessed that!")
        continue
    if guess in numbers:
        score+=1
        print(f"Score: {score}")
        temp.add(guess)
    else:
        print("Incorrect")
    
if score==5:
    print("You got them all!")
else:
    print("You couldn't guess them all.")