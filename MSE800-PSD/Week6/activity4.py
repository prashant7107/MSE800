# Use 1 : format large numbers
population = (-9234_394234_213) 
print(f"1. Large population: {population}")

# Use 2 : ignore a value
values = (111,222,333)
a,b,_ =values
print(f"values :  {a}  {b}")

class show_private:
    # Use 3 : System-defined
    def __init__(self,value):
        # Use 4 declaring private variable
        self.__val = value

        # Method to update private variablex
    def user_private_variable(self,new_val):
        self.__val = new_val