class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passengers = []
    def addPassenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
   
    def open_seats(self):
        return self.capacity - len(self.passengers)

flight = Flight(3)
persons =["Ehsan","Rahim","Roshan","Ali"]

for person in persons:
    success = flight.addPassenger(person)
    if success: 
        print(f" {person} is added to flight ")
    else: 
        print(f"No seats available for {person}")

