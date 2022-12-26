
print("welcome to my store")
name = input(" what is your name? ")

if not  name == "monkey" or name == "peter" :
   
   
   
   evil_status = input("are you hungry?\n")
    if evil_status == "no" :
        print(" pls get out")
        exit()
    good_deeds = int(input("how many times have you eaten today?\n"))
    if evil_status == "yes" and good_deeds > 2:
      print("your not too hungry to be here !!")
      exit()
    else:
        print("okey!!")
else:
    print(" hi " + name + " what would you like to order?\n" )
menu = input("MENU: star fingers. lemon pepsi. human fingers \n\n\n\n")
if not menu == "star fingers" or menu == "lemon pepsi" or menu == "human fingers":
    print("srry but we dont have that here" )
    exit() 
print("okey " + menu + " it is\n ")
many = input("how many " + menu + " you want?\n")
if menu == "star fingers" :
    prize = 36
if menu == "human fingers" :
    prize = 4
if menu == "lemon pepsi" :
    prize = 27
if not menu == "star fingers" or menu == "lemon pepsi" or menu == "human fingers" :
    print("srry but we dont have that here" )
    exit() 
yes = input("okey " + many + " " + menu + " is that it\n")
if not yes == "yes" :
    total = prize * int(many)
    print("your total will be:$" + str(total))
    print(" heres your "  + menu + " " + name + "")
    print("good bye!!!")
    exit()
else:
    print("then what would you like")

   
