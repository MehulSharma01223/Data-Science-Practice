sentence = input("Write a sentence :-")


words = sentence.split()
longest= ""
for i in words:
    if len(i) > len(longest):
        longest = i 

print("big words in sentence :" , longest)

