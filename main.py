#imports here
import csv
from src.openspace import OpenSpace
from src.table import Table
import pandas as pd

if __name__ == "__main__":
    # this will be the main program. 
    file = input("Please provide the name of the file with the collagues to be seated:")
    colleagues_df = pd.read_excel(file, header=None)
    col_list = colleagues_df.values.tolist()
    #print(col_list)
    #print(len(col_list))
    col_sum=len(col_list)
    if col_sum > 24:
        print(f"There are too many people waiting to be seated ({col_sum}), and there are only 24 seats availabe. Please add more seats!")
    space=OpenSpace()
    space.organize(col_list)
    space.display()
    space.store(input("Please give your file a name:")+".xlsx")
    
    
        
        

            
    