from Utilities import *
from specialization import *


class Backend:
    def __init__(self):
        self.Database = Specialization()  # Assuming this initializes a dictionary for specializations
        self.Max_Queue = 10  # Maximum number of patients allowed in each specialization

    def add_dummy_data(self):
        # You can implement this method to add dummy patient data for testing
        pass

    def Check_specialization_size(self, specialization):
        # Check if the size of the queue for the given specialization is within limits
        if specialization in self.Database.Database:  # Check if specialization exists
            queue_size = len(self.Database.Database[specialization])  # Get the size of the queue
            if queue_size >= self.Max_Queue:
                print("Cannot add any more patients to this specialization at the moment.")
                return False
        return True

    def Add_patient(self, specialization, Name, status):
        # Check if the specialization exists, and if not, initialize it
        if specialization not in self.Database.Database:
            self.Database.Database[specialization] = []  # Create a new list for the specialization
            print(f"Specialization '{specialization}' created.")

        # Check if the specialization is within queue limits
        if self.Check_specialization_size(specialization):
            # Add patient using the add_patient method of the Specialization class
            self.Database.add_patient(specialization, Name, status)
            print(f"Patient '{Name}' added to specialization '{specialization}'.")
        else:
            print(f"Could not add patient '{Name}' to specialization '{specialization}'.")

    def Get_the_Next_patient(self, specialization):
        self.Database.Get_Next_patient(specialization)

    def Printing_all_patient(self):
        # Print all patients in each specialization
        for spec, patients in self.Database.Database.items():
            print(f"Specialization: {spec}")
            if not patients:
                print(" - No patients in this specialization.")
            for patient in patients:
                print(f" - {patient}")  # Assuming __str__ is defined in Patient class

    def Remove_leaving_patient(self, specialization, name):
        # Remove a patient based on name if they exist in the specialization's queue
        if specialization in self.Database.Database:
            patients = self.Database.Database[specialization]
            for patient in patients:
                if patient.name == name:  # Assuming Patient class has a 'name' attribute
                    patients.remove(patient)  # Remove the patient
                    print(f"Removed patient '{name}' from specialization '{specialization}'.")
                    return
            print(f"Patient '{name}' not found in specialization '{specialization}'.")
        else:
            print(f"Specialization '{specialization}' does not exist.")

# Example usage to test print statements
if __name__ == "__main__":
    backend = Backend()
    backend.Add_patient("Cardiology", 1, 2)  # This will create "Cardiology"
    # backend.Add_patient("Cardiology", "Bob", "Critical")  # Adding another patient to "Cardiology"
    # backend.Add_patient("Neurology", "Charlie", "Stable")  # This will create "Neurology"
    # backend.Printing_all_patient()  # Print all patients to see the output
