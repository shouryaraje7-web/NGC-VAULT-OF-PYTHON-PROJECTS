#About me
print("This is a simple spam comment detector made by NextGenCoder.")
print()

#Spam keywords
s1 = "link" 
s2 = "otp" 
s3 = "free gift" 
s4 = "password" 

#loops to give infinite comment options
run = True
while run == True:

#input to type user's comment 
    comment = input("Type your comment: ")
    clean_comment = comment.lower()

#Conditions for spam comment
    if s1 in clean_comment or s2 in clean_comment or s3 in clean_comment or s4 in clean_comment:
        print("This is a spam comment")
        print()
        
    else:
        print("This comment is not a spam")
        print()   
 #Program end       