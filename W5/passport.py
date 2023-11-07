from datetime import *

class Passport:
    def __init__(self, first_name, last_name, dob, country, exp_date):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.country = country
        self.exp_date = datetime.strptime(exp_date, "%Y-%m-%d").date()

    def is_valid(self):
        if(self.exp_date > datetime.now().date()):
            return True
        else:
            return False

    def summary(self):
        isvalid = "valid" if self.is_valid() else "invalid"
        return f"This passport belongs to {self.first_name} {self.last_name}, born on {self.dob}, in {self.country}. It is {isvalid}."

    def check_data(self, first_name, last_name, dob, country):
        return (first_name == self.first_name and
                last_name == self.last_name and
                dob == self.dob and
                country == self.country and
                self.is_valid())    
        

        
    
        
        