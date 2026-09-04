while True:
    #about
    print('''
    ---Cafe Management System---
    ''')
    
    print('''
    __MENU__
    ''')
    
    print('''
    Tea    ₹20
    Burger ₹40
    Coffee ₹20
    Pizza  ₹60
    ''')
    choice = input("Enter what you want: ")
    bill = 0 
    
    #Tea
    if choice.lower() == "tea":
        quant = int(input("Enter quantity: "))
        if quant <= 0:
            print("In-valid number") 
            continue
        print(f"{quant} {choice.lower()} are ordered")
        print("Just wait for few minutes")
        bill = 20*quant
        print(f"Total Bill is ₹{bill}")
            
        #Burger    
    elif choice.lower() == "burger":
        quant1 = int(input("Enter quantity: "))
        if quant1 <= 0:
            print("In-valid number") 
            continue
        print(f"{quant1} {choice.lower()} are ordered")
        print("Just wait for few minutes")
        bill = 40*quant
        print(f"Total Bill is ₹{bill}")
             
        #coffee     
    elif choice.lower() == "coffee":    
        quant2 = int(input("Enter quantity: "))
        if quant2 <= 0:
            print("In-valid number") 
            continue
        print(f"{quant2}   {choice.lower()} are ordered")
        print("Just wait for few minutes")
        bill = 20*quant
        print(f"Total Bill is ₹{bill}")
            
        #pizza    
    elif choice.lower() == "pizza":
        quant3 = int(input("Enter quantity: "))
        if quant3 <= 0:
            print("In-valid number") 
            continue
        print(f"{quant3} {choice.lower()} are ordered")
        print("Just wait for few minutes")
        bill = 60*quant
        print(f"Total Bill is ₹{bill}")
      
       #error         
    else:
        print("Error 404: pls check that you've spelled word correctly!")  
             