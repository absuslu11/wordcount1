gameover = False

while gameover == False:
    
    input1 = input("Please enter a prompt under 200 characters: ")
    list1= list(input1)
    carval = 0


    for i in list1:
        carval += 1

   

    if carval < 200:
        print(carval)
        gameover = True
    else:
        print("Your charcater value exceeds allowed space.")