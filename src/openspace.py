from src.table import Table
from src.table import Seat
from datetime import datetime
import random
import pandas as pd


class OpenSpace():
    #This class represents the whole open space with the 6 tables, each with 4 seats.
    #The class has arguments, such as the list of the table objects created
    #the class also has a number_of_tables attribute, which represents the capacity of the Space, 6 tables in total.
    def __init__(self,tables=[],number_of_tables=6):
        self.tables = tables
        self.number_of_tables = number_of_tables
        for t in range(number_of_tables):              #the loop iterates through objects created by the Table() class to a list (up to the space's capacity)
            tables.append(Table())
    
    def organize(self, names):
        """Method, to organize the seating of the Open Space, by assigning names to the seats at the tables in the space.
            Takes in a list of strings and randomly assigns them to the generated Seat and Table objects.

        Args:
            names (list): A list of strings (names)
        """
        random.shuffle(names)
        seated =[]
        not_seated = []
        # This method will randomly assign people to the seat objects at the different table objects.
        for table in self.tables:
            for name in list(names):
                if table.has_free_spot():  # Check if the table has free spots
                    table.assign_seat(name)  # Assign a seat to the person
                    seated.append(name)      #Adds a name to 
                    names.remove(name)  # Remove the assigned person from the list of names
                    if len(seated)==len(names):
                        break
                else:
                    not_seated.append(name)
                    break
                    
        if not_seated:
            print("The following individuals could not be seated:")
            for name in not_seated:
                print(name)      
                             
    def display(self):
        """Displays the order of the seating. 
        """
        #this method will display all the tables with the seats and their occupants. 
        for t, table in enumerate(self.tables):
            # iterates through all the table obects and assigns an index for them
                print(f"Table {t + 1}:")
                # prints the table and its number
                for s, seat in enumerate(table.seats):
                    #iterates through all the indexed seats
                    #if not seat.free:
                        #prints the seat and its occupant if it is not free. 
                    print(f"{s + 1} - {seat.occupant}")
                    #prints the seat and its occupant
        
        
    def store(self, filename):
        """Stores the final seating allocation in a file.

        Args:
            filename (string): The name by which the file will be saved containg the output of the program.
        """
        #today_date = datetime.now()
        #filename = f"{today_date} + seating.xlsx"
        seating = []
        for t, table in enumerate(self.tables):
            for seat in table.seats:
                seating.append({'Table': t + 1, 'Seat': seat.occupant})
        df = pd.DataFrame(seating)
        df.to_excel(filename, index=False, engine='openpyxl')

#TEST vol2:   
#space1 = OpenSpace() 
#space1.organize(["Archana", "Polina", "Omar"])
#space1.display()