class Students:
    def __init__(self,name,roll,email,dept):
        self.name=name 
        self.roll=roll
        self.email=email
        self.dept=dept
    
    def to_dict(self):
        return {
            "name" : self.name,
            "roll" : self.roll,
            "email" : self.email,
            "dept" : self.dept
        }