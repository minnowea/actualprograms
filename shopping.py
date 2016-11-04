
main_shopping_list = {"Target":["utensils","frying pan"], "Whole Foods": 
["shrimp", "cheese"], "Safeway": ["pasta", "garlic"]}




def main_menu():
    print """
    0 - Main Menu
    1 - show all lists
    2 - show specific 
    3 - add a new shopping list 
    4 - add add an item shopping list
    5 - remove item shopping list
    6 - remove list
    7 - exit 
    """



def show_all_list():
    print main_shopping_list


def show_a_specific_list(key):
    if key in main_shopping_list:
        return main_shopping_list[key]
    else: 
        return "List can not be found"    


def add_a_new_shopping_list(key):
    shopping_list=[]
    if key not in main_shopping_list:
        main_shopping_list[key]=shopping_list
        return main_shopping_list
    else:
        return "List name in use"     



def add_an_item_shopping_list(key, item):
    if key in main_shopping_list:
        if item in main_shopping_list[key]:
            return "item is already in list"
        else:
            shopping_list=main_shopping_list[key]
            shopping_list.append(item)
            return shopping_list
    else:
        return " List can not be found"    
 

def remove_item_shopping_list(key, item):
    if key in main_shopping_list:
        if item in main_shopping_list[key]:
            shopping_list=main_shopping_list[key]
            shopping_list.remove(item)
            return shopping_list
        else: 
            return "Item can not be removed because not found"
    else:
        return "List can not be found"        




def remove_list():
    pass 






def main():

    # main_menu()
    # show_all_list()    # print add_an_item_shopping_list("Safeway", "lemons")
    # print show_a_specific_list("Target")
    # print add_a_new_shopping_list("Safeway")
    # print add_an_item_shopping_list("Safeway", "lemons")
    print remove_item_shopping_list("Sephora","lemons")

    # while True:













if __name__ == '__main__':
    main()