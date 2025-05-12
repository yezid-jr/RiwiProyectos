#IMPORTS
import os
#STATEMENT
name = ""
count = 0
products = []
#FUNCTIONS


def clear():
  if os.name == "nt":  # Windows
    os.system("cls")
  else:  # Linux/Mac
    os.system("clear")

def check_number(number):
    while True:
        try:
            number = float(number)
            if number < 0:
                number = input("Please, enter a positive number:\n")
            else:
                return number
        except:
            number = input("Please, enter a valid number:\n")

def print_logs(products):
    print(f"{'ID':<5} {'Name Product':<20}")
    print("-" * 23)
    for product in products:
        id_product = product["ID"]
        name_product = product["name"]
        print(f"{id_product:<5} {name_product:<20}")

while True:
    print("""\nINVENTORY MANAGEMENT 
            \nSelect an option:\n
            1. Add Product.
            2. Check Product.
            3. Update Price.
            4. Delete Product.
            5. Calculate inventory.
            \nEnter any key for exit. """)
    option = int(input())

    if option == 1:
        exit = "yes"
        while exit == "yes" or count < 5:
            print("Add Product\n")
            
            while name == "":
                name = input("Name:").strip()
            price = check_number(input("Price:"))
            stock = check_number(input("Stock:"))
            count += 1

            product = {"ID": count, "name": name, "price": price, "stock": stock}
            products.append(product)

            print("\nProduct entered SUCCESSFULLY.\n")
            name = ""
            minimum = 5 - count
            if count < 5:
                print(f"Please, enter {minimum} more producs")
            else:
                exit = input("Do you want to enter a new product? yes/no:").strip().lower()

    elif option == 2:
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
                        stok_product = product["stock"]
                        id_product = product["name"]
                        print("\nPRODUCT DETAILS:\n")
                        print("-" * 67)
                        print(f"{'ID':<5} {'Name':<20} {'Price':<20}{'Stock':<20}")
                        print("-" * 67)
                        print(f"{id_product:<5} {check_product:<20} {price_product:<20} {stok_product:<20}")
                        print("-" * 67)
                        product_found = True
                        break
                
                if product_found == False:
                    print("Poduct not found, try again")
                else:
                    exit = input("Do you want to find another product? yes/no:").lower()
                    if exit == "yes":
                        continue
                    else:
                        break
    elif option == 3:
        if len(products) == 0:
            input("Please enter products, Menu - option '1'")
        else:
            print("Update Price\n")
        
    elif option == 4:
        if len(products) == 0:
            input("Please enter products, Menu - option '1'")
        else:
            print("Delete Product\n")
        
    elif option == 5:
        if len(products) == 0:
            input("Please enter products, Menu - option '1'")
        else:
            print("Calculate inventory\n")
        
    else:
        print("Please, enter a valid option.")