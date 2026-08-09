#name,math,eng,dutch,science
print("Welcome to your Resultzz!")
report_cards=(("Tanshi",100,96,56,99),
              ("Jay",10,96,46,19),
              ("Austin",90,96,36,59),
              ("Love",60,96,56,99),
              ("Paris",80,66,6,79),
              ("Rauf",20,76,56,89))
while True:
    name=input("Enter your name: ").capitalize()
    found=False
    for i in report_cards:
        if name in i[0]:
            print(f"Here are your results: Math={i[1]},English={i[2]},Dutch={i[3]},Science={i[4]}")
            found=True
            break

    if found==False:
        print("No records found")
    stop=input("Do You wish to continue?yes/no ").lower()
    if stop=="no":
        print("Bye")
        break
    elif stop=="yes":
        print("Welcome to your Resultzz!")
        continue
    else:
        print("Invalid!!")
        continue
    
