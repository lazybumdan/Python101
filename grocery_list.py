def groceries():
    grocery_list = []
    while True:
      user_choice = int(input(
          "What input would you like to do?\n 1. Add an item to the grocery list\n 2. Remove an item from the grocery list\n 3. Display the grocery list\n Enter you choice here:"))
      if user_choice == 1:
          grocery_item = input("Select an item:")
          grocery_list.append(grocery_item)
      elif user_choice == 2:
          grocery_list.remove(grocery_item)
      elif user_choice == 3:
          print(grocery_list)
          break



groceries()
