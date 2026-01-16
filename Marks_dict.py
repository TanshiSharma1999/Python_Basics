my_dict = {}

subjects = ["Maths", "Science", "English", "History", "French"]

for subject in subjects:
    my_dict[subject] = float(input(f"How much did you score in {subject}? "))

def analyze_results():
    min_sub = min(my_dict, key=my_dict.get)
    max_sub = max(my_dict, key=my_dict.get)
    avg = sum(my_dict.values()) / len(my_dict)

    print(f"\nMinimum marks scored: {min_sub} = {my_dict[min_sub]}")
    print(f"Maximum marks scored: {max_sub} = {my_dict[max_sub]}")
    print(f"Average marks scored: {avg:.2f}")

show = input("Do you want to print Marksheet? Y/N ").upper()

if show == "Y":
    print("\nYour Marksheet:")
    for subject, marks in my_dict.items():
        print(f"{subject}: {marks}")

analysis = input("\nDo you want to run a brief analysis on the result? Y/N ").upper()
if analysis == "Y":
    analyze_results()
else:
    print("Thank you for your time!")
