import random
while True:
    
    try: 
        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;<=>?@[]^_`{|}~" 
        length = int(input("Set length of your password: "))
        if length < 0:
            print("Nice try! but number length should be greater than zero.")
            print()
            continue
        password = random.choices(chars,k = length)
        passw = ''.join(password)
        print(f"Password generated is {passw}")
        break
       
    except ValueError:
        print("Only Numbers Allowed")
        print()