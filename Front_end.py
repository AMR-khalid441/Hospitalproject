from Back_end import *
from Utilities import *
class Front_end:
    def __init__(self):
        self.BK=Backend()
    def run(self):
        Options=[
            "1) Add new patient",
            "2) Print all the patients",
            "3) Get the next patient",
            "4) Remove a leaving patient",
            "5) End the program"
        ]
        printing_list(Options)
       
        while True:
            Choice=add_value(1,5)

            if Choice == 1:
                specialization =add_value(1,20)
                Name=input("put the name ")
                status=add_value(0, 2)
                self.BK.Add_patient(specialization,Name,status)
            elif Choice == 2:
                self.BK.Printing_all_patient()
            elif Choice == 3:
                specialization =add_value(1,20)
                self.BK.Get_the_Next_patient(specialization)
            elif Choice == 4:
                Name =input("put patient Name ")
                specialization =add_value(1,20)
                self.BK.Remove_leaving_patient(Name,specialization)
            elif Choice == 5:
                print("End the program")
                break
    


  
