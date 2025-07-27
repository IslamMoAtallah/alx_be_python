def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
def add_item(shopping_list):
    item=input("Enter your item to add : ").strip()
    if item:
        shopping_list.append(item)
    else:
        print("Invalid item. please try again.")
def remove_item(shopping_list):
    item=input("Enter item to remove : ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from the shopping ")
    else:
        print(f"{item}item not found please try again.")
def view_list(shopping_list):
    if not shopping_list:
        print("Your shopping list is currently empty.")
    else:
        print("\nYour Shopping List:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
            
        elif choice == '3':
            view_list(shopping_list)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()       
