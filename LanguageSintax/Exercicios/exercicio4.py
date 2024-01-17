# LISTA DE COMPRAS
import os

wishlist = []
list_done = False

while not list_done:
    option = input("1 - Insert in the wishlist\n2 - Remove an item\n3 - Show wishlist\n4 - Clear screen\n0 - Quit\nType an option: ")
    
    if(option == '1'):
        wishlist.append(input("Item to insert: "))

    elif(option == '2'):
        # item = input("Item to remove: ")
        # if(item in wishlist):
        #     wishlist.remove(item)
        # else:
        #     print("The item isn't in the wishlist.")
        index = input("Item's index: ")
        
        try:
            if(len(wishlist) > 0):
                wishlist.pop(int(index))
        except:
            wishlist.pop()

    elif(option == '3'):
        if len(wishlist) > 0:
            for index, item in enumerate(wishlist):
                print(f"Item {index}: {item}")
        else:
            print("Empty list")

    elif(option == '4'):
        os.system("cls")
    
    else:
        if(option != '0'):
            print("Invalid option")
        else:
            print("Goodbye!")
            list_done = True
    print("\n")