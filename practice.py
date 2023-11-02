x = input("Enter your message: ")
x_x = x.upper().split()
if x_x[0] == "SAVE":
    print("OK")
    if x_x[0] == "READ":
        print(x[5:])
else:
    print("There might be something wrong, please try again")
