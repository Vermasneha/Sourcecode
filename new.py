#function
def welcome( *match ):
    print(“\n Total number of matches are : “,len(match))
    for n in match:
        print(“Score :”,n )


# Passing 9 parameters
welcome(10,9,8,9,7,6,9,8,5)

# Passing 6 parameters
welcome(4,5,9,4,10,5)
