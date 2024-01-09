import time
import sys

Border = ("*" * 42)

def intro():
    
    print(Border)
    print("**\tWelcome to the Snakes Cafe!\t**")
    print("**\tPlease see our menu below.\t**")
    print("**")
    print('**\tTo quit at any time, type "quit"**')
    print(Border)
    print("")
    
def orderText():
    
    print(Border)
    print("**\tWhat would you like to order?\t**")
    print(Border)
    print("")

def menu(category, meals):
    
    print(category)
    print("-" * 10)
    
    for meal in meals:
        print(meal)
        
    print()

def delay_print(a):
    for b in a:
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(0.10)    

def userOrder(Appetizers, Entrees, Desserts, Drinks):
    
    orderNum = 0
    retry = 0
    done = False
    Order = []
    
    while done is False:
        
        try:
            choice = input("Your Choice?: ")
            
            if choice.lower() in ['q' , 'quit']:
                
                if retry == 1 and orderNum == 0:
                    print("Well I warned you . . .\n")
                    time.sleep(0.5)
                    print("Probably . . .\n")
                    time.sleep(0.5)
                    delay_print("SEE YOU BACK IN LUMBY\n")
                    exit()
                    
                elif orderNum == 0:
                    print(". . .\n")
                    time.sleep(0.5)
                    print("So you came here to not get anything . . ?\n")
                    time.sleep(1)
                    print("Ok I'm just going to pretend this was a mistake . . .\n")
                    time.sleep(0.5)
                    delay_print("Let's try that again.\n\n")
                    print("WARNING! This shopkeeper doesn't like non paying customers! Please get something!")
                    retry += 1
                    continue
                
                else:
                    done = True
                    outro()

            if choice in Appetizers + Entrees + Desserts + Drinks:
                
                Order.append(choice)
                count = Order.count(choice)
                print(f"** {count} order of {choice} has been added to your meal **")
                orderNum+= 1
                
            else:
                print("Sorry friend we don't have that here.")
                time.sleep(0.5)
                delay_print("Can't really tell you that I can only read case-sensitive . . .")
                time.sleep(1)
                print()
                        
        except ValueError:
            print("Sorry I didn't quite catch that can you tell me again?")
        
def outro():
    
    print("Ok see you later!")
    exit(0)
        
def main():

    Appetizers = ["Wings", "Cookies", "Spring Rolls"]
    Entrees = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
    Desserts = ["Ice Cream", "Cake", "Pie"]
    Drinks = ["Coffee", "Tea", "Unicorn Tears"]
    
    intro()
    
    menu("Appetizers", Appetizers)
    menu("Entrees", Entrees)
    menu("Desserts", Desserts)
    menu("Drinks", Drinks)
    
    orderText()
    userOrder(Appetizers, Entrees, Desserts, Drinks)
    
main()