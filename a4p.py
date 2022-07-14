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
    
    >>> load_inventory("test.txt")
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
        pdb.set_trace()
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
    
    
  
if __name__ == "__main__":
    filename = "test.txt"
    customer = "John"
    
    
    doctest.testmod()  