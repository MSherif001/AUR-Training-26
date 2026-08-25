stock={}            #dictionar
def menu_show(): # only show menu function
    print("enter 1 to add stock")
    print("enter 2 to remove stock")
    print("enter 3 to show the stock's contents")
    print("enter 4 to exit the program")
    return None

def add_stock(key,value):#only add new/old stock
    b=False
    for key1,value1 in stock.items():
        if(key1==key):
         b=True
    if b ==True:
      stock[key] +=value
    else:
     stock[key]= value

def remove_stock():
    pass
def show_stock():
    pass


#while True:
try:
      with open("stock.txt","r") as f:
       for data in f:
         key,value = data.strip().split(",")
         stock[key] = int(value)
except OSError:
     print("Error while locating the file")
menu_show()
x = input()
if x not in ["1","2","3","4"]:
    
    print("Invalid input")
    #continue
if x == "1":
    
    print("adding stock")
    key = input("Enter the stock name")
    value = input("The quantity: ")
    key.lower()
    add_stock(key,value)
    
elif x == "2":
    
    print("removing stock")
elif x== "3" :
    
    print ("Showing stock")
elif x== "4":
    
    with open("stock.txt","w") as f:
        for key,value in stock.items():
            f.write(f"{key},{value}\n")
    #break        
        




