studentData={"sam":23,
             "rohan":29,
             "abriel":22,
             "shreya":25,
             "eshaani":28,
             "max":5,
             "edward":11,
             "harry":13,
             "muhammad":10,
             "Sarah":24,
             "Emma":13,
             "Emily":19,
             "Layla":13,
             "Monica":7,
             "Ross":27,
             "Rachael":15}

while True:
    name=input("Enter name to check result: ").lower().strip()
    if name in studentData:
        print(f"{name} scored {studentData[name]} out of 30.")
        
    else:
        print(f"{name}'s result not found.")