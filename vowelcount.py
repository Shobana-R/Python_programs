''' Take input from user.count the vowels in the string'''
string1=input("Enter a string: ")
set1=set("aeiou")
vowelcount=0
string1=string1.lower()
for chr in string1:
    if chr in set1:
        vowelcount=vowelcount+1
print("Number of vowels in the text is ",vowelcount)
