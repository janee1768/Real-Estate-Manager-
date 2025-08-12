# Import library
import pandas as pd
from os.path import exists


def show_menu():
    print("\n-------Real Estate Listing Manager--------")
    print("1. Add Listing")
    print("2. View all Listings")
    print("3. Search Listings (by city or price)")
    print("4. Update a Listing")
    print("5. Delete a Listing")
    print("6. Export listings to CSV")
    print("7. Exit")


def add_listings():
    title = input("Enter property title: ")
    price = input("Enter price: ")
    city = input("Enter city: ")

    #Check price is a number 
    while not price.isdigit():
        print("---Invalid price entered----")
        price = input("Enter price: ") 
    
    price = int(price) #Converting only after its a digit 
      


    #Creating a row 
    data = pd.DataFrame([[title, int(price), city]], columns=["Title", "Price", "City"])

    # Check if the file is already present
    file_exists = exists("property.csv")

    # Save new data to the file
    # If the file doesn't exist → write column names too
    # If it does exist → just add the row, no column names again

    data.to_csv("property.csv", mode="a", index=False, header=not file_exists)
   
    print("\nListings added successfully!!")


def view_listings():
    try:
        data_1 = pd.read_csv("property.csv")

        if data_1.empty:
            print("----No Listings found-----")
            return

        print("-----All Property Listings-------\n")

        # Using a loop to print and rows of the csv file with a gap

        for index, rows in data_1.iterrows():
            print("Title:", rows["Title"])
            print(
                "Price:", rows["Price"]
            )
            print("City:", rows["City"])
            print("\n---------------------\n")

    except FileNotFoundError:
        print("No file is found!")


def search_listings():
     try:
         search_item = input("Search here(by city or by price):  ").strip()
         data = pd.read_csv("property.csv")

         #Try to convert search item to integer 

         if search_item.isdigit():
             
             #Search by price 

             results = data[data["Price"] == int(search_item)]
         else:
             #Search by city (case insensitive)

             results = data[data["City"].str.lower() == search_item.lower()]

         if results.empty:
          print("No listings found!")

         else:
             print("-----Listings found successfully-----")

             for index,rows in results.iterrows():
                 print("Title: ",rows["Title"])
                 print("Price: ",rows["Price"])
                 print("City: ",rows["City"])
                 print("\n--------------------\n")
            
     except FileNotFoundError:
          print("File is not found")


    

def update_listings():
    try:
        data = pd.read_csv("property.csv")
        title_to_update = input("Enter title to update: ").strip()

        # Find the index (row number) of listings where the title matches (case-insensitive)
        match_index = data[data["Title"].str.lower() == title_to_update.lower()].index
        
        #Check if the title exists

        if match_index.empty:
            print("----No listing found----")
            return 
       
        new_price = input("Enter new price: ").strip()
        new_city = input("Enter new city: ").strip()

        #Check if the price is integer 

        if not new_price.isdigit():
            print("-----Invalid price------")
            return 
        
        #Entering the newly updated values in the file 

        data.loc[match_index,"Price"] = int(new_price)
        data.loc[match_index,"City"] = new_city

        data.to_csv("property.csv", index = False)
        print("\n Listings Updated Successfully!!")

    except FileNotFoundError:
        print("File is not found")


def delete_listings():
    try:
        data = pd.read_csv("property.csv")
        title_to_delete = input("Enter listings(title) to delete: ").strip()

        #Checking if the lisiting exists in the file 

        matching_rows = data[data["Title"].str.lower() == title_to_delete.lower()]

        if matching_rows.empty:
            print("----Listing not found-----")
            return 
        
        #Show what will be deleted 

        print("\nThis will be deleted..\n")
        print(matching_rows)

        #Confirm before deleting
        confirm = input("Do you want to delete this (yes/no): ").strip().lower()
        
        if confirm != "yes":
            print("---Deletion is stopped---")
            return 
        
        #Only the rows that do not match will not be deleted 
        data = data[data["Title"].str.lower() != title_to_delete.lower()]

        data.to_csv("property.csv",index = False)
        print("\n Listing deleted successfully")

    except FileNotFoundError:
        print("File is not found!!")

def export_listings():
     data = pd.read_csv("property.csv")

     #Confirmation from user 
     confirm = input("Do you want to export the file?(yes/no): ").strip().lower()
     
     if confirm != "yes":
         print("--Export is denied--")
         return 
     
     data.to_csv("exporting.csv",index = False)
     print("---File exported successfully---")

# main app loop
while True:
    show_menu()
    choice = input("Enter your choice(1-7): ")
    if choice == "1":
        add_listings()
    elif choice == "2":
        view_listings()
    elif choice == "3":
        search_listings()
    elif choice == "4":
        update_listings()
    elif choice == "5":
        delete_listings()
    elif choice == "6":
        export_listings()
    elif choice == "7":
        print("Goodbye!")
        break
    else:
        print("Invalid Input. Try again!")
