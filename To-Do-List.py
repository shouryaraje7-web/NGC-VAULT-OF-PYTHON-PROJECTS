print("NextGenCoder's simple To-Do-List code")
print()
print("If you finished the work just type Done infront of it." )
print()
run = True
while run == True:
    
    task = input(" Enter Task: ")
    print (f" Task is: {task}" )
    print()
    
    Did = input(" Enter 'done' when above task completed: ")
    
    if Did == "Done"or"done":
        print(f"done: {task}" )
        print()
        