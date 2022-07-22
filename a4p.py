#########################
# Author: Zouber Ismail
# Assignment 3 
# Date july 11 2022
#########################
import doctest
import pdb;
import logging;

LOG = logging.getLogger(__name__)
logging.basicConfig()
logging.basicConfig(level=logging.DEBUG)
LOG.setLevel(logging.DEBUG)

product_list = [["a", "b", "c","d"], ["d", "e", "f","f"]]
                

def load_inventory(filename):
    """
    Loads and re-initializes product_list array from a file
    Args: 
        -Filename
    Returns: None
    
    >>> product_list = load_inventory("test.txt")
    >>> product_list
    [['Zouber', 'sfdf', 32, 12], ['John', 'qeqe', 34, 24]]
    

    """
    global product_list
    # opening a text file
    file1 = open(filename, "r")
  
    
    count = 0
    line_count = 0
    lines = file1.readlines()
  
    product_list = []
    individual_list = [None for i in range(4)]
    # Loop through the file line by line
    #for x in range(len(lines)): 
    for line in lines:
        LOG.debug(f"{count}, {product_list}, {individual_list}")
        #pdb.set_trace()
        individual_list[count] = line.strip('\n')
        
        if count == 2 or count == 3:
            individual_list[count] = int(individual_list[count])
        count+= 1    
        if count == 4:
    
            product_list.append(individual_list)
            count = 0
            individual_list = [None for i in range(4)]
        
        #purchase_num = int(line_vals[1].strip('#'))
        #product_list[purchase_num-1][x].append() = lines[x]
    
    
    #num = product_list[1][0]
    #print(num)  
    file1.close() 
    return product_list
    
    
def save_inventory(filename):
    
    """
    Save product_list array into a file
    Args: 
        -Filename
    Returns: None
    >>> save_inventory("save.txt")
    'Zouber'
    """
     
    global product_list
    
    with open(filename, 'w') as f:
        
        f.truncate(0)
        for product in product_list:
            for info in product:
    
                f.write("%s\n" % str(info))
        

    
    file1 = open(filename, 'r')
    lines = file1.readlines()
    file1.close()
    return lines[0].strip('\n')
def add_new_product(name,desc,price, stock):
    
    """
    Add a new product to product_list array 
    Args: 
        -Filename
        -str, name of product 
        -str, product description
        -int, price of product
        -int, number of products left  
    Returns: bool, returns wether units were added or not

    """
    
    new_product = [name,desc,price,stock]
    lower_name = name.lower()
    not_in_list = True

    for x in range(len(product_list)):
        for j in range(len(product_list[x])-2):
            if lower_name == product_list[x][j].lower():
                not_in_list = False
    if not_in_list == True:
        product_list.append(new_product)
        return True
    return False
            
def remove_product(name):
    """
    Remove product from product_list array
    Args:
        -str, name of product
    Returns: bool, returns wether product was removed or not
    """
    lower_name = name.lower()

    for x in range(len(product_list)):
        for j in range(len(product_list[x])-2):
            if lower_name == product_list[x][j].lower():
                product_list.pop(x)
                return True
     
    return False
def add_product_stock(name, stock):
    
    """
    Add units to product to product_list array 
    Args: 
        -Filename
        -str, name of product 
        -int, number of units to add to the product
    Returns: bool, returns wether units were added or not

    """
    lower_name = name.lower()
    units = int(stock)

    for x in range(len(product_list)):
        for j in range(len(product_list[x])-2):
            if lower_name == product_list[x][j].lower():
                product_list[x][3] += int(units)
                return True
     
    return False
     
def sell_product(name, units):
    
    
    """
    Remove units of a product in product_list array 
    Args: 
        -Filename
        -str, name of product 
        -int, number of units to remove to the product
    Returns: bool, returns wether units were removed or not

    """
    lower_name = name.lower()
    units = int(units)
    
    
    for x in range(len(product_list)):
        for j in range(len(product_list[x])-2):
            if lower_name == product_list[x][j].lower() and product_list[x][3] >= units:
                product_list[x][3] -= units
                return True
    return False

def list_products(keyword):
    """
    Prints product specified by keyword 
    Args: 
        -Filename
        -str, name of product or description
        
    Returns: None

    """
    lower_name = keyword.lower()
    selected = [None for i in range(4)]
    titles = ["Name: ","Description: ","Price: ", "Stock: "]
    if keyword == '*':
        for x in range(len(product_list)):
            for j in range(len(product_list[x])):
                print(titles[j]+ str(product_list[x][j])+"\n")
     
    else:   
        for x in range(len(product_list)):
            for j in range(len(product_list[x])-2):
                if lower_name == product_list[x][j].lower():
                    selected = product_list[x]
        print(f""" Name: {selected[0]} \n
            Description:  {selected[1]}\n
            Price:  {selected[2]}\n
            Number:  {selected[3]}"""
            )         
                
        
if __name__ == "__main__":
    filename = "test.txt"
    customer = "John"
    
    added = add_new_product("zouber","da",12,14)
    print(added)
    print(product_list)
    
    add = sell_product("Zouber",11)
    print(add)
    print(product_list)
    list_products("*")
    #doctest.testmod(extraglobs={"product_list": []})  