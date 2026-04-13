with open('test.txt','r') as f:

    size_to_rea = 200
    f_contents = f.read(size_to_rea)

    while len(f_contents):
        print(f_contents, end ='')
        f_contents = f.read(size_to_rea)
