class Patient:
   

    def __init__(self, name: str, status: int):
        self.name = name
        self.status = status
        self.STATUS_OPTIONS = ["Normal", "Urgent", "Super Urgent"]

    def __str__(self) -> str:
        # Use the STATUS_OPTIONS to get the corresponding status string
        status_str =self.STATUS_OPTIONS[self.status ]
        return f"Patient name is {self.name} and their status is {status_str}"

    def __lt__(self, other: 'Patient') -> bool:
        # Compare patients based on their status; lower numerical status means higher priority
        return self.status < other.status

# Example usage
if __name__ == "__main__":
    p1 = Patient("Alice", 1)
    p2 = Patient("Bob", 2)

    print(p1)  # Output: Patient name is Alice and their status is Urgent
    print(p2)  # Output: Patient name is Bob and their status is Super Urgent
    print(p1 < p2)  # Output: True (Alice has higher priority)
