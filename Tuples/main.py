#City Name, Ticket Price Per Person, Money For Food Per Person, Hotel Price Per Person A Night, Overall /10 Rating

data=(("Paris",250,100,50,8),
    ("Amsterdam",100,70,30,8),
    ("Newyork",300,150,100,7),
    ("Moscow",200,50,40,9),
    ("Dubai",250,100,80,10))

city=input("Enter The City You Want To Go To ").capitalize()
for row in data:
    if row[0]==city:
        print(f"City Name: {row[0]} ")
        print(f"Ticket Price Per Person: {row[1]}")
        print(f"Money For Food Per Person: {row[2]} ")
        print(f"Hotel Price Per Person A Night: {row[3]}")
        print(f"Overall /10 Rating: {row[4]}")
if city not in data:     
    print("not found")