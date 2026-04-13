sentence =input("Enter a sentence : ")
checked = ""
for i in sentence :
    if i not in checked:
        print(i,":",sentence.count(i))
        checked = checked +i  