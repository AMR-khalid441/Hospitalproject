from patient import *
class Specialization:
    def __init__(self) -> None:
        self.Database = {}

    def add_patient(self, spec, Name, status):
        if spec not in self.Database:
            self.Database[spec] = []

        # Add the new patient
        self.Database[spec].append(Patient(Name, status))
        
        # Now sort the patients based on your comparison function
        self.Database[spec].sort()
    def Get_Next_patient(self, specialization):
        if specialization not in self.Database:
            print(f"sorry the specialization  {specialization}  is not in Database")
            return False
        if len(self.Database[specialization])<0:
            print(f"sorry the specialization  {specialization}  is Empty")
            return False
        self.Database[specialization].pop(0)
        print(f"the Next patient is {self.Database[specialization][0]}")
        return True
   
    


    