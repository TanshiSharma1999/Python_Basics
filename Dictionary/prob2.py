# Write a Python program to remove a specific key from a dictionary,
student_score={"Sam":100,"Austin":99,"Eshi":98,"Ram":97}
print(student_score)
student_score.pop("Ram")
print(student_score)

#  retrieve all key-value pairs, and check whether a given key exists.

for key in student_score:
    print(f"{key} scored {student_score[key]}% this term.")

if "Austin" in student_score.keys():
    print(f"{"Austin"} scored {student_score["Austin"]}% this term.")
else:
    print("not found")

if "Ram" in student_score.keys():
    print(f"{"Ram"} scored {student_score["Ram"]}% this term.")
else:
    print("not found")