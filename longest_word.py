'''
Write a Python program that finds the longest word in a sentence.
If there are multiple words with the same maximum length, print the first one.
'''
sentence=input("Enter sentence: ")
sentence=sentence.split(" ")
maxW=0
my=""
for word in sentence:
    if len(word)>maxW:
        my=word
        maxW=len(word)

print(f"Longest Word : {my}")
print(f"Length : {maxW}")