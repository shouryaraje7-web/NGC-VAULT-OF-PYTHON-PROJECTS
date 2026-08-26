run = True
while run == True:


    marks = int(input("Type Marks: "))

    if marks < 0 or marks > 100:
        print("Invalid marks entered")
        print()
    
    elif marks > 90 and marks < 100:
        print("Excellent!") 
        print()
    
    elif marks > 80 and marks < 90:
        print("A") 
        print()    

    elif marks > 70 and marks < 80:
        print("B") 
        print()
    
    elif marks > 60 and marks < 70:
        print("C") 
        print()

    elif marks > 50 and marks < 60:
        print("D")
        print()
     
    elif marks < 50:
        print("F")
        print()