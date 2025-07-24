Input = input("Type something random: \n")

boole = type(Input) is str

if boole == True:
    print("You typed a string.")
else:
    print("You did not type a string.")
