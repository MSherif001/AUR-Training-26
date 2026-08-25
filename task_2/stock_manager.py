stock={}            #dictionar

def menu_show(): # only show menu function
    print("enter 1 to add stock")
    print("enter 2 to remove stock")
    print("enter 3 to show the stock's contents")
    print("enter 4 to exit the program")
    return None

def add_stock(key,value:int):#only add new/old stock
    
    if key in stock:
      stock[key] +=int(value)
    else:
      stock[key]= int(value)

def remove_stock(key,value): #remove only items and quantities from dict
     if key in stock:
          if stock[key]-value>=0:
           stock[key]-=value
           print("Done")
          else:
            print("Quantity cannot be less than 0!")
     else :
         print ("Item not found")
         
def define_stock():#only to read stock from the txt fike
     with open("stock.txt","r") as f:
           for data in f:
             key,value = data.strip().split(",")
             stock[key] = int(value)
             
def print_stock():  #only printing the stock in the end
    number = 1
    for keys,values in stock.items():
        print(f"{number}. {keys}: {values}")
        number += 1
        
b= True
try:
      define_stock()
except OSError:
     print("Error while locating the file")
     b=False
#the loop of the work:
while b:

 menu_show()
 
 x = input()
 
 if x not in ["1","2","3","4"]:
    
    print("Invalid input")
    continue

 if x == "1":
    
    print("adding stock")
    print_stock()
    key = input("Enter the stock name: ")
    value = input("The quantity: ")
    key = key.lower()
    add_stock(key,value)
    
 elif x == "2":
    
    print("removing stock")
    print_stock()
    key = input("Enter the stock name: ")
    quant= input("quantity to be removed: ")
    key =  key.lower()
    
    remove_stock(key,int(quant))
    
 elif x== "3" :
    
    print ("Showing stock")
    print_stock()
    
 elif x== "4":
    
    with open("stock.txt","w") as f:
        for key,value in stock.items():
            f.write(f"{key},{value}\n")
    print("Saved!")
    
    break        