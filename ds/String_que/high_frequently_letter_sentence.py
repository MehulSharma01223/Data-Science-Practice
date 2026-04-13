sentence = input("Enter a sentence :")

Max_ch = ""
Max_count = 0
for ch in sentence:
    if ch ==" ":
        continue
    count= sentence.count(ch)

    if count>Max_count:
        Max_ch = ch
        Max_count = count

print("there are max letter is :",Max_ch)
print("there are max letter  num is :",Max_count)

