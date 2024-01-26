
class Seat():
    # Initializing a Seat object, with two attributes.
    # free: bool. Indicates whether the seat is taken or not. It is by default True.
    # occupant: string. This can take in a string of the person's name. Empty string by default.
    def __init__(self, occupant: str = "", free: bool = True):
        self.free = free
        self.occupant = occupant
    
    def set_occupant(self, name: str):
        """Method to seat seat a person to a Seat() object.  
        The method checks whether the seat object is empty,
        if yes, then it takes the argument, name, and assigns its value as the occupant of the initialized Seat object.

        Args:
            name (str): A string value with the name of the person to be seated.
        """
    # Method to set the occupant of the seat.
    # Checks if the seat is taken. If is free: it assigns a name to the occupant attribute, and set the free attribute to False.
    # If the seat is not free, then it prints: "This seat is already taken!"
        if self.free == True:
            self.occupant = name
            self.free = False
        elif self.free == False:
            return("This seat is already taken!")
    
    def remove_occupant(self):
        """This method will check whether the seat object has been assigned a name as occupant, and removes it.
        """
    # Method to remove occupants from a certain seat. 
    # If the seat is not free, this method will replace the name with an empty string and set the free attribute to True.
        if self.free == False:
            self.occupant = ""
            self.free = True
     
class Table():
# Initialize a Table object. 
# Seats is a list that takes in the generated Seat objects up to 4. (One table's capacity is 4).
# The table has a fixed capacity of 4 seats. 

    def __init__(self, capacity = 4):
        self.capacity = capacity
        self.seats = []
    # defining the two attributes as normal
    # initializing seats, which is a list object attribute, containing objects created with Seats.   
        for s in range(capacity):
            self.seats.append(Seat())
        #print(self.seats)  
        #print([seat.occupant for seat in self.seats])
        
    def has_free_spot(self):
    # this object needs to check whether the table has free seats left.
    # first it iterates over the objects of the seats list. 
    # then it checks whether the free attribute of the seat is True (therby the seat is true)
    # if any of them turns out to be free, this function will return True.
        if any([seat.free for seat in self.seats]):
            available_seats = sum(seat.free for seat in self.seats)
            print(f"There are {available_seats} available seats at this table.")
            return True 
        else:
            print("All of the seats are taken at this table.")
            return False    
                 
    def assign_seat(self,name):
        """Takes a list of names, and assigns them to a Seat object at a Table. 

        Args:
            name (str): A string, which is the name of the occupant.

        Returns:
            string: Indicates which person occupies the seat, or if it is free. 
        """
    #assigning a seat to a person at this table.
        if self.has_free_spot():                                      #calls the method: has_free_spot and if yes, it executes.
            for s in self.seats:  
                if s.free == True:
                    s.set_occupant(name)                           #iterates through the list of seat objects and assigns a seat to an occupant                               
                    break                                           #the loop needs to be breaked, since the person found a seat. 
            #[name for self.occupant in self.seats]
            print(f"{name} is seated at this table.")              #Prints who was seated at the table.
                 
        else:
            print("All of the seats are taken at this table.")             #If there was no empty seats, the program prints this.
    
    def capacity_left(self):     
        #counts how many empty seats are there at this table. 
        cap_left = 0                                    
        for s in self.seats:
            if s.free:
                cap_left += 1
        print(f"There are {cap_left} more seats at this table.")
        return cap_left    

#TEST for the seating:
#s1=Seat()
#s1.free
#print(s1.free)
#print(s1.occupant)
#s1.set_occupant("Léa")
#print(s1.free)
#print(s1.occupant)
#s1.remove_occupant()
#print(s1.free)
#print(s1.occupant)

#t1=Table()
#print(t1.has_free_spot())
#print(t1.capacity_left())
#t1.assign_seat("Brian")
#print(t1.capacity_left())