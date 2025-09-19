
class bug_blueprint:                                                                                    
    def __init__ (self, id, summary, priority):                                                     #constructor
        self.id = id
        self.summary = summary
        self.priority = priority
        self.status = "OPEN"

    def show_details(self):                                                                         #polymorphism
        return f"{self.id}  ||  {self.summary}  ||  {self.priority} ||  {self.status}"
    
    def update_status(self, new_status):
        self.status = new_status
    

class bingo_blueprint(bug_blueprint):                                                               #inheritance
    def __init__(self, id, summary, priority, sprint):
        super().__init__(id, summary, priority)
        self.sprint = sprint
    
    def show_details(self):                                                                         #polymorphism
        base = super().show_details()
        return f"{base} ||  {self.sprint}"


class private_id:                                                                                   #encapsulation
    def __init__(self, id, summary):
        self.__id = id
        self.summary = summary
    
    def get_private_id(self):
        return self.__id


defect1 = bug_blueprint("ABS-2000","no invoice shown","blocker")
print(f'\nSHOW DETAILS: {defect1.show_details()}')
print('UPDATE STATUS') 
defect1.update_status("IN ISOLATION")
print(f'SHOW UPDATED DETAILS: {defect1.show_details()}')


defect2 = private_id("MNO-13","Game Crash")
print(f"\nCALLING PRIVATE ID: {defect2.get_private_id()}")

defect3 = bingo_blueprint("BINGO-009","blank screen","critical","Q4 Sprint")
print(f"\nSHOW BINGO DETAILS: {defect3.show_details()}")
print('UPDATE STATUS')
defect3.update_status("TEST IN PROGRESS")
print(f"SHOW UPDATED BINGO DETAILS: {defect3.show_details()}")