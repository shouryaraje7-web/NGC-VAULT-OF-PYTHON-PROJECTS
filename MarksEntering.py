run = True
while run == True:
    a = input("Name: ")
    b = input("Marks: ")

    if b.isdigit():
        b = int(b)

        if b <= 33:
            print(f"{a} is failed")
            print()
    
        else:
            print(f"{a} is passed") 
            print()

    else:
        print("Error add number only for marks")
        print()
               