def groceries():
    grocery_list = []
    while True:
      add_items = str(input("What items do you need from the store?: "))
      grocery_list.append(add_items)
      finished_list = input("Are you done? Y/N")
      if finished_list == "N":
          continue
      elif finished_list == "Y":
          print(grocery_list)
          break
      else:
          continue


groceries()
