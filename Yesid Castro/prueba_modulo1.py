while True:
    clear()
    print("""\nINVENTORY MANAGEMENT 
            \nSelect an option:\n
            1. Add Product.
            2. Management Product.
            3. Total Inventory
            \nPress key Enter for exit. """)
    
    option_input = input()
    if option_input == "":
        break
    try:
        option = int(option_input)
    except ValueError:
        input("Invalid input. Press ENTER to return to menu.")
        continue

    if option == 1:
        clear()
        exit = "yes"
        while exit == "yes" or count < 5:
            print("Add Product\n")
            name = ""
            while name == "":
                name = input("Name:").strip()
            price = check_number(input("Price:"))
            stock = check_number(input("Stock:"))
            count += 1

            product = {"ID": count, "name": name, "price": price, "stock": stock}
            products.append(product)

            print("\nProduct entered SUCCESSFULLY.\n")
            minimum = 5 - count
            if count < 5:
                print(f"Please, enter {minimum} more products")
            else:
                exit = input("Do you want to enter a new product? yes/no:").strip().lower()

    elif option == 2:
        clear()
        if len(products) == 0:
            input("Please enter products, Menu - option '1'")
        else:
            print("Check Product\n")
            print_logs(products)
            exit = "yes"
            while exit == "yes":
                check_product = input("\nEnter the name of the product you want to search:")                
                product_found = False
                
                for product in products:
                    if check_product == product["name"]:
                        price_product = product["price"]
                        stock_product = product["stock"]
                        id_product = product["ID"]
                        print("\nPRODUCT DETAILS:\n")
                        print("-" * 67)
                        print(f"{'ID':<5} {'Name':<20} {'Price':<20}{'Stock':<20}")
                        print("-" * 67)
                        print(f"{id_product:<5} {check_product:<20} {price_product:<20} {stock_product:<20}")
                        print("-" * 67)
                        product_found = True
                        
                        while True:
                            try:
                                option_product = int(input("Select an operation:\n1. Update\n2. Delete\n3. Exit\n"))
                            except ValueError:
                                print("Please enter a valid number.")
                                continue
                                
                            if option_product == 1:
                                print("Update Price\n")
                                change_price = check_number(input(f"Enter the new price for '{check_product}': "))
                                product["price"] = change_price
                                print("Price changed SUCCESSFULLY.")
                                break

                            elif option_product == 2:
                                print("Delete Product\n")
                                confirm = input("Are you sure you want to delete this product? yes/no:").lower()
                                if confirm == "yes":
                                    products.remove(product)
                                    print("Product removed SUCCESSFULLY.")
                                else:
                                    print("Operation cancelled.")
                                break
                            elif option_product == 3:
                                break
                            else:
                                print("Please, Enter a valid option.")
                        break
                        
                if not product_found:
                    print("Product not found, try again")
                else:
                    exit = input("Do you want to find another product? yes/no:").lower()
                    if exit != "yes":
                        break
        
    elif option == 3:
        clear()
        if len(products) == 0:
            print("Inventory is empty")
            input("Please enter products, Menu - option '1'")
        else:
            print("Calculate inventory\n")
            total = sum(map(lambda x: x["price"] * x["stock"], products))
            print(f"\nThe total price of the inventory is: ${total}")
            input("\nPress ENTER to return to the Menu")
    else:
        print("Please, enter a valid option.")
