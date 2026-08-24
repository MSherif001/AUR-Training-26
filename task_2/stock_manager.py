try:
    with open("stock.txt","r") as f:
     stock = {f.read()}
except OSError:
    print("Error while locating the file")
print(stock)    
